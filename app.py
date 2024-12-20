from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model and label encoders
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoders.pkl', 'rb') as encoders_file:
    label_encoders = pickle.load(encoders_file)

# Define the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        form_data = request.form
        # print(f"Form Data Received: {form_data}")

        # Extract and preprocess inputs
        string_features = ['Vehicle Type', 'Weather Conditions', 'Traffic Conditions', 'Origin', 'Destination']
        int_feature = 'Distance (km)'

        # Encode categorical inputs
        encoded_features = []
        for feature in string_features:
            value = form_data.get(feature)
            if value not in label_encoders[feature].classes_:
                return render_template('index.html', prediction_text=f"Invalid value for {feature}: {value}")
            encoded_value = label_encoders[feature].transform([value])[0]
            encoded_features.append(encoded_value)

        # Convert and validate the numeric input
        try:
            distance = int(form_data.get(int_feature))
        except ValueError:
            return render_template('index.html', prediction_text="Distance must be a valid integer.")
        
        encoded_features.append(distance)

        # Prepare input for the model
        final_features = [np.array(encoded_features)]
        print(f"Final features for prediction: {final_features}")

        # Make prediction
        prediction = model.predict(final_features)
        output = 'Delayed' if prediction[0] == 1 else 'On Time'

        # Return the prediction
        return render_template('index.html', prediction_text=f'Prediction: {output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
