import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS, cross_origin

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))

# @app.route("/predictapi", methods = ["POST"])
# def predictapi():
#     # features = [np.array(float_features)]
#     # prediction = model.predict(features)
#     return render_template("tt.html", prediction_text = "The flower species is ")

@app.route("/api",methods = ["POST"])
@cross_origin()   
def api():
    return  jsonify({"data": [{"name": "jack"}]})

if __name__ == "__main__":
    app.run(debug=True)