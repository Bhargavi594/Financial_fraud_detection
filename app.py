from flask import Flask, request, jsonify
import joblib
import pandas as pd
import psycopg2

app = Flask(__name__)

model = joblib.load("../model/fraud_model.pkl")

conn = psycopg2.connect(
    database="frauddb",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transactions(amount, transaction_type, old_balance, new_balance, fraud_probability)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            data["amount"],
            data["transaction_type"],
            data["old_balance"],
            data["new_balance"],
            probability
        )
    )

    conn.commit()

    return jsonify({
        "fraud_prediction": int(prediction),
        "fraud_probability": float(probability)
    })

if __name__ == "__main__":
    app.run(debug=True)
