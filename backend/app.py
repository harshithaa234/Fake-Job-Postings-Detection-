from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import os
import logging
from html import escape

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Get absolute paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Verify templates directory
if not os.path.exists(TEMPLATES_DIR):
    logger.error(f"Template directory not found at {TEMPLATES_DIR}")
    raise FileNotFoundError(f"Template directory not found at {TEMPLATES_DIR}")

# List template files
try:
    template_files = os.listdir(TEMPLATES_DIR)
    logger.info(f"Template folder contents: {template_files}")
    required_templates = ['home.html', 'about.html', 'contact.html', 'dashboard.html', 'form.html', 'result.html']
    for template in required_templates:
        if template not in template_files:
            logger.error(f"Required template {template} not found in {TEMPLATES_DIR}")
            raise FileNotFoundError(f"Required template {template} not found in {TEMPLATES_DIR}")
except Exception as e:
    logger.error(f"Error accessing template folder: {e}")
    raise

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

# Log paths
logger.info(f"Base directory: {BASE_DIR}")
logger.info(f"Template folder: {TEMPLATES_DIR}")
logger.info(f"Static folder: {STATIC_DIR}")

# Model and vectorizer paths
model_path = r"C:\Users\reeth\Projects\Mini Project-Fake_job_posts\website\backend\model\rf_fake_job_model.pkl"
vectorizer_path = r"C:\Users\reeth\Projects\Mini Project-Fake_job_posts\website\backend\model\vectorizer_rf.pkl"

# Check model and vectorizer files
if not os.path.exists(model_path):
    logger.error(f"Model file not found at {model_path}")
    raise FileNotFoundError(f"Model file not found at {model_path}")

if not os.path.exists(vectorizer_path):
    logger.error(f"Vectorizer file not found at {vectorizer_path}")
    raise FileNotFoundError(f"Vectorizer file not found at {vectorizer_path}")

# Load model and vectorizer
try:
    model = joblib.load(model_path)
    logger.info(f"Model loaded successfully from {model_path}")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise

try:
    vectorizer = joblib.load(vectorizer_path)
    logger.info(f"Vectorizer loaded successfully from {vectorizer_path}")
except Exception as e:
    logger.error(f"Error loading vectorizer: {e}")
    raise

@app.route('/')
def home():
    logger.info("Serving home page")
    return render_template('home.html')

@app.route('/about')
def about():
    logger.info("Serving about page")
    return render_template('about.html')

@app.route('/contact')
def contact():
    logger.info("Serving contact page")
    return render_template('contact.html')

@app.route('/dashboard')
def dashboard():
    logger.info("Serving dashboard page")
    return render_template('dashboard.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    logger.info(f"Form route accessed with method: {request.method}")
    if request.method == 'POST':
        try:
            data = request.form
            required_fields = ['title', 'description', 'company', 'location']
            sanitized_data = {}
            for field in required_fields:
                if field not in data or not data[field].strip():
                    logger.warning(f"Missing or empty field: {field}")
                    return render_template('form.html', error=f"Missing or empty field: {field}")
                sanitized_data[field] = escape(data[field].strip())

            input_data = pd.DataFrame({
                'title': [sanitized_data['title']],
                'description': [sanitized_data['description']],
                'company': [sanitized_data['company']],
                'location': [sanitized_data['location']]
            })

            # Preprocess data with vectorizer
            text_data = input_data['title'] + ' ' + input_data['description'] + ' ' + \
                        input_data['company'] + ' ' + input_data['location']
            features = vectorizer.transform(text_data)

            prediction = model.predict(features)[0]
            confidence = model.predict_proba(features)[0][prediction] * 100
            prediction_text = 'Fake' if prediction == 1 else 'Real'

            logger.info(f"Prediction: {prediction_text}, Confidence: {confidence:.2f}%")

            return redirect(url_for('result', prediction=prediction_text, confidence=confidence))
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            return render_template('form.html', error=str(e))

    return render_template('form.html')

@app.route('/result')
def result():
    prediction = request.args.get('prediction', 'Unknown')
    confidence = request.args.get('confidence', 'N/A')
    try:
        confidence = f"{float(confidence):.2f}"
    except (ValueError, TypeError):
        confidence = 'N/A'

    logger.info(f"Serving result page: Prediction={prediction}, Confidence={confidence}%")

    return render_template('result.html', prediction=prediction, confidence=confidence)