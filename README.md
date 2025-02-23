# HousePricePredictor

HousePricePredictor is a Machine Learning project designed to help real estate investors, homeowners, and property managers predict the sales prices of houses based on various attributes. By leveraging advanced data analysis and machine learning techniques, HousePricePredictor provides accurate and reliable price predictions, enabling users to make informed decisions about property investments and sales. ![Sample Page](/src/images/image.png)

HousePricePredictor helps real estate investors and homeowners accurately appraise property values using a data-driven approach. It offers comprehensive data visualizations, price predictions based on various house attributes, and highlights key features influencing house prices. 
HousePricePredictor is user-friendly and accessible, catering to real estate investors, homeowners, and property managers.

The dashboard for [HousePricePredictor is hosted on Heroku](https://housepricepredictor-8c23b0f8520c.herokuapp.com/).

# Table of Contents

1. [Dataset Content](#1-dataset-content)
2. [Project Terms and Jargon](#project-terms-and-jargon)
3. [Business Requirements](#business-requirements)
    - [Epics](#epics)
    - [User Stories](#user-stories)
4. [Hypotheses and Validation](#hypotheses-and-validation)
5. [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
6. [ML Business Case](#ml-business-case)
7. [Dashboard Design](#dashboard-design)
8. [Testing](#testing)
9. [Unfixed Bugs](#unfixed-bugs)
10. [Deployment](#deployment)
11. [Technologies Used](#technologies-used)
12. [Forking and Cloning](#forking-and-cloning)
13. [Credits](#credits)
14. [Acknowledgements](#acknowledgements)

## 1. Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

The table below indicates the variables, their description and units of measurement. We note that some variables are numerical while others are categorical.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Project Terms and Jargon

* **Sale price** of a house refers to the current market price of a house with certain attributes.

* **Inherited house** is a house that the client has inherited from grandparents.

## Business Requirements

The client has inherited properties located in Ames, Iowa, and seeks assistance in maximizing their sales price. Despite having a strong understanding of property prices in her own state and residential area, the client is concerned that her current knowledge may lead to inaccurate appraisals in Ames, Iowa. 

The factors that make a house desirable and valuable in her area may differ significantly from those in Ames, Iowa. To address this, the client has found a public dataset with house prices for Ames, Iowa, and will provide this data for analysis.

1. **Correlation Analysis**:
   - The client is interested in discovering how various house attributes correlate with the sale price. The client expects data visualizations of the correlated variables against the sale price to provide insights into these relationships.

2. **Price Prediction**:
   - The client is interested in predicting the sale price of her four inherited houses and any other house in Ames, Iowa. The goal is to develop a predictive model that can accurately estimate house prices based on the provided dataset.

### Epics

- Information gathering and data collection.
- Data visualization, cleaning, and preparation.
- Model training, optimization, and validation.
- Dashboard planning, designing, and development.
- Dashboard deployment and release.

### User Stories

- US1: As a user, I want to know the source and content of the data used in training the model so that I can be confident about the quality of the trained model.
- US2: As a user, I want to know the project hypotheses and how they were validated so that I get a deeper understanding of the mechanisms that determine sale price.
- US3: As a client, I want to know which attributes of a house are most correlated with its sale price so that I can base my prediction on the right set of features. (Business Requirement Covered: BR1)
- US4: As a user, I want to see relevant plots so that I can visualize the relationships between sale price and other features. (Business Requirement Covered: BR1)
- US5: As a user, I want to have access to the data cleaning and preparation pipeline so that I can quickly predict sale price without reinventing the wheel.
- US6: As a technical user, I want to learn about the ML steps that were used to arrive at the sale price prediction so that I can understand the model employed. (Business Requirement Covered: BR2)
- US7: As a technical user, I want to know the model performance so that I can ensure that the predictions are reliable. (Business Requirement Covered: BR2)
- US8: As a client, I want to have reliable predictions of the sale price of houses I have inherited so that I can sell them at the maximum total price possible. (Business Requirement Covered: BR2)
- US9: As a client, I want to get a dashboard so that I can display the results of the prediction on a standalone app.
- US10: As a user, I want to have interactive input widgets so that I can provide real-time house data and predict the sale price. (Business Requirement Covered: BR2)

## Hypotheses and Validation

#### Hypothesis 1: Higher Overall Quality Leads to Higher Sale Prices
- **Hypothesis**: Houses with higher overall quality ratings (`OverallQual`) tend to have higher sale prices.
- **Validation**: Perform a correlation analysis between `OverallQual` and `SalePrice`. Create scatter plots and calculate the Pearson and Spearman correlation coefficients to validate the strength and direction of the relationship.



#### Hypothesis 2: Larger Living Areas Result in Higher Sale Prices
- **Hypothesis**: Houses with larger above-ground living areas (`GrLivArea`) tend to have higher sale prices.
- **Validation**: Perform a correlation analysis between `GrLivArea` and `SalePrice`. Create scatter plots and calculate the Pearson and Spearman correlation coefficients to validate the strength and direction of the relationship.

#### Hypothesis 3: Newer Houses Have Higher Sale Prices
- **Hypothesis**: Newer houses (houses built more recently) tend to have higher sale prices.
- **Validation**: Perform a correlation analysis between `YearBuilt` and `SalePrice`. Create scatter plots and calculate the Pearson and Spearman correlation coefficients to validate the strength and direction of the relationship.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

#### Business Requirement 1 (BR1): Data Visualization and Correlation Study

To understand how various house attributes correlate with the sale price, we will perform the following tasks:

1. **Inspect Sale Price Distribution**:
   - Plot a histogram of the sale prices to understand their distribution.

2. **Correlation Analysis**:
   - Compute both Pearson and Spearman correlation coefficients to study the magnitudes and directions of correlation between the attributes and sale price of the houses.

3. **Visualize Key Variables**:
   - Plot scatter plots of key variables against the sale price to illustrate the nature of their relationships.

The [correlation study notebook](https://github.com/Olala2024/project-5/blob/main/jupyter_notebooks/03-CorrelationStudy.ipynb) will handle this business requirement by providing insights into the relationships between house attributes and sale prices through data visualizations and correlation analysis.

#### Business Requirement 2 (BR2): Regression Analysis

To predict the sale price of houses, we will use regression analysis, as the target variable (sale price) is continuous. The following tasks will be performed:

1. **Feature Importance**:
   - Identify the most important variables that contribute significantly to the sale price. This will help the client maximize the price by leveraging these factors.

2. **Regression Model**:
   - Develop a regression model to predict the sale price of houses based on the provided dataset.

3. **Model Evaluation**:
   - Evaluate the performance of the regression model using appropriate metrics (e.g., Mean Squared Error, R² Score) to ensure its reliability.

[The Modeling and Evaluation notebook](https://github.com/Olala2024/project-5/blob/main/jupyter_notebooks/05-ModelingandEvaluation.ipynb) will handle this business requirement by developing and evaluating a predictive model for house prices.

## ML Business Case

### Regression Model

We want a machine learning model to predict the sale price of houses based on various attributes (e.g., size, location, number of bedrooms) using previously gathered housing data from Ames, Iowa. The target variable, 'SalePrice', is continuous and represents the sale price of the houses.

We will consider a regression model, a supervised model with a continuous output that matches the target variable.

**Model Success Metrics**:
- The model will be considered successful if it achieves at least 70% R² score on the test set.

**Model Failure Criteria**:
- The model will be considered a failure if it fails to achieve a 70% R² score on the test set.

**Model Output**:
- The model output is defined as the predicted sale price of a house based on its attributes.

**Training Data**:
- The training data to fit the model comes from a public dataset provided by the client, sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).

**Dataset Details**:
- The dataset contains approximately 1.5 thousand observations and various attributes representing housing records from Ames, Iowa, including attributes such as Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built, and their respective sale prices for houses built between 1872 and 2010.

**Target Variable**:
- SalePrice

**Features**:
- All other attributes in the dataset.

## Dashboard Design

### Page 1: Project Summary
* **Section 1 - Summary**
    * Introduction to the project
    * Description of the dataset, including its source
    * Link to the README file
* **Section 2 - Business Requirements**
    * Description of business requirements

### Page 2: Project Hypotheses
* Outline the three project hypotheses
* Present validation of each hypothesis

### Page 3: Feature Correlation Study
* State Business Requirement 1
* Overview of the dataset - display the first 5 rows of data and describe the dataset shape
* Display correlation results
* Display distributions of correlated features against the target variable (SalePrice)
* Conclusions

### Page 4: House Price Prediction
* State Business Requirement 2
* Widget inputs for prediction (e.g., size, location, number of bedrooms)
* "Run prediction" button to run inputted data through the ML model and output a predicted sale price

### Page 5: Regression Model Performance Metrics
* Summary of model performance and metrics
* Model pipeline, features used to train the model, and how they were selected
* Documentation of model performance on train and test sets

## Testing

To ensure that the project meets the business requirements and user stories, I conducted manually the following tests:

| **User Story** | **Test** | **Expected Result** |
|--------------|---------|------------------|
| **US1: Data Source Documentation** | Verify that the data source and content are documented and accessible. | The documentation should include information about the data source, dataset content, and any preprocessing steps applied. |
| **US2: Project Hypotheses and Validation** | Review the project hypotheses and their validation steps. | The documentation should clearly state the project hypotheses and provide evidence of their validation through data analysis and visualizations. |
| **US3: Attribute Correlation** | Verify that the dashboard displays the attributes most correlated with the sale price. | The dashboard should show a list of attributes with their correlation coefficients and relevant visualizations (e.g., scatter plots). |
| **US4: Relevant Plots** | Verify that the dashboard displays relevant plots showing the relationships between sale price and other features. | The dashboard should include visualizations such as histograms, scatter plots, and correlation matrices. |
| **US5: Data Cleaning and Preparation Pipeline** | Review the data cleaning and preparation pipeline to ensure it is accessible and functional. | The pipeline should be well-documented and allow users to preprocess data efficiently. |
| **US6: ML Steps Documentation** | Review the documentation and code to ensure that the ML steps are clearly explained. | The documentation should include a detailed explanation of the ML pipeline, feature engineering, model training, and evaluation steps. |
| **US7: Model Performance** | Evaluate the model performance using metrics such as Mean Squared Error (MSE) and R² Score. | The model should achieve acceptable performance metrics, indicating reliable predictions. |
| **US8: Reliable Price Predictions** | Input house attributes into the model and verify the predicted sale price. | The model should provide a reliable and accurate sale price prediction based on the input attributes. |
| **US9: Dashboard Functionality** | Verify that the dashboard is accessible and displays the prediction results. | The dashboard should be user-friendly and display the prediction results clearly. |
| **US10: Interactive Input Widgets** | Test the interactive input widgets on the dashboard to ensure they work correctly. | Users should be able to input house attributes in real-time and receive a sale price prediction. |

#### Conclusion

All tests were conducted according to the user stories provided. The application performed well in all areas except for the description of the ML model, which needs improvement. The issue is documented in the unfixed bugs section. Overall, the project meets the business requirements and provides a valuable tool for real estate investors, homeowners, and property managers.

## Unfixed Bugs

* One of the main bugs in the project is related to the regression model performance metrics page. The page is intended to display the performance metrics of the trained regression model, including Mean Squared Error (MSE) and R² Score for both the training and testing sets. However, due to issues with fitting the feature engineering pipeline and transforming the data, the page does not function as expected. 

* The primary challenge was ensuring that the feature engineering pipeline was correctly fitted before transforming the data. Despite multiple attempts to resolve this issue, the page still encounters errors, such as the `NotFittedError`, which indicates that the pipeline instance is not fitted yet.

* The bug remains unfixed due to time constraints and the complexity of the issue. While the rest of the application functions correctly, this specific page requires further debugging and testing to ensure it works as intended.

* Future work will involve revisiting this page to properly fit the feature engineering pipeline and accurately display the regression model performance metrics.

## Deployment

### Heroku

* The App live link is: <https://housepricepredictor-8c23b0f8520c.herokuapp.com/>
The project was deployed to Heroku using the following steps:

1. Within your working directory, ensure there is a setup.sh file containing the following:
```
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
2. Within your working directory, ensure there is a runtime.txt file containing a  version of Python.

3. Within your working directory, ensure there is a Procfile file containing the following:
```
web: sh setup.sh && streamlit run app.py
```
4. Ensure your requirements.txt file contains all the packages necessary to run the streamlit dashboard.
5. Update your .gitignore and .slugignore files with any files/directories that you do not want uploading to GitHub or are unnecessary for deployment.
6. Log in to Heroku and create an App
7. At the Deploy tab, select GitHub as the deployment method.
8. Select your repository name and click Search. Once it is found, click Connect.
9. Select the branch you want to deploy, then click Deploy Branch.
10. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
11. If the slug size is too large then add large files not required for the app to the .slugignore file or optimize dependencies removing from requirements.txt unessential for your application.

## Technologies Used

The technologies used throughout the development are listed below:

### Languages

* [Python](https://www.python.org/)

### Python Packages

* [Pandas](https://pandas.pydata.org/docs/index.html) - Open source library for data manipulation and analysis.
* [Numpy](https://numpy.org/doc/stable/index.html) - Adds support for large, multi-dimensional arrays and matrices, and high-level mathematical functions.
* [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated and interactive visualisations.
* [Seaborn](https://seaborn.pydata.org/) - Another data visualisation library for drawing attractive and informative statistical graphics.
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Library with multiple transformers to engineer and select features for machine learning models.
* [scikit-learn](https://scikit-learn.org/stable/) - Open source machine learning library that features various algorithms for training a ML model.
* [SciPy](https://scipy.org/) - Library used for scientific computing and technical computing.
* [XGBoost](https://xgboost.readthedocs.io/en/stable/) - Optimised distributed gradient boosting library.
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Provides tools for lightweight pipelining, e.g. caching output values.

### Other Technologies

* [Git](https://git-scm.com/) - For version control
* [GitHub](https://github.com/) - Code repository and GitHub projects was used as a Kanban board for Agile development
* [Heroku](https://heroku.com) - For application deployment
* [VSCode](https://code.visualstudio.com/) - IDE used for development

## Forking and Cloning
If you wish to fork or clone this repository, please follow the instructions below:

### Forking
1. In the top right of the main repository page, click the **Fork** button.
2. Under **Owner**, select the desired owner from the dropdown menu.
3. **OPTIONAL:** Change the default name of the repository in order to distinguish it.
4. **OPTIONAL:** In the **Description** field, enter a description for the forked repository.
5. Ensure the 'Copy the main branch only' checkbox is selected.
6. Click the **Create fork** button.

### Cloning
1. On the main repository page, click the **Code** button.
2. Copy the HTTPS URL from the resulting dropdown menu.
3. In your IDE terminal, navigate to the directory you want the cloned repository to be created.
4. In your IDE terminal, type ```git clone``` and paste the copied URL.
5. Hit Enter to create the cloned repository.

## Credits

* The PPS heatmap function code was sourced from the Code Institute's "Exploratory Data Analysis Tools" module.
* The multi-page class was taken from the Code Institute "Data Analysis & Machine Learning Toolkit" streamlit lessons.
* The icon in the dashboard was taken from [Discuss Streamlit](https://discuss.streamlit.io/t/page-icon/36475).
* Special thanks to the [Stack Overflow](https://stackoverflow.com/) community for providing solutions to various coding challenges encountered during the project.
* The structure of this README was inspired by the [CVD Predictor](https://github.com/jfpaliga/CVD-predictor/tree/main) repository.

## Acknowledgements 

* I would like to express my gratitude to my mentor, Mo Shami, for his invaluable support and guidance.

