# **Team Project**
## Consumer Behavior and Shopping Habits

### Group#24 
#### Team Members 
- Shiraz Latif: 
- Jessilynn Kim: https://drive.google.com/file/d/154oUYqRxrjb2NYRciiltaPbO3xmOLw3g/view?usp=sharing 
- Mykhailo Vitvinov:
- Olena Bolokhonova: https://drive.google.com/file/d/1v07EtJ6vsUtRywuMMTopht9VIy6_oRRa/view?usp=drivesdk

## Team's approach 
### Data Selection
After determining the sectors we had chosen for the team project (Retail/Commerce & Finance), we collectively explored various datasets in Retail/Commerce field in Kaggle and decided on Consumer Behavior and Shopping Habits dataset.

### Analysis Focus
Each team member reviewed Consumer Behavior and Shopping Habits dataset separately by answering questions part of Team Project 1 Instruction to better understand the data and to set objective of the analysis. We formulated possible variables/relationships/hypothesis and updated excel tracker. 

### Roles and Responsibilities 
Taking everyone's strength, background and circumstances into consideration, everyone contributed to the group project to ensure successful completion. 
Shiraz setup overall framework for the project and reviewed codes as he has the most technical background. Olena dove into data and documentations of work to jumpstart the project.  Mykhailo continued the data analysis to round out the possibilities of meaningful data relationships. Jessilynn completed pre-analysis of the dataset and completed README file for the group with everyone's input. With everyone's input, we contributed as a group to provide insights and recommendations for the project. Additionally, we've leverage Rules of Engagement we've setup for the team to ensure successful completion of this project. 

### Data Analysis 
#### Description
This project aims to analyze consumer behavior and shopping habits using a wide range of variables such as age, gender, purchase amount, location, product category, and more. The primary objective is to explore the relationships between these variables to uncover meaningful insights that can inform business strategies on how to drive total purchase amount.

#### Purpose
The purpose of this project is to leverage statistical analysis and machine learning techniques to understand the factors influencing customer purchase behavior. By examining how different variables, such as age and discount application, impact purchase amounts, we aim to provide data-driven recommendations for improving marketing strategies, optimizing product offerings, and enhancing overall customer satisfaction that will result in increase in total purchase amount. Specifically, the project focuses on the following goals:
    1.	Identify Key Drivers of Purchase Amounts:
        o	Determine which demographic and transactional factors significantly influence the total and average purchase amounts.
    2.	Segment Customers Effectively:
        o	Segment customers based on their purchasing behavior and demographics to tailor marketing campaigns and product recommendations.
    3.	Evaluate Discount Effectiveness:
        o	Analyze the impact of discounts on customer spending to optimize promotional strategies and improve revenue generation.
    4.  Predict subscription status based on wide range of variables included in the dataset.     
    5.	Provide Actionable Insights:
        o	Generate insights that can help businesses understand their customers better, leading to improved customer retention and increased sales.
By achieving these goals, the project aims to contribute to the development of more effective business strategies that are rooted in a deep understanding of customer behavior and preferences.


#### Intended Audience for Data Analysis:

•	Business Analysts: To gain insights into how consumer behaviors are modelled and leveraged 
•	Marketing Teams: To tailor campaigns and promotions based on customer segments and preferences and to increase subscription 
•	Product Managers: To understand product performance and customer preferences that can lead to increased total purchases
•	Executive Leadership: To make data-driven decisions for business growth and customer satisfaction.

#### Patterns and Trends in the Data:

1.	Seasonal Trends:
    o	Analyze how purchase amounts vary across different seasons.
2.	Demographic Insights:
    o	Identify purchasing patterns based on age, gender, and location.
3.	Discount and Promotion Impact:
    o	Assess how discounts and promotional codes influence purchase amounts and frequency.
4.	Customer Loyalty:
    o	Examine the relationship between previous purchases and current spending to identify loyal customers.
 
#### Key Insights and Recommendations:
##### Key Insights
Initial observations of dataset concluded that there were no variances in average purchase per transaction and review ratings by gender. When we looked at age, we also saw that age had no influence on total purchase amount. Additionally, we didn't find statistically significant difference between transactions with and without discounts nor previous purchases and higher average purchase amount. As a result, we rejected all hypotheses due to lack of statistical significance supported by regression analyses. 

We've pivoted our focus to Classification model. We wanted to predict customer's subscription status based on customer's shopping habit. With accuracy of 83%, we concluded that customer shopping habits are good predictor of customer's subscription status. 

##### Recommendations
Leverage customer shopping habits to increase subscriptions. Typically, customers with subscriptions purchased items with discount applied and used promo code. Even though we didn't find statistical significance between discount with average purchase amounts, this may be due to overall reduction in price for each item customers purchased and impacted the total purchase value being lower than items purchased with regular prices. 

As economic conditions continue to impact customer shopping habits and customers are showing price sensitivity, we recommend targeting customers who do not current have subscription and focus on discounts that will be appealing to all customers. 


##### Key Variables and Attributes in the Dataset:
1.	Customer ID: Unique identifier for each customer.
2.	Age: Age of the customer.
3.	Gender: Gender of the customer.
4.	Item Purchased: Specific product purchased by the customer.
5.	Category: Broad classification of the purchased item (e.g., clothing, electronics).
6.	Purchase Amount (USD): Monetary value of the transaction.
7.	Location: Geographical location where the purchase was made.
8.	Size: Size specification of the purchased item (if applicable).
9.	Color: Color of the purchased item.
10.	Season: Seasonal relevance of the purchased item (e.g., spring, summer).
11.	Review Rating: Customer's satisfaction rating for the purchased item.
12.	Subscription Status: Whether the customer has a subscription service.
13.	Payment Method: Mode of payment used by the customer.
14.	Shipping Type: Method used to deliver the purchased item.
15.	Discount Applied: Indicates if any discounts were applied to the purchase.
16.	Promo Code Used: Notes if a promotional code was used during the transaction.
17.	Previous Purchases: Information on the number or frequency of prior purchases by the customer.
18.	Preferred Payment Method: Customer's preferred mode of payment.
19.	Frequency of Purchases: How often the customer makes purchases.

##### Exploring Relationships Between Different Variables:
1.	Statistical Analysis:
    o	Use correlation analysis to identify relationships between numerical variables.
    o	Conduct hypothesis testing (e.g., t-tests, ANOVA) to compare means across different groups.
2.	Regression Analysis:
    o	Perform linear regression to quantify the effect of independent variables (e.g., age, discount applied) on the dependent variable (purchase amount).
    o	Use logistic regression for binary outcomes (e.g., subscription status).
3.	Data Visualization:
    o	Create scatter plots, bar charts, and histograms to visualize relationships and distributions.
    o	Use heatmaps to visualize correlation matrices.
4.	Segmentation:
    o	Cluster analysis (e.g., k-means clustering) to segment customers based on purchasing behavior and demographics.


##### Specific Libraries or Frameworks Well-Suited to the Project Requirements:
1.	Pandas: For data manipulation and analysis.
2.	NumPy: For numerical computations.
3.	Matplotlib and Seaborn: For data visualization.
4.	SciPy: For statistical analysis and hypothesis testing.
5.	Statsmodels: For regression analysis and statistical modeling.
6.	Scikit-learn: For machine learning algorithms and clustering analysis.
7.	Jupyter Notebook: For interactive data analysis and visualization.


## Rules of Engagement 

### Engagement Channel:
1. Zoom Breakout Room
2. Whatsapp Group
3. Slacks
4. Github
5. Emails
6. Google Meets

### Communication:
• Leveraging Whatsapp group for main communication
• Any delays in joining meeting, completion of task, or availabilities for meeting times are shared 

### Meeting Schedule:
1. Post live session breakout room 
    • Check in around 7:15 for about 15 mins
    • Check in around 9:00 for about 15 mins
2. Friday
    • During work period 
    • Evening around 6-7 pm 
3. Saturday -TBD

### Progress Tracking
Shared Excel Tracker
    • Documenting tasks and progress
    • Avoid possible duplication with visibility for everyone

### Conflict Resolution 
1. Voting
2. Respecting other's opinions
3. Listening
4. Actively communicating during meetings
5. Avoid assumptions and ask questions where clarity is required 


