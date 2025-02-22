import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_project_hypotheses import page_project_hypotheses_body
from app_pages.page_correlation_study import page_correlation_study_body
from app_pages.page_predict_price import page_predict_price_body
from app_pages.page_model_performance import page_model_performance_body

app = MultiPage(app_name="House Price Predictor")

# Load pages scripts
app.add_page("Project Summary", page_summary_body)
app.add_page("Project Hypotheses", page_project_hypotheses_body)
app.add_page("Feature Correlation Study", page_correlation_study_body)
app.add_page("House Price Prediction", page_predict_price_body)
app.add_page("Regression Model Performance Metrics", page_model_performance_body)

app.run()  # Run the app