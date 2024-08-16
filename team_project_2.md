# Team Project Part 2

## Description

Working together in your project team, you'll continue to apply your newly acquired skills and revisit your program from Part 1. Data Science Certificate participants will collaborate to creatively visualize their data. Participants working toward the Machine Learning Software Foundations Certificate will work together to deploy a machine learning model. For example, your team might choose to develop a sentiment analysis model for social media comments in order to enable businesses to gauge public opinion effectively.

At the end of the module, all team members are encouraged to fork the repo onto their profile so that prospective employers can view the project on all of your profiles. 

_Reminder: Please add in the additional file structures found on the README.md._

This project applies skills from the following previous modules:

* Introduction to Building Software (Shell, Git, Python)
* SQL
* Applying Statistical Concepts (Linear regression, classification, and resampling
* Scaling to Production
* Visualization (Data Science Certificate)
* Sampling (Data Science Certificate)
* Algorithm & Data Structures (Machine Learning Software Foundations Certificate)
* Deep Learning (Machine Learning Software Foundations Certificate)

## Learning Outcomes
By the end of the team project, participants will be able to either:
* Create a data visualization as a team
* Create a machine learning model as a team

## Instructions

1. Review the Rules of Engagement you created together and revise it if necessary
2. Using the guiding questions below, discuss what your team would like to create to enhance your existing project.
3. Create a new repository for your project or update the existing repository. Hint: this repo has some features commonly found in industry repos that might help you structure your repo appropriately.
4. Determine what roles the various team members will play on the team, which tasks need to be completed and assigned to which team members, and what your team norms will be with respect to code reviews, approvals and merges. 
5. Each time you work on the project, add a log to the repository's README indicating what was accomplished. 
6. At the end of the week, please record a 3-5 minute video individually that answers the following questions:
    1. What did you learn?
    2. What challenges did you face?
    3. How did you overcome those challenges?
    4. If you had more time to complete your project, what would you add to it?
    5. What strengths do you bring to a team work environment?
7. Have fun! This project is yours. This is the time to create something that prospective employers can consider when reviewing your application for a role. What will your project tell them about you, your skills and your ability to work effectively on a team.
  
## Data Visualization Guiding Questions

* What are the main goals and objectives of our visualization project?
* How can we tailor the visualization to effectively communicate with our audience?
* What type of visualization best suits our data and objectives (e.g., bar chart, scatter plot, heatmap)?
* Are there any specific libraries or frameworks that are well-suited to our project requirements?
* How can we iterate on our design to address feedback and make iterative improvements?
* What best practices can we follow to promote inclusivity and diversity in our visualization design?
* How can we ensure that our visualization accurately represents the underlying data without misleading or misinterpreting information?
* Are there any privacy concerns or sensitive information that need to be addressed in our visualization?

## Machine Learning Model Guiding Questions

* What are the specific objectives and success criteria for our machine learning model?
The primary objective is to develop a robust model that accurately identifies fraudulent transactions within the credit card dataset. Success criteria include:
Accuracy: High overall accuracy in detecting fraudulent transactions.
Precision: High precision to minimize false positives (non-fraudulent transactions incorrectly labeled as fraudulent).
Recall: High recall to ensure most fraudulent transactions are detected.
F1-Score: A balanced F1-score that considers both precision and recall.
AUC-ROC: A high AUC-ROC score to assess the model’s ability to distinguish between fraudulent and non-fraudulent transactions.

* How can we select the most relevant features for training our machine learning model?
We selected features based on domain knowledge, data exploration, and feature importance analysis. By eliminating non-relevant features and refining the remaining ones, we ensured that only the most impactful features were used for training, enhancing the model’s performance.

* Are there any missing values or outliers that need to be addressed through preprocessing?
We found no missing values in our data. However, we identified outliers and skewness in the 'amt' and 'city_pop' columns. To address this, we used StandardScaler and QuantileTransformer in our preprocessing pipeline to manage extreme values and skewed distributions, preserving the predictive power of the data.

* Which machine learning algorithms are suitable for our problem domain?
We used Logistic Regression, Random Forest, and Gradient Boosting. We created four distinct pipelines (A, B, C, and D) with different preprocessing techniques and model configurations to evaluate and compare the performance of these algorithms in detecting fraudulent transactions.

* What techniques can we use to validate and tune the hyperparameters for our models?
We initially used GridSearchCV for exhaustive hyperparameter tuning but switched to RandomizedSearchCV due to high memory usage and computation time. RandomizedSearchCV allowed us to efficiently sample parameter combinations and find near-optimal solutions. We also used cross-validation within the search process to validate each configuration and ensure robust model performance.

* How should we split the dataset into training, validation, and test sets?
We used a standard approach to split the dataset, allocating 70-80% for training and 20-30% for testing. Additionally, we employed cross-validation during hyperparameter tuning to evaluate the model on multiple subsets of the data, ensuring it generalizes well and is not overfitted.

* Are there any ethical implications or biases associated with our machine learning model?
Yes, our model faces ethical implications and biases. The imbalanced is_fraud target variable may lead to high false-negative rates for fraudulent transactions. We also considered data privacy, ensuring that anonymized or hashed credit card numbers do not expose sensitive personal information.

* How can we document our machine learning pipeline and model architecture for future reference?
We documented our machine learning pipeline and model architecture comprehensively in our VS Code notebook. This includes details on preprocessing steps, models used (Logistic Regression, Random Forest, Gradient Boosting), their configurations, cross-validation strategy, and performance results. We pushed the notebook to GitHub, created pull requests, and followed version control practices to track changes and facilitate collaboration. This approach ensures that our work is well-documented, accessible, and maintainable for future reference.

## Requirements

* Each team member must create, review, and merge a pull request 
* Each team member must contribute to the repository’s log 
* Each team member must create a video about their learnings and experience
Shahrzad: https://youtu.be/i7MbVCJOhn4
Stuart: https://drive.google.com/drive/folders/1ZXHnp4O978vnW8NodpjlseO5M_woAj0V?usp=sharing

* Each project's README should describe the project, why the team approached the project the way they did, and should demonstrate thoughtful consideration of the guiding questions above. This is the best way to demonstrate your learning to prospective employers who may view this project on your profile. 

## Resources from Part 1

* [Interactive Git Tutorial](https://learngitbranching.js.org/)
* [Interactive Rebase: Git In Practice - Part 2 - Thinktecture AG](https://www.thinktecture.com/en/tools/git-interactive-rebase/)
* [Git merge conflicts | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts#:~:text=Understanding%20merge%20conflicts,automatically%20determine%20what%20is%20correct.)
