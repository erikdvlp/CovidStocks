from flask import Flask
import scrape as s

app = Flask(__name__)

results = s.scrape()
output = ""
for result in results:
	output += result.print()
	output += "<br>"

@app.route("/")
def main_():
	return output

if __name__ == "__main__":
	app.run()