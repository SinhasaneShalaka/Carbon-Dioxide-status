
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load your model and data
# Replace this with the actual path to your dataset and model
data_path = 'data\CO2.csv'
model_path = 'artifacts\random_forest_model.pkl'
col_data = pd.read_csv(data_path)
model = RandomForestRegressor()  # Load your trained model

# Assume le_type is a global variable or obtained from somewhere else in your code
le_type = LabelEncoder()

@app.route('/')
def home():
    return render_template('index.html')

# Categorical Column APIs
@app.route('/api/get_plants', methods=['GET'])
def get_plants():
    plants = col_data['Plant'].unique().tolist()
    return jsonify({'plants': plants})

@app.route('/api/get_types', methods=['GET'])
def get_types():
    types = col_data['Type'].unique().tolist()  # Fetch unique values for 'Type'
    return jsonify({'types': types})

@app.route('/api/get_treatments', methods=['GET'])
def get_treatments():
    treatments = col_data['Treatment'].unique().tolist()
    return jsonify({'treatments': treatments})

# Prediction API
@app.route('/api/predict_emission', methods=['POST'])
def predict_emission():
    try:
        # Assuming the form has 'Plant', 'Type', 'Treatment' fields
        data = request.form.to_dict()

        # Debugging: Print input data
        print("Input Data:", data)

        # Transform categorical variables
        data['Type'] = le_type.transform([data['Type']])[0]

        # Debugging: Print transformed data
        print("Transformed Data:", data)

        # Create a DataFrame for prediction
        input_data = pd.DataFrame([data])

        # Debugging: Print input_data
        print("Input DataFrame:", input_data)

        # Make sure the columns in input_data match the columns used for training
        # If necessary, handle missing columns or add default values

        # Make prediction
        predicted_uptake = model.predict(input_data)
        # Assuming your model returns an array, use [0] to get the first prediction

        # Debugging: Print predicted_uptake
        print("Predicted Uptake:", predicted_uptake)

        return jsonify({'predicted_uptake': predicted_uptake})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
