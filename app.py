from flask import Flask, request, render_template, session, redirect, url_for
from flask_cors import CORS, cross_origin
import pywhatkit

app = Flask(__name__)

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")
    elif request.method == "POST":
        celular = "+50379241086"
        mensaje="hola"
        pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)
        return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)