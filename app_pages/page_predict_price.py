import streamlit as st
import pandas as pd
import joblib

def page_predict_price_body():
    st.title("House Price Prediction")
    st.write("Business Requirement 2: The client is interested in predicting the sale price of her four inherited houses and any other house in Ames, Iowa. The goal is to develop a predictive model that can accurately estimate house prices based on the provided dataset.")
    
    # Load the model
    model = joblib.load("outputs/models/house_price_model_v1_top_5.pkl")
    
    # Load inherited houses data
    st.write("### Predict Sale Prices for Inherited Houses")
    if st.button("Load and Predict Inherited Houses"):
        inherited_houses_df = pd.read_csv("outputs/datasets/collection/inherited_houses.csv")
        st.write("Inherited Houses Data:")
        st.write(inherited_houses_df)
        
        # Ensure the inherited houses data has the necessary columns
        required_columns = ['OverallQual', 'GrLivArea', 'YearBuilt', 'TotalBsmtSF', '1stFlrSF']
        if all(column in inherited_houses_df.columns for column in required_columns):
            # Feature engineering
            inherited_houses_df['OverallQual_GrLivArea'] = inherited_houses_df['OverallQual'] * inherited_houses_df['GrLivArea']
            inherited_houses_df['TotalBsmtSF_1stFlrSF'] = inherited_houses_df['TotalBsmtSF'] + inherited_houses_df['1stFlrSF']
            
            # Select the top 5 features
            top_5_features = ['OverallQual_GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'TotalBsmtSF_1stFlrSF']
            predictions = model.predict(inherited_houses_df[top_5_features])
            inherited_houses_df['PredictedSalePrice'] = predictions
            
            # Move the PredictedSalePrice column to the first position
            cols = ['PredictedSalePrice'] + [col for col in inherited_houses_df if col != 'PredictedSalePrice']
            inherited_houses_df = inherited_houses_df[cols]
            
            st.write("Predicted Sale Prices for Inherited Houses:")
            st.write(inherited_houses_df)
        else:
            st.write("Error: Inherited houses data does not contain the required columns.")
                  
    # Widget inputs for prediction
    st.write("### Predict Sale Price for a Single House")
    overall_qual = st.slider("Overall Quality", 1, 10, 5)
    gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=0, value=1500)
    year_built = st.number_input("Year Built", min_value=1800, value=2000)
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, value=1000)
    first_flr_sf = st.number_input("1st Floor Area (sq ft)", min_value=0, value=1000)
    
    # Feature engineering for single house prediction
    overall_qual_gr_liv_area = overall_qual * gr_liv_area
    total_bsmt_sf_first_flr_sf = total_bsmt_sf + first_flr_sf
    
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'OverallQual_GrLivArea': [overall_qual_gr_liv_area],
        'OverallQual': [overall_qual],
        'TotalBsmtSF': [total_bsmt_sf],
        'YearBuilt': [year_built],
        'TotalBsmtSF_1stFlrSF': [total_bsmt_sf_first_flr_sf]
    })
    
    # Run prediction for a single house
    if st.button("Run prediction for single house"):
        prediction = model.predict(input_data)
        st.write(f"Predicted Sale Price: ${prediction[0]:,.2f}")