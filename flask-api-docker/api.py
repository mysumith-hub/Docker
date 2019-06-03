from flask import Flask
import os

app = Flask(__name__)

@app.route("/greetings")
def hello():
	html = "<h3>Hello {name}!</h3><b>Hostname:</b> Api<br/>"

	return html.format(name=os.getenv("NAME", "world"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
