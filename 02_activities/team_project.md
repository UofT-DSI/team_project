# Team Project

## Description

In your assigned team of 4-5, you will collaboratively create a program to analyze data from an open-sourced dataset. 

For example, your team might wish to examine the relationship between the length of a movie and the ratings users give the movie on a popular website. Or you may wish to explore the relationship between the size of a dog breed and the associated genetic ailments of that breed. Teams are encouraged to pick a business case that interests you, is robust enough that you have flexibility to practice your skills, and that is well-suited for showcasing business impact.

The task in front of your team is deliberately open-ended. Your team will have to make decisions together:
* How will you make sure all team members can contribute to the project?
* How will you make decisions?
* What is the question you're trying to answer through your data analysis?
* What tasks need to be completed to get to your final output?

At the end of the project, all team members are encouraged to fork the repo onto their profile so that prospective employers can view the project.

This project should incorporate skills taught and used in the following modules:

* Introduction to Building Software (Git, Shell & Python)
* SQL
* Linear Regression, Classification, and Resampling
* Scaling to Production

AND

> * Visualization (Data Science Certificate)
> * Sampling (Data Science Certificate)

OR

> * Algorithm & Data Structures (Machine Learning Software Foundations Certificate)
> * Deep Learning (Machine Learning Software Foundations Certificate)

---

## Learning Outcomes

### Part 1 Learning Outcomes
By the end of **Part 1**, participants will be able to:
* Work through common problems or challenges a team encounters when collaborating using Git and GitHub, including merge conflicts.
* Understand your business case and dataset.
* Perform investigative analysis on your dataset with contributions from multiple team members.

### Part 2 Learning Outcomes
By the end of **Part 2**, participants will be able to:
* Create a data visualization or a machine learning model as a team.
* Clearly document and present the results of their analysis.
* Reflect on their learning and collaboration process through a recorded video.

---

## Instructions

1. You will be given access to a dataset bank. As a team, choose one of our carefully selected datasets (more info on this later) and explore it, keeping the questions listed below in mind.

2. A team member should create a new repository for the project, which the rest of the team can clone (see the [Project Folder Structure](#project-folder-structure) for a folder structure template to use as a starting point). It doesn’t matter who creates the repository, as GitHub tracks everyone’s contributions fairly.

3. Determine what roles the various team members will play on the team, which tasks need to be completed and assigned to which team members, and what your team standards will be with respect to code reviews, approvals, and merges. 

4. Have fun! This project is yours. This is the time to create something that prospective employers can consider when reviewing your application for a role, so be sure to clearly demonstrate the business value that your project could provide. What will your project tell them about you, your skills, and your ability to work effectively on a team?

Additionally, there are resources listed at the bottom of this page to help you understand Git conflicts and ways to work effectively as a team. You should review these to help set standards for your team processes.

---

## Potential Questions to Discuss When Reviewing Your Dataset

* What are the key variables and attributes in your dataset?
* How can we explore the relationships between different variables?
* Are there any patterns or trends in the data that we can identify?
* Who is the intended audience for our data analysis?
* What is the question our analysis is trying to answer?
* Are there any specific libraries or frameworks that are well-suited to our project requirements?
* How can we iterate on our design to address feedback and make iterative improvements?
* What best practices can we follow to promote inclusivity and diversity in our visualization design?
* How can we ensure that our visualization accurately represents the underlying data without misleading or misinterpreting information?
* Are there any privacy concerns or sensitive information that need to be addressed in our visualization?
* What are the specific objectives and success criteria for our machine learning model?
* How can we select the most relevant features for training our machine learning model?
* Are there any missing values or outliers that need to be addressed through preprocessing?
* Which machine learning algorithms are suitable for our problem domain?
* What techniques can we use to validate and tune the hyperparameters for our models?
* How should we split the dataset into training, validation, and test sets?
* Are there any ethical implications or biases associated with our machine learning model?
* How can we document our machine learning pipeline and model architecture for future reference?

## Requirements

* Thoroughly understand your data and the business case for your analysis. What will the impact of your results be?
* Clean your data. Be confident in the decisions you have made while doing so (e.g. default handling of NULL values).
* Test out regression analyses (for Part 1) or machine learning models/data visualizations (for Part 2). It may take several tries before you are satisfied with your results and understand how you can provide the most insight.
* Make sure your code is well-commented and decisions are documented.
* Keep your README up to date. Not only is that easier than writing it all at the end of your project, it will help keep you on track and ensure your alignment with your business objective.
* Each team member must create, review, and merge a pull request.
* Record a 3-5 minute video (at the end of Part 2) reflecting on your experience. Answer the following questions:
  * What did you learn?
  * What challenges did you face?
  * How did you overcome those challenges?
  * If you had more time, what would you add?
  * What strengths do you bring to a team environment?
  
---
## Project Folder Structure

Each team is responsible for creating their own Git repository for the Team Project. The following is a good starting point for the folder structure, however the structure is ultimately up to each team. You should structure your project in a way that makes sense for your business case, ensure it is clean, and **remove any unused folders**.

```markdown
|-- data
|---- processed
|---- raw
|---- sql
|-- experiments
|-- models
|-- reports
|-- src
|-- README.md
|-- .gitignore
```

* **Data:** Contains the raw, processed and final data. For any data living in a database, make sure to export the tables out into the `sql` folder, so it can be used by anyone else.
* **Experiments:** A folder for experiments
* **Models:** A folder containing trained models or model predictions
* **Reports:** Generated HTML, PDF etc. of your report
* **src:** Project source code
* README: This file!
* .gitignore: Files to exclude from this folder, specified by the Technical Facilitator

---

## Schedule

### Part 1 Schedule

|Day 1|Day 2|Day 3|Day 4|Day 5|
|-----|-----|-----|-----|-----|
|Live Learning + Work Period | Work Period | Case Study + Work Period|Work Period|Work Period|

### Part 2 Schedule

|Day 6|Day 7|Day 8|Day 9|Day 10|
|-----|-----|-----|-----|-----|
|Review + Work Period | Work Period | Case Study + Work Period | Work Period | Presentation + Video Submission|

---

## Resources

### Git

* [Interactive Git Tutorial](https://learngitbranching.js.org/)
* [Interactive Rebase: Git In Practice - Part 2 - Thinktecture AG](https://www.thinktecture.com/en/tools/git-interactive-rebase/)
* [Git merge conflicts | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts#:~:text=Understanding%20merge%20conflicts,automatically%20determine%20what%20is%20correct.)

### Working as a Team

* [Five Rules of Engagement for Your High-Performing Team - High5 Leadership](https://high5leadership.com/five-rules-of-engagement-for-your-high-performing-team/)
* [Ground Rules for Teams: Definition and Examples | Indeed.com](https://www.indeed.com/career-advice/career-development/ground-rules-for-teams)
* [8 Ground Rules for Great Meetings (hbr.org)](https://hbr.org/2016/06/8-ground-rules-for-great-meetings)
* [16 Ground Rules for Group Work | Facilitator School](https://www.facilitator.school/ground-rules/ground-rules-for-group-work)
* [Chapter 8 Working in Teams | Research Software Engineering with Python (third-bit.com)](https://third-bit.com/py-rse/teams.html#teams-coc)

### Example Projects

* [TTC Transit Delay Project](https://github.com/JasonYao3/TTC_transit_delay_proj)
* [Mortgage Risk Assessment Project](https://github.com/movcha/team_project)
* [Mexican Government Report Text Analysis](https://github.com/PhantomInsights/mexican-government-report)