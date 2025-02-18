from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained XGBoost model
model = joblib.load('xgb_model.jb')

# Feature names with full descriptions
feature_labels = {
    'OverallQual': 'Overall Quality (1-10)',
    'GrLivArea': 'Above Ground Living Area (sq ft)',
    'GarageArea': 'Garage Area (sq ft)',
    '1stFlrSF': 'First Floor Square Feet',
    'FullBath': 'Number of Full Bathrooms',
    'YearBuilt': 'Year Built',
    'YearRemodAdd': 'Remodel Year',
    'MasVnrArea': 'Masonry Veneer Area (sq ft)',
    'Fireplaces': 'Number of Fireplaces',
    'BsmtFinSF1': 'Basement Finished Area (sq ft)',
    'LotFrontage': 'Lot Frontage (feet)',
    'WoodDeckSF': 'Wood Deck Area (sq ft)',
    'OpenPorchSF': 'Open Porch Area (sq ft)',
    'LotArea': 'Lot Size (sq ft)',
    'CentralAir': 'Central Air Conditioning'
}

@app.route('/')
def index():
    return render_template('index.html', features=feature_labels)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    input_data = {
        'OverallQual': int(request.form['OverallQual']),
        'GrLivArea': float(request.form['GrLivArea']),
        'GarageArea': float(request.form['GarageArea']),
        '1stFlrSF': float(request.form['1stFlrSF']),
        'FullBath': int(request.form['FullBath']),
        'YearBuilt': int(request.form['YearBuilt']),
        'YearRemodAdd': int(request.form['YearRemodAdd']),
        'MasVnrArea': float(request.form['MasVnrArea']),
        'Fireplaces': int(request.form['Fireplaces']),
        'BsmtFinSF1': float(request.form['BsmtFinSF1']),
        'LotFrontage': float(request.form['LotFrontage']),
        'WoodDeckSF': float(request.form['WoodDeckSF']),
        'OpenPorchSF': float(request.form['OpenPorchSF']),
        'LotArea': float(request.form['LotArea']),
        'CentralAir': 1 if request.form['CentralAir'] == 'Yes' else 0
    }

    # Create DataFrame and make prediction
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    return render_template('result.html', 
                         prediction=f"${prediction:,.2f}",
                         input_data=input_data,
                         features=feature_labels)

if __name__ == '__main__':
    app.run(debug=True)