import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page_correlation_study_body():
    st.title("Feature Correlation Study")
    
    # State Business Requirement 1
    st.write("### Business Requirement 1")
    st.write("The client is interested in discovering how various house attributes correlate with the sale price. The client expects data visualizations of the correlated variables against the sale price to provide insights into these relationships.")
    
    # Load the dataset
    df = pd.read_csv("outputs/datasets/processed/house_prices_records_train_processed.csv")
    
    # Overview of the dataset
    st.write("### Overview of the Dataset")
    st.write(df.head())
    st.write(f"Dataset shape: {df.shape}")
    
    # Create a DataFrame to compare the correlation values
    pearson_corr_matrix = df.corr(method='pearson')
    spearman_corr_matrix = df.corr(method='spearman')
    top_features = list(set(pearson_corr_matrix['SalePrice'].head(10).index).union(set(spearman_corr_matrix['SalePrice'].head(10).index)))
    # Remove 'SalePrice' from the list of top features
    if 'SalePrice' in top_features:
        top_features.remove('SalePrice')
    comparison_df = pd.DataFrame({
        'Pearson': pearson_corr_matrix['SalePrice'][top_features],
        'Spearman': spearman_corr_matrix['SalePrice'][top_features]
    })
    
    # Sort the DataFrame by Pearson correlation in ascending order
    comparison_df = comparison_df.sort_values(by='Pearson', ascending=False)
    
    st.write("### Comparison of Top Features Correlated with SalePrice")
    st.write(comparison_df)
    
    # Plot the comparison
    st.write("### Comparison Plot of Top Features Correlated with SalePrice")
    plt.figure(figsize=(14, 8))
    comparison_df.plot(kind='bar', figsize=(14, 8))
    plt.title('Top Features Correlated with SalePrice')
    plt.xlabel('Features')
    plt.ylabel('Correlation Coefficient')
    plt.xticks(rotation=45)
    plt.legend(title='Correlation Method')
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(plt)
    
    st.write("The bar plot above shows the top features that are most correlated with the sale price using both Pearson and Spearman correlation methods. These features have the highest correlation coefficients with the sale price, indicating a strong relationship.")
    
    # Display distributions of correlated features against the target variable (SalePrice)
    st.write("### Distributions of Correlated Features Against SalePrice")
    key_features = ['OverallQual', 'GrLivArea', 'YearBuilt']
    for feature in key_features:
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[feature], y=df['SalePrice'], ax=ax)
        ax.set_title(f'{feature} vs SalePrice')
        st.pyplot(fig)
        st.write(f"The scatter plot above shows the relationship between {feature} and SalePrice. We can observe that as {feature} increases, the SalePrice tends to increase as well, indicating a positive correlation.")
    
    # Conclusions
    st.write("### Conclusions")
    st.write("The correlation analysis and visualizations provide insights into how various house attributes correlate with the sale price. These insights can help the client make informed decisions about property investments and pricing strategies.")
    st.write("The heatmap and bar plot highlight the top features that have the strongest correlations with the sale price. The scatter plots further illustrate the relationships between these key features and the sale price, showing positive correlations.")