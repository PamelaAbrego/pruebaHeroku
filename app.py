from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import requests
import pywhatkit


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")
    else request.method == "POST":
        celular ="+50379241086"
        mensaje = "prueba"
        # pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)
        return render_template("main.html")

        

if __name__ == "__main__":
    app.run(debug=True)