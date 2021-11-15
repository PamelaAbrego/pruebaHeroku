from flask import Flask, render_template
from flask_cors import CORS, cross_origin
#import pywhatkit

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/")
def home():
    mensaje = "Hola"
    celular = "+50379241086"
    #pywhatkit.sendwhatmsg_instantly(celular, mensaje)
    return render_template("main.html")
        

if __name__ == "__main__":
    app.run(debug=True)