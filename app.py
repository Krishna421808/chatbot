from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import get_response 

app= Flask(__name__)
cors= CORS(app)
# This will redirect us to our main or chatbox page
@app.get("/")
def index_get():
    return render_template("index.html")
# This is used for taking the user input and giving response to the user by prediction based on the model training
@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    response= get_response(text)
    message={"answer": response}
    return jsonify(message)

if __name__=="__main__":
  app.run(debug=True)