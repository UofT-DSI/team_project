# Team Project

## Contents

* [Overview](#overview)
* [Learning Outcomes](#learning-outcomes)
* [Getting Started](#getting-started)
    * [Key Contacts](#key-contacts)
    * [Module Delivery & Expectations](#module-delivery--expectations)
    * [Schedule](#schedule)
* [Instructions](#instructions)
    * [Repository Setup](#repository-setup)
    * [Selecting a Business Case and Dataset](#selecting-a-business-case-and-dataset)
    * [Guiding Questions](#guiding-questions)
* [Working as a Team](#working-as-a-team)
* [Submitting Your Project](#submitting-your-project)
    * [Submission & Evaluation](#submission--evaluation)
    * [Project Showcase](#project-showcase)
* [Getting Help](#getting-help)
    * [Troubleshooting & FAQs](#troubleshooting--faqs)
    * [Guidelines for Requesting Help](#guidelines-for-requesting-help)
* [Other Resources](#other-resources)
    * [Git](#git)
    * [Teamwork](#teamwork)
    * [Past Participant Projects](#past-participant-projects)

## Overview

The Team Project will showcase your ability to deliver business value in a real-world context. This project will be a valuable asset in your portfolio, and you should be comfortable presenting it to prospective employers as a demonstration of your skillset.

In your assigned team of ~4-5, you will collaboratively analyze an open-sourced dataset. For example, your team might wish to examine the relationship between the length of movies and the ratings users give them. Or, you may wish to explore the relationship between the size of a dog breed and the associated genetic ailments of that breed. You are encouraged to pick a business case that interests you, is robust and flexible enough to practise your skills, and is well-suited for showcasing business impact. We will provide example datasets that your team can choose from, but the rest is up to you!

The task in front of your team is deliberately open-ended. You will have to make many decisions together, such as:
* How will you make sure all team members contribute to the project?
* How will you make decisions as a team?
* What is the question you're trying to answer through your data analysis?
* What tasks need to be completed to get to your final output?
* How will you present your results in a meaningful way?

At the end of the project, all team members are encouraged to fork the repo onto their profiles so that prospective employers can view your project.

## Learning Outcomes

By the end of this module, participants will be able to:
1. **Apply multiple technical skills in a cohesive project** by integrating concepts from Python, Git, Shell, SQL, Linear Regression, Classification, Resampling, Production, Data Science Stream Content (Sampling and Visualization) or Machine Learning Software Foundation Stream Content (Algorithms, Data Structures, and Deep Learning).
2. **Develop a portfolio-ready project** that demonstrates technical proficiency, problem-solving skills, and the ability to generate meaningful insights from data.
3. **Write high-quality, maintainable code** by practicing structured coding, effective commenting, debugging, and refactoring in a team setting.
4. **Document and present project findings effectively** by maintaining a clear README, summarizing key decisions, and delivering insights in a way that is accessible to both technical and non-technical audiences.
5. **Collaborate effectively in a team environment** by using Git best practices (small commits, branches, pull requests), participating in stand-ups, and maintaining effective communication.

## Getting Started

### Key Contacts
**Questions should first be submitted to the 'help' channel on Slack.**

For other matters, you can also reach to your instructional team:

* Technical Facilitator: 
  * **Phil Van-Lane** (he/him)
  phil.vanlane@mail.utoronto.ca

* Learning Support Staff:

  * **Aditya Kulkarni** (he/him)
  aditya.kulkarni@mail.utoronto.ca
  * **Ernani Fantinatti** (he/him)
  ernanif@fantinatti.com
  * **Farzaneh Hashemi** (she/her)
  fhashemi.ma@gmail.com

### Module Delivery & Expectations

The Team Project includes some content delivery in the live learning sessions, however most of the session time (and additional work periods) will be used to work on your project collaboratively as a team. There will also be a case study presented during the second week, which is a great opportunity to see a real-life example of the type of project you are working on.

Although the project is not due until the end of the second week, it is important to plan out your work and stick to a schedule, so there will be milestones that you are expected to meet. The Technical Facilitator and Learning Support will check in with your team daily, and help guide you throughout the module. Frequent and effective communication with your team is crucial in short projects such as this!

Your project plan will be evaluated at the end of your first week, and your finished project will be evaluated at the end of the second week. The last work period will be the Project Showcase, where you will have the opportunity to present your project to the DSI team and the rest of your cohort. This is the best opportunity to practice demonstrating the value of your work, and we encourage you to include your recording in your portfolios!


### Schedule

|Day 1|Day 2|Day 3|Day 4|Day 5|
|-----|-----|-----|-----|-----|
|Live Learning + Work Period| Live Learning + Work Period | Work Period | Work Period|Work Period|


|Day 6|Day 7|Day 8|Day 9|Day 10|
|-----|-----|-----|-----|-----|
|Review + Work Period | Case Study + Work Period | Work Period | Work Period | Project Showcase |


## Instructions

First of all, have fun! This project is yours to get creative with. This is the time to build something that prospective employers can consider when reviewing your portfolio, so be sure to clearly demonstrate the business value that your project provides. What will your project tell them about you, your skills, and your ability to work effectively on a team?

### Repository Setup

First, ***one*** team member should create a new repository for the project, which the rest of the team will clone. It doesn’t matter who creates the repository, as GitHub tracks everyone’s contributions.

Below is a suggested starting structure, but your team should adapt it as needed. You should structure your project in a way that makes sense for your business case, ensure it is clean, and **remove any unused files and folders**.

```
├── data
├──── processed
├──── raw
├──── sql
├── experiments
├── models
├── reports
├── src
├── README.md
└── .gitignore
```

* **Data:** Contains the raw, processed and final data. For any data living in a database, make sure to export the tables out into the `sql` folder, so it can be used by anyone else.
* **Experiments:** A folder for experiments.
* **Models:** A folder containing trained models or model predictions.
* **Reports:** Generated HTML, PDF etc. of your report.
* **src:** Project source code.
* **README:** This file!
* **.gitignore:** Files to exclude from this folder (e.g., large data files).

### Selecting a Business Case and Dataset

You will be given access to a bank containing carefully selected datasets from many different industries. As a team, you will need to align on an industry and choose a dataset to use. You will also need to decide on your "business case", which describes your project goal. We have provided examples of these as well, but you are encouraged to modify them based on your team's particular interests.

Keep in mind that this may be an interative process! As you explore and develop your project, think about the questions below, and don't be afraid to refine your data or business case as needed to create an impactful project.

### Guiding Questions

* Who is the intended audience for your project?
* What is the question you will answer with your analysis?
* What are the key variables and attributes in your dataset?
* Do you need to clean your data, and if so what is the best strategy?
* How can you explore the relationships between different variables?
* What types of patterns or trends are in your data?
* Are there any specific libraries or frameworks that are well-suited to your project requirements?

In addition, you should be considering the following (depending on your stream):

**Data Science Guiding Questions**

* How can you tailor the visualizations to effectively communicate with your audience?
* What type of visualization best suits your data and objectives (e.g., bar chart, scatter plot, heatmap)?
* How can you iterate on your design to address feedback and make improvements?
* What best practices can you follow to promote inclusivity and diversity in our visualization design?
* How can you ensure that your visualization accurately represents the underlying data without misleading or misinterpreting information?
* Are there any privacy concerns or sensitive information that need to be addressed in your visualization?

**Machine Learning Guiding Questions**

* What are the specific objectives and success criteria for your machine learning model?
* How can you select the most relevant features for training?
* Are there any missing values or outliers that need to be addressed through preprocessing?
* Which machine learning algorithms are suitable for the problem domain?
* What techniques are available to validate and tune the hyperparameters?
* How should the data be split into training, validation, and test sets?
* Are there any ethical implications or biases associated with the machine learning model?
* How can you document the machine learning pipeline and model architecture for future reference?


## Working as a Team

Working in a team provides the benefit of having more people to share the work, but it also creates some challenges. Consistent, effective communication is critical to ensuring that your team works in a constructive and efficient way.

Here are some tips to help your team work as effectively as possible:

* **Define roles and responsibilities.** Make sure everyone knows which tasks are assigned to which team members, and what your team standards will be with respect to code reviews, approvals, and merges. 
* **Establish clear communication protocols** (e.g., set up a dedicated Slack channel, schedule regular check-ins).
* **Keep your README up to date.** Not only is that easier than writing it all at the end of your project, it will help keep you on track and ensure your alignment with your business objective.
* **Document decisions** so you can review and validate why you made the choices you did.
* **Comment your code** so other team members can help out or take over specific tasks as needed.
* **Use software to keep track of tasks** (such as [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)). 


For additional insights on effective teamwork, meetings, and collaboration, check out the additional [Teamwork Resources](#teamwork).


## Submitting Your Project

### Submission & Evaluation

Your team must update [this document](https://docs.google.com/spreadsheets/d/1srZaFCoW4eAaUfqAgH3RIQt1rpx4OJNJh7o3yIuCs3E/edit?usp=sharing) with the links to your project repository and the dataset that you have chosen to analyze. _You will not be submitting a PR to the DSI repository to submit your project_. We will be evaluating your repository directly.

After Week 1, you will be evaluated on your project's README file. By this point, it must include a detailed project proposal. This should include the business motivation for your project, the dataset you have chosen to use, and any risks or unknowns you have identified.

Your final project will be evaluated on the following criteria after Week 2:

1. Each team member must have created a pull request, and reviewed and merged a different pull request.
2. (a) For **Data Science** teams, your project must include a visualization that presents new insights into the chosen dataset.

   (b) For **Machine Learning** teams, your project must include a machine learning model that you have developed and implemented to obtain new insights.

3. In addition to the project proposal from Week 1, each project's README should describe the final outcome of the project, the key business takeaways, and describe your team's approach to working collaboratively. It should also demonstrate thoughtful consideration of the [guiding questions](#guiding-questions).

4. Your project should be ***completely reproducible***. This means that anyone (e.g. the instructional team for marking, or potential employers for evaluating your work) should be able to completely recreate your analysis and results based on the instructions in your repository. This includes any software and data dependencies. You should test this by trying to regenerate your results from scratch.

5. Each team member must record a 3-5 minute video reflecting on your experience. You may each choose where to host your own video, however _it should be public and a link to each team member's video should be included in your project README_. This video is meant to be an asset to your portfolio, and should be available for prospective employers. Your videos should answer the following questions:
    * What did you learn?
    * What challenges did you face?
    * How did you overcome those challenges?
    * If you had more time, what would you add?
    * What strengths do you bring to a team environment?

### Project Showcase

* Each team will have 5 minutes to present your project during the Project Showcase on November 15th.

* This is not a lot of time, so you should not try to describe every step of your project.

* Instead, think of it as an "elevator pitch".

    * Assume that the audience is not an expert in your industry. Provide the required context.
    * Who are your intended stakeholders and why should they care about your project?
    * Explain your dataset in a way that your audience can understand.
    * BRIEFLY describe the tools/technologies that you used.
    * What are the key outcomes and takeaways? What is the business impact of your findings? Highlight one or two key visualizations or metrics.
    * If you had more time, what would your team have explored next?


## Getting Help

### Troubleshooting & FAQs

1. Gather information about your problem
   - Copy and paste your error message
   - Copy and paste the code that caused the error, and the last few commands leading up to the error
   - Write down what you are trying to accomplish with your code. Include both the specific action, and the bigger picture and context
   - (optional) Take a screenshot of your entire workspace

2. Try searching the web for your error message
   - Sometimes, the error has common solutions that can be easy to find!
      - This will be faster than waiting for an answer
   - If none of the solutions apply, consider asking a Generative AI tool
      - Paste your code, the error message, and a description of your overall goals

3. Try asking in your cohort's Slack help channel
   - Since we're all working through the same material, there's a good chance one of your peers has encountered the same error, or has already solved it
   - Try searching in the DSI Certificates Slack help channel for whether a similar query has been posted
   - If the question has not yet been answered, post your question!
      - Describe your the overall goals, the context, and the specific details of what you were trying to accomplish
      - Make sure to **copy and paste** your code, your error message
      - Copying and pasting helps:
         1. Your peers and teaching team quickly try out your code
         2. Others to find your question in the future

### Guidelines for Requesting Help
* [Asking for Help - The Odin Project](https://www.theodinproject.com/lessons/foundations-asking-for-help)
* [How do I ask a good question? - Stack Overflow](https://stackoverflow.com/help/how-to-ask)
* [The XY problem: A question pitfall that won't get useful answers](https://xyproblem.info/)
* [How to create a minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example)


## Other Resources

### Git
* [Interactive Git Tutorial](https://learngitbranching.js.org/)
* [Interactive Rebase: Git In Practice - Part 2 - Thinktecture AG](https://www.thinktecture.com/en/tools/git-interactive-rebase/)
* [Git merge conflicts | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts#:~:text=Understanding%20merge%20conflicts,automatically%20determine%20what%20is%20correct.)


### Teamwork

* [Five Rules of Engagement for Your High-Performing Team - High5 Leadership](https://high5leadership.com/five-rules-of-engagement-for-your-high-performing-team/)
* [Ground Rules for Teams: Definition and Examples | Indeed.com](https://www.indeed.com/career-advice/career-development/ground-rules-for-teams)
* [8 Ground Rules for Great Meetings (hbr.org)](https://hbr.org/2016/06/8-ground-rules-for-great-meetings)
* [16 Ground Rules for Group Work | Facilitator School](https://www.facilitator.school/ground-rules/ground-rules-for-group-work)
* [Chapter 8 Working in Teams | Research Software Engineering with Python (third-bit.com)](https://third-bit.com/py-rse/teams.html#teams-coc)

### Past Participant Projects

* [Bank Marketing Campaign](https://github.com/darshan-kale-dsi/Bank-Marketing-Campaign) (Machine Learning)
* [Customer Purchasing Behaviours](https://github.com/sunshinesharon/Customer-Purchasing-Behaviors) (Data Science)
* [Stroke Prediction](https://github.com/RuiQianSun/team7) (Machine Learning)
* [Car Sales Analysis](https://github.com/emailmealoy/Car-Sales-Trend_DS7) (Data Science)
* [Insights from Bank Marketing](https://github.com/blackpearl/ML_T7_Bank-Marketing) (Machine Learning)