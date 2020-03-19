from flask import Flask, render_template
import scrape as s

app = Flask(__name__)
data = s.scrape()

@app.route("/")
def main_():
	return render_template("index.html", data=data)

if __name__ == "__main__":
	app.run()