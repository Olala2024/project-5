import streamlit as st

def page_model_performance_body():
    st.title("Regression Model Performance Metrics")
        
    # Regression Model Description
    st.write("""
   
    **Model Success Metrics**:
    - The model will be considered successful if it achieves at least 70% R² score on the test set.

    **Model Failure Criteria**:
    - The model will be considered a failure if it fails to achieve a 70% R² score on the test set.

    **Model Output**:
    - The model output is defined as the predicted sale price of a house based on its attributes.
    """)
    
    # Display Mean Squared Error (MSE)
    st.header("Mean Squared Error (MSE)")
    st.write("Training Set MSE: 411,496,843.69")
    st.write("Testing Set MSE: 2,299,035,504.57")
    
    # Display R² Score
    st.header("R² Score")
    st.write("Training Set R² Score: 0.9310")
    st.write("Testing Set R² Score: 0.7003")
    
    