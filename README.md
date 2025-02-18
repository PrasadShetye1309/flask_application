# Flask Application: House Price Prediction

This repository contains a Flask-based web application for predicting house prices using a machine learning model. The application takes various house features as input and predicts the estimated price.

## Project Structure

```
flask_application/
│-- static/
│   └── styles.css          # CSS for frontend styling
│-- templates/
│   ├── index.html          # Main page with input form
│   ├── result.html         # Page to display prediction results
│-- app.py                  # Main Flask application
│-- dataset.csv             # Housing dataset used for model training
│-- model.ipynb             # Jupyter Notebook for data analysis and model training
│-- requirements.txt        # Dependencies required to run the application
│-- xgb_model.jb            # Trained XGBoost model file
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask_application.git
   cd flask_application
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask application:
   ```sh
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

- Fill in the house details in the input form on the home page (`index.html`).
- Click the "Predict Price" button to submit the data.
- The predicted house price will be displayed on the result page (`result.html`).

## Model Details

- The model is trained using an **XGBoost** algorithm.
- The dataset (`dataset.csv`) contains historical house price data.
- The `model.ipynb` file includes data preprocessing, feature engineering, and model training.

## Dependencies

The `requirements.txt` file includes necessary Python packages, such as:
```
Flask
numpy
pandas
scikit-learn
xgboost
```

