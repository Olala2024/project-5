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

### Project Terms and Jargon

* **Sale price** of a house refers to the current market price of a house with certain attributes.

* **Inherited house** is a house that the client has inherited from grandparents.

## Business Requirements

The client has inherited properties located in Ames, Iowa, and seeks assistance in maximizing their sales price. Despite having a strong understanding of property prices in her own state and residential area, the client is concerned that her current knowledge may lead to inaccurate appraisals in Ames, Iowa. 

The factors that make a house desirable and valuable in her area may differ significantly from those in Ames, Iowa. To address this, the client has found a public dataset with house prices for Ames, Iowa, and will provide this data for analysis.

1. **Correlation Analysis**:
   - The client is interested in discovering how various house attributes correlate with the sale price. The client expects data visualizations of the correlated variables against the sale price to provide insights into these relationships.

2. **Price Prediction**:
   - The client is interested in predicting the sale price of her four inherited houses and any other house in Ames, Iowa. The goal is to develop a predictive model that can accurately estimate house prices based on the provided dataset.

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

## Unfixed Bugs

* One of the main bugs in the project is related to the regression model performance metrics page. The page is intended to display the performance metrics of the trained regression model, including Mean Squared Error (MSE) and R² Score for both the training and testing sets. However, due to issues with fitting the feature engineering pipeline and transforming the data, the page does not function as expected. 

* The primary challenge was ensuring that the feature engineering pipeline was correctly fitted before transforming the data. Despite multiple attempts to resolve this issue, the page still encounters errors, such as the `NotFittedError`, which indicates that the pipeline instance is not fitted yet.

* The bug remains unfixed due to time constraints and the complexity of the issue. While the rest of the application functions correctly, this specific page requires further debugging and testing to ensure it works as intended.

* Future work will involve revisiting this page to properly fit the feature engineering pipeline and accurately display the regression model performance metrics.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

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

