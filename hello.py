/*
This script illustrate the basics of flash
*/

from flash import Flask

app = Flash(__name__)

@app.route("/")
def hello_world():
	return "<p> Hello, world!</p>"
