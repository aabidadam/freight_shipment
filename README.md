# Shipment Delay Prediction

## Problem Statement
The aim of this project is to build an AI model capable of predicting whether a shipment will be delayed or on time based on historical data. This predictive solution helps logistics companies to proactively manage delays and optimize their operations.

## Solution
This project involves building a machine learning classification model to predict shipment delays. The project is structured in the following steps:

### 1. Data Cleaning and Preprocessing
- **Handling Missing Values:** Null values in the dataset were identified and treated using mode values in place of Null.
- **Data Transformation:** Categorical features were encoded, and numerical features were scaled as necessary to make the dataset suitable for modeling.

### 2. Exploratory Data Analysis (EDA)
- EDA was conducted to understand the distribution of the data, identify patterns, and explore relationships between features.
- Visualizations such as bar graphs were generated to gain insights into the data.

### 3. Model Training
Two models were trained and evaluated:
- **Logistic Regression:** A simple and interpretable model used as a baseline.
- **Random Forest Classifier:** A more robust and complex model, which provided better performance in terms of accuracy and other evaluation metrics.

The **Random Forest Classifier** outperformed Logistic Regression and was selected as the final model for deployment. Hyperparameter tuning was performed using grid search to optimize the model’s performance.

### 4. Deployment
- The final model was saved using **Pickle**, a Python library for serializing and deserializing objects.
- A **Flask** web application was developed to provide a user-friendly interface where users can input shipment data and receive predictions on whether the shipment will be delayed or on time.

### 5. Repository Structure
The complete codebase, including data cleaning, EDA, model training, and Flask integration, is available in this GitHub repository. Key files and directories include:
- `Fright_Tiger_problem1.ipynb`: Jupyter notebooks for data cleaning, EDA, and model training.
- `model.pkl`: Serialized model files (Pickle format).
- `app.py`: Flask application code.
- `requirements.txt`: List of Python dependencies.
- `label_encoders.pkl`: Label encoder for categorical colunm(pickle format).
## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/aabidadam/freight_shipment.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Access the web interface at `http://localhost:5000` and input shipment details to get predictions.

## you can also directly accesss by the `https://freight-shipment.onrender.com`


## Results
The **Random Forest Classifier** achieved an accuracy of 91% on the test dataset, outperforming Logistic Regression by 62%. The detailed evaluation metrics are documented in the EDA and model training notebooks.

## Conclusion
This project demonstrates how machine learning can be effectively applied to solve real-world problems in logistics. By predicting shipment delays, this solution can help businesses improve their operational efficiency and customer satisfaction.

