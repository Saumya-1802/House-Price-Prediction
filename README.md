# 🏡 House Price Predictor (Python, Flask, XGBoost, Scikit-learn, Pandas, HTML/CSS)

A Flask web application that predicts house prices using an XGBoost regression model trained on the Ames Housing dataset.

![WhatsApp Image 2025-07-05 at 12 08 53_add615bb](https://github.com/user-attachments/assets/05592e13-bd4d-49c4-8c4f-2af2954eb9c5)

![WhatsApp Image 2025-07-05 at 12 09 39_3b2d253e](https://github.com/user-attachments/assets/10710ef2-e3e0-4592-8446-29f9d169eacc)

![WhatsApp Image 2025-07-05 at 12 10 12_2d02127f](https://github.com/user-attachments/assets/550ee018-62b5-4591-ac65-baa37092f8c4)

![WhatsApp Image 2025-07-05 at 12 10 42_026ac12c](https://github.com/user-attachments/assets/782bf367-c515-44a3-b5b7-bacd48616936)


🚀 Features

Predicts house prices based on top 20 features selected via XGBoost feature importance.

Achieves R²: 0.91, MAE: ~16K USD (~8% error) on test data.

Preprocessing: mean imputation, one-hot encoding, and feature selection.

Clean, responsive HTML/CSS interface with gradient animations and form validation.

Runs locally via Flask.

⚙️ Tech Stack

Python

Flask

XGBoost

Scikit-learn

Pandas

HTML/CSS

📂 Project Structure

.
├── app.py               # Flask app backend
├── xgb_model.json       # Saved XGBoost model
├── model_columns.pkl    # Columns used by the model
├── templates/
│   ├── form.html        # Input form page
│   └── result.html      # Result display page
└── requirements.txt     # Python dependencies

🛠️ Setup Instructions

1️⃣ Clone the repository:

git clone https://github.com/Saumya-1802/House-Price-Prediction.git
cd House-Price-Prediction

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the app:

python app.py

4️⃣ Open your browser at:

http://127.0.0.1:5000


📈 Model Performance

| Metric | Training   | Test        |
| ------ | ---------- | ----------- |
| R²     | 0.9841     | 0.9128      |
| MAE    | \~7.4K USD | \~16.3K USD |
| RMSE   | \~9.9K USD | \~24K USD   |




