// PROJECT: GoGUI
//
// MAINTAINED BY: hkdb <hkdb@3df.io>
//
// SPONSORED BY: 3DF OSI - https://osi.3df.io
//
// This application is maintained by volunteers and in no way
// do the maintainers make any guarantees. Use at your own risk.
package main

import (
	"fmt"
	"log"
	"net"
	"net/http"
	"path/filepath"

	"github.com/skratchdot/open-golang/open"
	"github.com/sqweek/dialog"
	"github.com/zserge/webview"

	b64 "encoding/base64"
)

const (
	windowWidth  = 600
	windowHeight = 700
	title        = "SSHshare"
	version      = "v0.2.0"
)

// WebView Object
var debug = true
var w = webview.New(debug)

// User Input
var file string
var key string
var direction string

// Load Logo
var logo = MustAsset("assets/header.png")

var indexHTML = `<!doctype html>
<html>	
	<head>
		<title>SSHshare</title>
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
	</head>

	<style>
		body {
			background-color: 303030;
		}
			
		h1 {
			color: white;
			text-align: center;
		}
		
		.general {
			color: white;
			font-family: Roboto;
			font-size: 14px;
			text-align: center;
			padding-bottom: 20px;
		}

		.file {
			border: 0px;
			cursor: pointer;
			display: inline-block;
			font-family: "Font Awesome 5 Pro";
			font-size: inherit;
			font-weight: 100%;
			margin-bottom: 1rem;
			outline: none;
			padding: 10px;
			min-width: 220px;
			max-width: 220px;
			vertical-align: middle;
			overflow: hidden;
			text-overflow: ellipsis;
			background-color: #cccccc;
			border-radius: 5px;
			position: relative;
		}

		.file:hover {
			filter: brightness(85%);
		}

		.submit {
			border: 0px;
			cursor: pointer;
			display: inline-block;
			font-family: "Font Awesome 5 Pro";
			font-size: inherit;
			font-weight: 100%;
			margin-bottom: 1rem;
			outline: none;
			padding: 10px;
			min-width: 120px;
			max-width: 120px;
			vertical-align: middle;
			overflow: hidden;
			text-overflow: ellipsis;
			background-color: #aac734;
			border-radius: 25px;
			position: relative;
			filter: brightness(85%);
		}

		.submit:hover {
			filter: brightness(120%);
		}

		.loader {
			border: 10px solid #4d4d4d;
			border-top: 10px solid #42791c;
			border-radius: 50%;
			width: 20px;
			height: 20px;
			animation: spin 2s linear infinite;
			display: table;
			margin: 0 auto;
			visibility: hidden;  
		  }
		  
		  @keyframes spin {
			0% { transform: rotate(0deg); }
			100% { transform: rotate(360deg); }
		  }

	</style>
	
	<body bgcolor="#303030">
		<br>
		<br>
		<center><img src="data:image/png;base64, ` + string(b64.StdEncoding.EncodeToString([]byte(logo))) + `"></center>
		<br>
		<center><font face="Roboto" color="#cccccc" size=2>An <a href="javascript:handle('openosi')">OSI</a> application sponsored by <a href="javascript:handle('open3df')">3DF</a></font></center>
		<center><font face="Roboto" color="#cccccc" size=2>` + version + `</font></center>
		<br>
		<div class="general">
			<select id="direction" onselect="setDirection('this.value')">
				<option value="encrypt" selected>Encrypt</option>
				<option value="decrypt">Decrypt</option>
			</select>
			<br>
			<br>
			<p style="padding: 0px; margin: 10px">FILE:</p>
			<button id="file" class="file" onclick='selectDialog("file")'><svg xmlns="http://www.w3.org/2000/svg" width="20" height="17" viewBox="0 0 20 17"><path d="M10 0l-5.2 4.9h3.3v5.1h3.8v-5.1h3.3l-5.2-4.9zm9.3 11.5l-3.2-2.1h-2l3.4 2.6h-3.5c-.1 0-.2.1-.2.1l-.8 2.3h-6l-.8-2.2c-.1-.1-.1-.2-.2-.2h-3.6l3.4-2.6h-2l-3.2 2.1c-.4.3-.7 1-.6 1.5l.6 3.1c.1.5.7.9 1.2.9h16.3c.6 0 1.1-.4 1.3-.9l.6-3.1c.1-.5-.2-1.2-.7-1.5z"/></svg></button>
			
			<p style="padding: 0px; margin: 10px">SSH KEY:</p>
			<button id="key" class="file" onclick='selectDialog("key")'><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="17" viewBox="0 0 20 17">
			<image y="4" width="20" height="9" xlink:href="data:img/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAJCAYAAAAywQxIAAAAwUlEQVQokaXRsUqCURjG8Z/RDYgkbS55ATV5DW5uDY3OETS4CS7dS0O34KKT1dTQUkM4hEOrOATJqRc8+H3pRz3wcuDhOf/zvu+RaYg5vjBBzz80DtB2Xf0FeRmQF3RwjH4Grhdu7FANCzRxgtcsOoo1POI+svu0El18lgTPSlawtw7xgQZaeMuA3Tif8ICDwpM/SqA0Ycovk3Ed5jNOY2cXWSdHFUZtZ/lvTX8ZZVDxLxLwDre5eYP3AM1wXhG2EdbTfzv7jRNS5wAAAABJRU5ErkJggg=="/></svg></button>
			<br>
			<br>
			<button class="submit" value="submit" onclick="preSubmit()">Submit</button>
			  <br>
			  <br>
			<div id="loader" class="loader"></div>
		</div>
		<script>
			function preSubmit() {
				var dir = document.getElementById("direction").value;
				setDirection(dir);
				document.getElementById('loader').style.visibility = "visible";
				submit();
				document.getElementById('loader').style.visibility = "hidden";
				popup("done")
			}
			
		</script>
	</body>
</html>
`

func startServer() string {
	ln, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		log.Fatal(err)
	}
	go func() {
		defer ln.Close()

		http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
			w.Write([]byte(indexHTML))
		})

		log.Fatal(http.Serve(ln, nil))
	}()
	fmt.Println(ln.Addr().String())
	return "http://" + ln.Addr().String()
}

func handleRPC(data string) {
	switch {
	case data == "openosi":
		openl("https://osi.3df.io")
	case data == "open3df":
		openl("https://3df.io")
	case data == "file":
		filename, err := dialog.File().Load()
		if err != nil {
			fmt.Println("Can't read file...")
		} else {
			file = filename
			w.Eval("document.getElementById(\"file\").innerText = \"" + getFileName("file") + "\";")
			w.Eval("document.getElementById(\"file\").style.border = \"3px dashed black\";")
		}
	case data == "key":
		filename, err := dialog.File().Load()
		if err != nil {
			fmt.Println("Can't read file...")
		} else {
			key = filename
			w.Eval("document.getElementById(\"key\").innerText = document.getElementById(\"key\").innerText + \"" + getFileName("key") + "\";")
			w.Eval("document.getElementById(\"key\").style.border = \"3px dashed black\";")
		}
	}
}

//Helper for Opening URL with Default Browser
func openl(uri string) {
	err := open.Run(uri)
	fmt.Println(err)
}

func pop(msg string) {
	if msg == "done" {
		message := filepath.Base(file) + " has been " + direction + "ed successfully!"
		action := direction + "ed!"
		dialog.Message("%s", message).Title(action).Info()
	}
}

func getFileName(f string) string {
	var basename string
	if f == "file" {
		basename = filepath.Base(file)
	} else {
		basename = filepath.Base(key)
	}
	return basename
}

func submit(file string, key string, direction string) {
	// cmd := file + " - " + key + " - " + direction
	fmt.Println(direction)
}

func main() {

	url := startServer()

	defer w.Destroy()
	w.SetTitle(title)
	w.SetSize(windowWidth, windowHeight, webview.HintNone)
	w.Bind("toConsole", func(line string) {
		fmt.Println(line)
	})
	w.Bind("popup", func(msg string) {
		pop(msg)
	})
	w.Bind("handle", func(data string) {
		handleRPC(data)
	})
	w.Bind("selectDialog", func(t string) {
		handleRPC(t)
	})
	w.Bind("setDirection", func(d string) {
		direction = d
	})
	w.Bind("submit", func() {
		fmt.Println(file + " | " + key + " | " + direction)
	})
	w.Bind("quit", func() {
		w.Terminate()
	})
	w.Navigate(url)

	w.Run()

	// w.SetColor(77, 77, 77, 255)
}
