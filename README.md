# Analysis of variables in dataset using Linear Regression techniques

## Project Overview

This project aims to analyze the variables that predict the subscription
and purchase amount of the customers in the dataset.

The dataset selected by the team is from this [dataset link](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset?resource=download).


We chose the **Customer Shopping Preferences Dataset** because this
dataset encompasses various factors such as age, gender, purchase
history, preferred payment methods, and shopping frequencies, which are
fundamental for businesses aiming to tailor their strategies to customer
needs. Analyzing this data allowed us to gain practical experience in
applying data analysis and machine learning techniques to real-world
scenarios.

By utilizing various statistical techniques and regression analysis, we
tried to understand the relationships between customer demographics,
purchasing behaviors, and the methods of payment.

## Project Team
- George Zuo
- Panpan Wang
- Pramod Sharma
- Jingyi Lu

## Objectives

The team brainstormed on various parameters before enlisting below
target objectives which were divided amongst team members in an
exclusive manner so that we all can test the whole skillset to clean and
evaluate the dataset using linear regression

### PART A -- George Zuo
Predict if a customer will subscribe services based on their attributes and purchasing behavior to find connections between service subscription and customer characteristics

### PART B -- Panpan Wang 
Build and evaluate a predictive model for purchase amounts based on age, product category and discount applied factors

### PART C -- Pramod Sharma 
Evaluate if the variables (Age, previous purchases, frequency of purchases) influence the purchase amounts in the retail dataset

### PART D -- Jingyi Lu 
Predict the category based on various input features namely Size, Gender, Age Group, Frequency of Purchases, Promo Code Used, Rating Group, Purchase Amount (USD), Subscription Status, Shipping Type

## Dataset Description

The dataset includes the following columns:

-   Customer ID: Unique identifier for each customer.

-   Age: Age of the customer.

-   Gender: Gender of the customer.

-   Item Purchased: Item that was purchased.

-   Category: Category of the purchased item.

-   Purchase Amount (USD): The amount spent on the purchase.

-   Location: Customer\'s location.

-   Size: Size of the purchased item.

-   Color: Color of the purchased item.

-   Season: Season during which the purchase was made.

-   Review Rating: Customer\'s review rating for the item.

-   Subscription Status: Whether the customer has a subscription.

-   Shipping Type: Type of shipping chosen.

-   Discount Applied: Whether a discount was applied.

-   Promo Code Used: Whether a promo code was used.

-   Previous Purchases: Number of previous purchases by the customer.

-   Payment Method: Method of payment used.

-   Frequency of Purchases: Frequency of customer\'s purchases.

## Analysis Details

### Part A -- George Zuo

-   Verify if dataset has null values or other invalid data

-   Classify features to numeric and categorical group and encode categorical features

-   Use Logistic Regression to build a model

-   Split a dataset into training and testing sets using a random state

-   Fit model using train data and predict with test data

-   Check results by the Confusion Matrix and Accuracy Rate

### PART B -- Panpan Wang

Data Preprocessing:

-   Categorical Encoding: Transform the categorical variables (category and discount applied).

-   ColumnTransformer: Combining the one-hot encoding and passing through numerical features (age).

Model Building:

-   Pipeline Creation: Using pipeline to integrate the preprocessing step and the linear regression model.

-   Model Training: Fitting the pipeline to the data.

Model Evaluation:

-   Metrics: Calculating Mean Squared Error (MSE) and R² score to evaluate model performance.

-   Visualization: Creating a scatter plot to compare actual vs. predicted purchase amounts.

### Part C -- Pramod Sharma

-   Performed the following activities- preprocess data, run statistical tests, and perform regression analysis.

-   Specifically, I converted categorical data into numerical codes and clean the dataset by checking for and handling missing values. I also used statistical tests like Chi-square, T-tests, and ANOVA to analyze relationships and differences in our data.

-   As a part of the Regression Analysis I performed Ordinary Least Squares (OLS) regression to predict purchase amounts using independent variables of Age, Previous Purchases, Frequency of Purchases, and Payment Method.

### Part D -- Jingyi Lu

-   Clean data: load dataset/Convert categorical variables to numeric values/Bin the \'Age\' and \'Rating\' into groups

-   Define the X and Y

-   Split the data into training and testing sets

-   Train the Logistic Regression model

-   Evaluate model- get accuracy score, classification report and confusion matrix

## Key Findings

### Part A -- George Zuo

-   Accuracy: 83% indicates a high overall accuracy of the model.

-   Precision: For subscribers (1) is 63%, indicating that about 63% of the samples predicted as subscribers are actually subscribers.

-   Recall: For subscribers (1) is 94%, indicating that the model correctly identified about 94% of the actual subscribers.

-   F1-Score: 76% combines precision and recall, providing a balanced measure.

### Part B -- Panpan Wang

-   The model has a high Mean Squared Error: 559.9984322042955.

-   The model has a very low R² Score: 0.001525402943547749.

-   The scatter plot of actual vs. predicted purchase amounts indicates
    that the model\'s predictions are not well-aligned with the actual
    values.

### Part C -- Pramod Sharma

-   Chi-square Test: No significant association was found between Payment Method and Frequency of Purchases.

-   T-tests: No significant differences in purchase amounts were found between various payment methods.

-   ANOVA: Neither Payment Method nor Frequency of Purchases were significant predictors of purchase amounts.

-   Regression Analysis: All independent variables had p-values greater than 0.05, indicating that none were significant predictors of purchase amounts.

Detailed Regression Analysis Results:

-   Mean Squared Error (MSE): The MSE value of 559.12 is very high indicating the fit is not good.

-   R-squared (R²) Score: The R-squared score of -0.0034. Not good interpretation.

-   Coefficients and p-values: The coefficients for each variable (Age, Previous Purchases, Frequency of Purchases, Payment Method) indicate the estimated change in the purchase amount for a one-unit change in each predictor variable, holding other variables onstant. None of the coefficients are statistically significant at conventional levels (typically p \< 0.05).

-   F-statistic and Prob (F-statistic): The F-statistic with a value of 0.4399 and a probability (Prob (F-statistic)) of 0.780 indicates that the model as a whole is not statistically significant.

### Part D -- Jingyi Lu

-   The accuracy of the logistic regression model on the test set is
    approximately 44.79%.

-   The classification report and confusion matrix showed the model has
    high recall for Category 1 but fails to predict Categories 2, 3, and
    4.

## Conclusion

### Part A -- George Zuo

The model performs well with an accuracy of 83%. We may use it as a tool
for predicting customer subscription behavior, and then develop
corresponding marketing strategies for different customer groups.

### Part B -- Panpan Wang

The result concludes that the linear regression model does not
accurately capture the relationship between the independent variables
(Age, Category, Discount Applied) and the dependent variable (Purchase
Amount (USD)). The high MSE and low R² score suggest that the model\'s
performance is poor and it fails to explain the variance in the purchase
amounts. This indicates that the chosen features and model may not be
appropriate for predicting purchase amounts.

### Part C -- Pramod Sharma

The regression analysis suggests that the variables Age, Previous
Purchases, Frequency of Purchases, and Payment Method do not
significantly predict Purchase Amounts in this dataset.

### Part D -- Jingyi Lu

The logistic regression in this case is in poor performance. Even though
the overall accuracy is approximately 44.79%, it only performed very
well in predicting Category 1, not Categories 2, 3 and 4.
<BR>
<BR>

## Video Links

[Part A -- George Zuo](https://youtu.be/YUF0OaLFe4M)

[Part B -- Panpan Wang](https://youtu.be/u7TTnxpvGUg?si=g7aD6970IZF0C9-2)

[Part C -- Pramod Sharma](https://youtu.be/oYyeUJzEspg)

Part D -- Jingyi Lu
<BR>
<BR>

## Project Folder Structure
```markdown
|-- code (jupyter notebook files)
|-- data
|---- processed
|---- raw (dateset csv files)
|---- sql
|-- reports
|-- src
|-- README.md
|-- .gitignore
```

## Project Approach and Rules of Engagement

Our team approached the project with a structured and collaborative
strategy, focusing on leveraging each member\'s unique skills and
interests. Here\'s a breakdown of how we tackled the project and our
team\'s Rules of Engagement:

**Team Approach:**

1.  **Project Selection and Objectives Setting**

    -   We chose the Customer Shopping Preferences Dataset from Kaggle
    because it offered a comprehensive set of variables, such as age,
    gender, purchase history, preferred payment methods, and shopping
    frequencies. This dataset provided a real-world scenario for us to
    apply data analysis and machine learning techniques.

    -   We set clear objectives for the project. These were divided into
    four parts (A, B, C, and D) to cover different aspects of the
    analysis and ensure that each team member had a specific focus area.

2.  **Division of Tasks**

    -   **Part A:** Predict if a customer will subscribe to services based
    on their attributes and purchasing behavior. This part aimed to find
    connections between service subscription and customer
    characteristics.

    -   **Part B:** Build and evaluate a predictive model for purchase
    amounts based on factors such as age, product category, and discount
    applied. This part focused on understanding the impact of these
    factors on purchase amounts.

    -   **Part C:** Evaluate if variables like Age, Previous Purchases, and
    Frequency of Purchases influence purchase amounts. This part aimed
    to identify significant predictors of purchase amounts.

    -   **Part D:** Predict the product category based on various input
    features, including Size, Gender, Age Group, Frequency of Purchases,
    Promo Code Used, Rating Group, Purchase Amount (USD), Subscription
    Status, and Shipping Type. This part aimed to classify product
    categories using these variables.

3.  **Data Preprocessing**

    -   Each member was responsible for cleaning and preprocessing their
    respective data segments. This included handling missing values,
    encoding categorical variables, and normalizing data where
    necessary.

4.  **Statistical Analysis and Model Building**

    -   We applied various statistical techniques such as Chi-square tests,
    T-tests, ANOVA, and regression analysis to understand relationships
    and predict outcomes.

    -   Each member built and evaluated predictive models specific to their
    part, ensuring that we tested the entire skillset required for the
    project.

5.  **Collaboration and Communication:**

    -   We held regular team meetings to discuss progress, share insights,
    and address any challenges. This ensured that everyone was on the
    same page and could provide input and support where needed.

## Rules of Engagement

1.  Clear Communication

2.  Defined Roles and Responsibilities

3.  Respect and Support

4.  Regular Updates and Feedback

    -   We provided regular updates on our progress on Slack and gave
    constructive feedback to help each other.

5.  Time Management

    -   We set deadlines for each phase of the project to ensure timely
    submission.

6.  We reviewed each other\'s work to ensure high-quality results and
    consistency across the different parts of the project.

By dividing the project into manageable parts and working
collaboratively with clear guidelines, we were able to effectively
analyze the dataset and achieve our project objectives.
