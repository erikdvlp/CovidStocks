from flask import Flask, render_template
import scrape as s

app = Flask(__name__)
data = s.scrape()
indexes = data[:2]
stocks = data[2:]

@app.route("/")
def main_():
	return render_template("index.html", indexes=indexes, stocks=stocks)

if __name__ == "__main__":
	app.run()