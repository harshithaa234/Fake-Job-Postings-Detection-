# Fake-Job-Postings-Detection-


This project is an end-to-end machine learning web application that detects **fraudulent job postings** using **Natural Language Processing (NLP)** and **Machine Learning** techniques. It also incorporates **Explainable AI (XAI)** to help users understand why a job is predicted as fake or real.

---

##  Project Overview

Online job portals are flooded with fake job listings aimed at phishing or exploiting job seekers. This project helps combat that by providing a system where:

- Users can **input job details** (title, description, requirements, etc.)
- Or **upload a PDF job posting**
- The system **predicts if it's fake or real**
- **XAI explanations** (like SHAP or LIME) show which keywords or phrases led to the prediction

---

##  Tech Stack

| Component       | Tools Used                          |
|----------------|--------------------------------------|
|  Frontend     | HTML, CSS, Bootstrap                 |
|  Backend      | Python, Flask or FastAPI             |
|  ML Model     | Scikit-learn (Logistic Regression, Random Forest, etc.) |
|  Explainability | SHAP, LIME                        |
|  Dataset      | [Fake Job Postings - Kaggle](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) |
|  Deployment (Optional) | Render / Streamlit / Hugging Face Spaces |

---

Fake-Job-Postings-Detection/
│
├── website/                         # Frontend and associated resources
│   ├── static/                      # Static files (e.g., CSS, images, JS)
│   │   └── style.css                # Styling for the frontend
│   │
│   ├── templates/                   # HTML templates for rendering views
│   │   ├── index.html               # Homepage (landing page)
│   │   ├── dashboard.html           # Job input form and dashboard
│   │   ├── result.html              # Display prediction and XAI output
│   │   ├── about.html              # Display about
|       ├── contact.html              # Display contact
│   ├── utils/                       # Utility scripts for various tasks
│   │   └── pdf_parser.py            # Extract text from PDFs for prediction
│   │
│   ├── app.py                       # Main Flask/FastAPI app (backend)
│   └── requirements.txt             # Python dependencies for the app
│
├── backend/                         # Backend logic and models
│   ├── models/                      # Trained models and vectorizers
│   │   ├── model.pkl                # ML model (trained job posting classifier)
│   │   └── vectorizer_rf.pkl           # TF-IDF or CountVectorizer for text vectorization
│       └── rf_fake_job_model.pkl       # Random Forest Model
│   
│  
│
├── README.md                        # Project overview and setup instructions
├── .gitignore                       # Git ignore file to exclude unnecessary files (e.g., data, logs)
└── LICENSE                          # License information for the project (if applicable)

