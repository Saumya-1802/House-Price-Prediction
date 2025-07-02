from flask import Flask, render_template, request
import xgboost as xgb
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
model = xgb.Booster()
model.load_model("xgb_model.json")

# Load columns
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

top_features = [
    "OverallQual", "GarageCars", "GarageType_Detchd", "FullBath", "ExterQual_Gd",
    "GrLivArea", "ExterQual_TA", "CentralAir_Y", "2ndFlrSF", "BsmtFinSF1",
    "KitchenQual_TA", "Neighborhood_NoRidge", "TotalBsmtSF", "GarageType_Attchd",
    "Fireplaces", "YearBuilt", "YearRemodAdd", "1stFlrSF", "GarageType_BuiltIn",
    "GarageQual_TA"
]

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        input_data = {col: 0 for col in model_columns}
        for feat in top_features:
            val = request.form.get(feat, 0)
            try:
                val = float(val)
            except:
                val = 0
            input_data[feat] = val

        X_input = pd.DataFrame([input_data])
        dmatrix = xgb.DMatrix(X_input)
        prediction = model.predict(dmatrix)[0]
        return render_template("result.html", prediction=round(prediction, 2))

    return render_template("form.html", top_features=top_features)

if __name__ == "__main__":
    app.run(debug=True)
