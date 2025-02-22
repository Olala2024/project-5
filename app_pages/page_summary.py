import streamlit as st
import pandas as pd

# Load a sample of the dataset to display
DATASET_DF = pd.read_csv("outputs/datasets/collection/house_prices_records.csv").head(3)

def page_summary_body():
    st.write(
        f"* [Project Summary](#project-summary)\n"
        f"* [Project Terms & Jargons](#project-terms-and-jargons)\n"
        f"* [Project Dataset](#project-dataset)\n"
        f"* [Business Requirements](#business-requirements)"
    )

    st.write("### Project Summary")

    st.write(
        f"The client has inherited properties located in Ames, Iowa, and seeks assistance in maximizing their sales price. Despite having a strong understanding of property prices in her own state and residential area, the client is concerned that her current knowledge may lead to inaccurate appraisals in Ames, Iowa. The factors that make a house desirable and valuable in her area may differ significantly from those in Ames, Iowa. To address this, the client has found a public dataset with house prices for Ames, Iowa, and will provide this data for analysis.\n\n"
        f"* For further information, please visit and **read** the [project documentation](https://github.com/Olala2024/project-5/blob/main/README.md)."
    )
    
    st.info(
        f"**Project Terms & Jargons**\n\n"
        f"* **Sales price** of a house refers to the current market price of a house with certain attributes.\n"
        f"* **Inherited house** is a house that the client has inherited from grandparents.\n")

    st.info(
        f"#### **Project Dataset**\n\n"
        f"**Dataset**: A publicly available dataset sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data) was used for this project.\n\n"
        f"**Dataset Attributes**: The dataset contains various attributes representing housing records from Ames, Iowa, including attributes such as Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built, and their respective sale prices for houses built between 1872 and 2010.\n\n"
        f"**Dataset Observations**: The dataset contains approximately 1.5 thousand observations."
    )

    st.success(
        f"#### **Business Requirements**\n\n"
        f"**Business Requirement 1** - The client wants to analyze how various attributes (e.g., size, location, number of bedrooms) affect the sale price. The client expects data visualizations of the correlated variables against the sale price to provide insights into these relationships.\n\n"
        f"**Business Requirement 2** - The client is interested in predicting the sale price of her four inherited houses and any other house in Ames, Iowa. The goal is to develop a predictive model that can accurately estimate house prices based on the provided dataset."
    )