# 🔗 Phishing URL Detector

A machine learning project to detect phishing websites based on URL features.  
This project uses **TF-IDF vectorization** and **XGBoost** for classification and is deployed locally using **Streamlit**.

---

## 📂 Project Structure

```bash
phishing-url-detector/
│
├── app/                  # Streamlit app (app.py)
├── data/                 # Dataset (optional or link to Kaggle)
├── models/               # Saved models (TF-IDF + XGBoost)
├── notebooks/            # Jupyter notebooks for training/EDA
│
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignored files (e.g., venv, __pycache__)
└── LICENSE               # License

## How to Run
1.Clone the repository
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector

2.Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

3.Run the Streamlit app
streamlit run app/app.py


## Dataset

The dataset was sourced from [Kaggle – Phishing Websites Dataset](https://www.kaggle.com/datasets/).  
It contains URLs labeled as:

- `1` → Benign (safe)  
- `0` → Phishing (malicious)  

This dataset was used to train and evaluate the machine learning model.


## Technologies Used
	• Python
	• Scikit-learn
	• XGBoost
	• Streamlit
	• Pandas / NumPy




