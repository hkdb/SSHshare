#!/usr/bin/env python

###################################################################
### PROJECT:
### SSHshare
### VERSION:
### v0.1.2
### SCRIPT:
### SSHshare.py
### DESCRIPTION:
### GTK+ application to easily encrypt & decrypt files w/ ssh-vault
### MAINTAINED BY:
### hkdb <hkdb@3df.io>
### Disclaimer:
### This application is maintained by volunteers and in no way
### do the maintainers make any guarantees. Use at your own risk.
### ################################################################

import sys
import threading
import subprocess
import traceback
import queue
import os
import re
import webbrowser
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class MyWindow(Gtk.Window, threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        # Set Window Specification
        Gtk.Window.__init__(self, title="SSHshare - Share Secrets w/ SSH Keys")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(450, 300)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8, margin=20)
        self.add(self.box)

        # App Logo
        header = self.resource_path("header.png")
        self.image = Gtk.Image()
        self.image.set_from_file(header)
        self.box.pack_start(self.image, True, True, padding=20)

        # App About
        aLabel = Gtk.Label("<br>An Open Source Initiative Sponsored by 3DF")
        aLabel.set_markup("<small>An <a href=\"https://osi.3df.io\"" "title=\"OSI @ 3DF\">OSI</a> application sponsored by <a href=\"https://www.3df.com.hk\"" "title=\"3DF Ltd.\">3DF</a></small>")
        aLabel.connect("activate-link", self.link)
        self.box.pack_start(aLabel, True, True, 0)

        # App Version
        vLabel = Gtk.Label("v0.1.2")
        vLabel.set_justify(Gtk.Justification.CENTER)
        self.box.pack_start(vLabel, True, True, 0)

        # Separator
        bar = Gtk.HSeparator()
        self.box.pack_start(bar, True, True, 0)

        # Specify Action Type
        tLabel = Gtk.Label("Action Type:", xalign=0)
        self.box.pack_start(tLabel, True, True, 0)
        store = Gtk.ListStore(str)
        for item in ["Choose...", "Encrypt", "Decrypt"]:
            store.append([item])
        self.aType = Gtk.ComboBox()
        self.aType.set_model(store)
        self.aType.set_active(0)
        self.aType.connect("changed", self.on_combobox_changed)
        self.box.pack_start(self.aType, True, True, 0)
        cellrenderertext = Gtk.CellRendererText()
        self.aType.pack_start(cellrenderertext, True)
        self.aType.add_attribute(cellrenderertext, "text", 0)

        # Help Button - Action Types
        self.help = Gtk.Button(label="?")
        self.help.connect("clicked", self.on_help_clicked)
        self.box.pack_start(self.help, True, True, 0)

        # Separator
        bar1 = Gtk.HSeparator()
        self.box.pack_start(bar1, True, True, 0)

        # Specify SSH Key File
        sLabel = Gtk.Label("SSH Key File ~ public | private:", xalign=0)
        self.box.pack_start(sLabel, True, True, 0)
        self.sChooser = Gtk.FileChooserButton()
        self.box.pack_start(self.sChooser, True, True, 0)

        # Help Button - SSH Key Help
        self.help = Gtk.Button(label="?")
        self.help.connect("clicked", self.on_shelp_clicked)
        self.box.pack_start(self.help, True, True, 0)

        # Separator
        bar1 = Gtk.HSeparator()
        self.box.pack_start(bar1, True, True, 0)

        # Specify Input File w/ Content to Encrypt/Decrypt
        tLabel = Gtk.Label("Content File ~ .txt | .ssh:", xalign=0)
        self.box.pack_start(tLabel, True, True, 0)
        self.cChooser = Gtk.FileChooserButton()
        self.box.pack_start(self.cChooser, True, True, 0)

        # Help Button - File w/ Content to Encrypt/Decrypt
        self.cHelp = Gtk.Button(label="?")
        self.cHelp.connect("clicked", self.on_cHelp_clicked)
        self.box.pack_start(self.cHelp, True, True, 0)

        # Separator
        bar1 = Gtk.HSeparator()
        self.box.pack_start(bar1, True, True, 0)

        # Separator
        bar3 = Gtk.HSeparator()
        self.box.pack_start(bar3, True, True, 0)

        # Progress Bar
        pLabel = Gtk.Label("Status:", xalign=0)
        self.box.pack_start(pLabel, True, True, 0)
        self.progressbar = Gtk.ProgressBar()
        self.box.pack_start(self.progressbar, True, True, 1)
        show_text = True
        text = "Ready"
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)
        self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

        # Separator
        bar4 = Gtk.HSeparator()
        self.box.pack_start(bar4, True, True, 0)

        # Toggle Action
        self.button = Gtk.Button(label="GO!")
        self.button.set_sensitive(True)
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    # ComboBox Handler
    def on_combobox_changed(self, combobox):
        treeiter = combobox.get_active_iter()
        model = combobox.get_model()

    # Help Button Handler
    def on_help_clicked(self, widget):
        # Show Action Type Descriptions Help Dialog
        verbiage = "\n\n\nEncrypt:\n\nencrypt a text file with a specified SSH public key.\n\n\nDecrypt:\n\ndecrypt a file with your SSH private key.\n\n\n"
        self.info("Action Types", verbiage)
    
    # sHelp Button Handler
    def on_shelp_clicked(self, widget):
        # Show Action Type Descriptions Help Dialog
        verbiage = "\n\n\nEncrypt:\n\nSelect recipient public key file.\n\n\nDecrypt:\n\nSelect your private key file.\n\n\n"
        self.info("SSH Key File", verbiage)

    # cHelp Button Handler
    def on_cHelp_clicked(self, widget):
        # Show Output File Help Dialog
        verbiage = "A text file that contains the content to encrypt/decrypt"
        self.info("Content to Encrypt", verbiage)

    # Action Button Handler - Where all the magic happens
    def on_button_clicked(self, widget):
        # Disable Go Button
        self.button.set_sensitive(False)
        # Set Progress Bar Text to "Completed" and Progress Bar to Pulse
        self.progress()

        # Set Command Action Type Variable
        sFile = self.sChooser.get_filename()
        # sName = os.path.basename(sFile)
        cFile = self.cChooser.get_filename()
        cName = os.path.basename(cFile)
        slash = "/"
        oName = os.path.splitext(cName)[0]
        
        # Set Action Type
        aTypeIter = self.aType.get_active_iter()
        aTypeModel = self.aType.get_model()
        aType = aTypeModel[aTypeIter][0]

        # Set Ouput File based on Action Type  
        if aType == "Encrypt":
            oFullName = oName + ".ssh"
        elif aType == "Decrypt":
            oFullName = oName + ".txt"
        else:
            # Show Error Dialog - Exception
            verbiage = "Something went wrong! Action type not set."
            self.info("ERROR!", verbiage)
            # Set Progress Bar to Ready and Stop Pulsing
            self.ready()

        # If Any Input files are not specified, show an error dialog box
        if sFile == None or cFile == None:
            # Show Error Dialog
            verbiage = "The input file field is empty. Please specify an input file to encrypt/decrypt..."
            self.warning("ERROR!", verbiage)
            # Set Progress Bar Text to "Ready"
            self.ready()
            # Enable Action Button
            self.button.set_sensitive(True)

            return 1

        # If Input file does not end with .txt or .ssh, show an error dialog box
        if not cFile.endswith(".txt") and not cFile.endswith(".ssh"):
            # Show Error Dialog
            verbiage = "Only .txt or .ssh files can be encrypted or decrypted respectively with this application. Please specify a file with an accepted format."
            self.warning("ERROR!", verbiage)
            # Set Progress Bar Text to "Ready"
            self.ready()
            # Enable Action Button
            self.button.set_sensitive(True)

            return 1

        # Prep Action Type - Must happen before comparing cFile and oFile
        if cFile != None:
            cPath = os.path.dirname(os.path.realpath(cFile))
            oFile = cPath + slash + oFullName

        # If the Input File and Output File are the same, show an error dialog box
        if cFile == oFile:
            # Show Error Dialog
            verbiage = "The output file name cannot be the same as the input file name."
            self.warning("ERROR!", verbiage)
            # Set Progress Bar Text to "Ready"
            self.ready()
            # Enable Action Button
            self.button.set_sensitive(True)

            return 1

        # If Specified Input File Name Contains Unsupported Characters, Show Dialog Error Dialog Box and Return to Main Window
        # Security Procaution
        if re.search('[\\\\\|:;\`]', cName):
            verbiage = "The input file name contains unsupported characters. Please ensure your input file name does not contain special characters / \\ : ; \`"
            self.warning("Unsupported File Name Convention!", verbiage)
            self.button.set_sensitive(True)

            return 1

        # If Specified Output File Name Matches a File in the Output Directory
        if os.path.isfile(oFile):
            # Show Error Dialog
            verbiage = "There's a file with the same name, \"" + oName + "\" already in the directory. Are you sure you want to overwrite?"
            response = self.verify("WARNING!", verbiage)

            # If OK, then continue to overwrite existing file. If cancel, then stop and go back to main window
            if response == Gtk.ResponseType.CANCEL:
                self.ready()
                # Enable Action Button
                self.button.set_sensitive(True)

                return 1

        # Build gs Command
        if aType == "Encrypt":
            self.cmmd = 'ssh-vault -k ' + sFile + ' create < ' + cFile + ' ' + oFile
        elif aType == "Decrypt":
            self.cmmd = 'ssh-vault -k ' + sFile + ' -o ' + oFile + ' view ' + cFile
        else:
            # Show Error Dialog - Exception
            verbiage = "Something went wrong when building command"
            self.info("ERROR!", verbiage)
            # Set Progress Bar to Ready and Stop Pulsing
            self.ready()

        # Start Processing
        q = queue.Queue()
        cnow = threading.Thread(target=self.process, args=[q])
        cnow.start()
        # Keep Progress Bar Active
        while cnow.isAlive():
            Gtk.main_iteration_do(False)

        # Don't continue until thread is finished
        cnow.join(timeout=4)

        # Setup Queue to get try catch results
        success = q.get()

        # If try succeeds, tell user it succeeded, else, show an error dialog
        if success == True:

            # Set Progress Bar to Completed and Stop Pulsing
            self.completed()

            # Show Completion Dialog - Try Completed
            verbiage = "Processed! Enjoy! You can find the file at " + oFile
            self.info("Success!", verbiage)

        else:
            # Show Error Dialog - Exception
            verbiage = "Something went wrong! Maybe your file is corrupted?"
            self.info("ERROR!", verbiage)
            # Set Progress Bar to Ready and Stop Pulsing
            self.ready()

    # Informational Dialog Message
    def info(self, title, verbiage):
        # Show Info Dialog
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, title)
        dialog.format_secondary_text(verbiage)
        response = dialog.run()
        dialog.destroy()

    # Warning Dialog Message
    def warning(self, title, verbiage):
        # Pause Processing Progress Bar
        self.pause()
        # Show Error Dialog
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK, title)
        dialog.format_secondary_text(verbiage)
        response = dialog.run()
        dialog.destroy()

    # Verify What to Do Dialog Message
    def verify(self, title, verbiage):
        # Pause Processing Progress Bar
        self.pause()
        # Show Error Dialog
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL, title)
        dialog.format_secondary_text(verbiage)
        response = dialog.run()
        dialog.destroy()
        # Resume Processing Progress Bar & Continue
        self.resume()

        return response

    # Set Progress Bar Text to "Processing..." and Progress Bar to Pulse
    def progress(self):
        show_text = True
        text = "Processing..."
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)
        self.activity_mode = True
        self.progressbar.pulse()

    # Set Progress Bar Text to "Ready" and Progress Bar to Stop
    def ready(self):
        show_text = True
        text = "Ready"
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)
        self.activity_mode = False
        self.progressbar.set_fraction(0.0)
        # Enable Action Button
        self.button.set_sensitive(True)

    # Set Progress Bar Text to "Puased" and Progress Bar to Stop
    def pause(self):
        show_text = True
        text = "Paused"
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)
        self.activity_mode = False
        self.progressbar.set_fraction(0.0)

    # Set Progress Bar Text to "Processing..." and Progress Bar to Resume
    def resume(self):
        show_text = True
        text = "Processing..."
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)
        self.activity_mode = True
        self.progressbar.pulse()

    # Set Progress Bar Text to "Completed" and Progress Bar to Stop
    def completed(self):
        show_text = True
        text = "Completed"
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)
        self.activity_mode = False
        self.progressbar.set_fraction(0.0)
        # Enable Action Button
        self.button.set_sensitive(True)

    # Process Function to execute ssh-vault as SubProcess to be Called on a Separate Thread
    def process(self, out_queue):
        try:
            process = subprocess.Popen(self.cmmd, shell=True, stdout=subprocess.PIPE)
            out, err = process.communicate()
            out_queue.put(True)
        except:
            if err == None:
                print("There's an error with no trace data...")
            else:
                print(err)
            out_queue.put(False)

    # Progress Bar Status Handler
    def on_timeout(self, user_data):

        # Update value on the progress bar
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction()

            if new_value > 1:
                new_value = 0

            self.progressbar.set_fraction(new_value)

        # As this is a timeout function, return True so that it
        # continues to get called
        return True

    # Open WebBrowser for Links
    def link(self, widget, url):
        webbrowser.open(url)

    # Get Absolute Path of the Temp Work Directory
    def resource_path(self, relative_path):

        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

# Initiate Window
win = MyWindow()
win.start()
# win.set_icon_from_file("icon.icns") # Set App Icon
win.connect("destroy", Gtk.main_quit)
win.show_all()
# Bring to Front on Launch
win.set_keep_above(True)
# Allow to be backgrounded
win.set_keep_above(False)
Gtk.main()
