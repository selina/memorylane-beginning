# import requests
# import json

# data = requests.get("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCj_bAQA7Rmxebtgaq08ykLXl1cxA03o0c").text


# print(data)


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		longitude = request.form["longitude"]
		latitude = request.form["latitude"]
		print(longitude)
		print(latitude)	
		return render_template("index2.html", longitude=longitude, latitude=latitude)
	else:
		return "Error, No data transerred"


# if __name__ == "__main__":
#     
app.run(debug=True)