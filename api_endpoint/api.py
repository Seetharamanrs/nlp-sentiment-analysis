from flask import Flask,jsonify,request
import joblib
from src.preprocessing import preprocessing
app=Flask(__name__)
model=joblib.load("models/lr_model.pkl")
vect=joblib.load("models/tfidf_vectorizer.pkl")

def processing(data):
    cleaned=preprocessing(data)
    vector=vect.transform([cleaned])
    prediction=model.predict(vector)
    return prediction[0]
@app.route("/")
def home():
    return " API running! "
@app.route("/predict",methods=['POST'])
def predict():
    data=request.get_json()
    review=data['review']
    prediction=processing(review)
    return (jsonify({"Prediction": prediction}))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)