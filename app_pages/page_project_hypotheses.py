import streamlit as st

def page_project_hypotheses_body():
    st.markdown(
        """
        * [Hypothesis 1: Higher Overall Quality Leads to Higher Sale Prices](#hypothesis-1-higher-overall-quality-leads-to-higher-sale-prices)
        * [Hypothesis 2: Larger Living Areas Result in Higher Sale Prices](#hypothesis-2-larger-living-areas-result-in-higher-sale-prices)
        * [Hypothesis 3: Newer Houses Have Higher Sale Prices](#hypothesis-3-newer-houses-have-higher-sale-prices)
        """
    )

    st.write("### Hypothesis 1: Higher Overall Quality Leads to Higher Sale Prices")
    st.write("**Hypothesis**: Houses with higher overall quality ratings (`OverallQual`) tend to have higher sale prices.")
    st.write("**Validation**: Perform a correlation analysis between `OverallQual` and `SalePrice`. Create scatter plots and calculate the Pearson and Spearman correlation coefficients to validate the strength and direction of the relationship.")
    
    st.write("### Hypothesis 2: Larger Living Areas Result in Higher Sale Prices")
    st.write("**Hypothesis**: Houses with larger above-ground living areas (`GrLivArea`) tend to have higher sale prices.")
    st.write("**Validation**: Perform a correlation analysis between `GrLivArea` and `SalePrice`. Create scatter plots and calculate the Pearson and Spearman correlation coefficients to validate the strength and direction of the relationship.")
    
    st.write("### Hypothesis 3: Newer Houses Have Higher Sale Prices")
    st.write("**Hypothesis**: Newer houses (houses built more recently) tend to have higher sale prices.")
    st.write("**Validation**: Perform a correlation analysis between `YearBuilt` and `SalePrice`. Create scatter plots and calculate the Pearson and Spearman correlation coefficients to validate the strength and direction of the relationship.")