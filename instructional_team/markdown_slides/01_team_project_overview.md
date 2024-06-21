---
marp: true
theme: dsi-certificates-theme
_class: invert
paginate: true
---

# Team Project
```
$ echo "Data Sciences Institute"
```
---

## Today

1. Team Project Guidelines

2. Developing a Project Plan

3. Git Review: Resolving Merge Conflicts

---

# Team Project Guidelines

---

### Goal

___Develop a program that uses data creatively to solve a problem or provide insights that have a positive business impact.___

---

### Learning Outcomes

1. Resolve merge conflicts.

2. Describe common problems or challenges a team encounters when working collaboratively using Git and GitHub.

3. Create a program to analyze a dataset with contributions from multiple team members.

---

### Key Questions

* How will you select your dataset?

* How will you make sure all team members can contribute to the project?

* How will you make decisions?

* What is the question you're trying to answer through your data analysis?

* What tasks need to be completed to get to your final output?

---

### Requirements

1. Each team member must __create, review, and merge a pull request__.

2. Each team member must __write one PR description__.

3. Each project must __design, implement, and test regression__.

4. Each team must __create a README__ that explains  the project, how the team approached their project, and any relevant details to their team project, including the team's Rules of Engagement. Keep in mind that the repo will be on each team member's profile, so be thoughtful about the details you include here.

5. Each team member must __create a video__ about their learnings and experience.

---

### Submission

* **One** person from each team must fork the [`team_project`](https://github.com/UofT-DSI/team_project) Git repository. Other team members should clone the forked repository.

* The folder structure of your forked repository may be modified to suit your needs.

* Follow the [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md) to submit your team project when it is completed. The branch you merge to the **main** branch of your forked repository (**NOT** to the DSI repository) should be called `team-project-1`.

---

### Refer to Git repository for more details.

---

# Developing a Project Plan

---

### How do we create business value?
* We want to allocate our resources (eg. money, employees) in the way that generates the most value.
    * How do we enable the decision makers?

*Strategic decisions should be based on data!*

![w:700 center](./images/business_data_context.png)

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**A "meta-model of ignorance" that can help us put the unknowns of projects into context.**

0. Zeroth Order Ignorance (0OI): Lack of Ignorance
1. First Order Ignorance (1OI): Lack of Knowledge
2. Second Order Ignorance (2OI): Lack of Awareness
3. Third Order Ignorance (3OI): Lack of Process
4. Fourth Order Ignorance (4OI): Meta Ignorance

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**0. Zeroth Order Ignorance (0OI): Lack of Ignorance**

* You provably know something
* The ability to prove it is necessary

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**1. First Order Ignorance (1OI): Lack of Knowledge**

* You know that you do not know something
* "Acknowledged ignorance"

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**Second Order Ignorance (2OI): Lack of Awareness**

* You do not know that you do not know something
* Metacognition: awareness of what you know and don't know
* This is what we try to eliminate as we work through projects

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**Third Order Ignorance (3OI): Lack of Process**

* You do not know of a suitably effective way to find out that you don’t know that you don’t know something
* This may result in a knowledge trap
* Finding ways to escape from this quickly is critical
* Escaping from this is an important function of software testing: showing areas where you lack knowledge

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**Fourth Order Ignorance (4OI): Meta Ignorance**

* You do not know about the Five Orders of Ignorance
* Fundamental ignorance of ignorance

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**A "meta-model of ignorance" that can help us put the unknowns of projects into context.**

* The goal is to move down the ladder to 0OI.
* 2OI and 3OI is where we should be spending most of our production energy.

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**0. Zeroth Order Ignorance (0OI): Lack of Ignorance**

* You know there is a door.
* You know where the door is.
* You can see the path to the door clearly.

![bg right contain](./images/0OI.jpg)


---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**1. First Order Ignorance (1OI): Lack of Knowledge**

* You know there is a door.
* You do not know the path to the door, but you know you can find the path with a tool that you have (eg. a flashlight).

![bg right contain](./images/1OI.jpg)

---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**Second Order Ignorance (2OI): Lack of Awareness**

* You know there is a door, but you do not know how to get to it or where to start looking.

![bg right contain](./images/2OI.jpg)


---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**Third Order Ignorance (3OI): Lack of Process**

* You know you are in a room, but don't know if there is any way out.

![bg right contain](./images/3OI.jpg)


---

## [The Five Orders of Ignorance](https://www.5oi.org/the-five-orders-of-ignorance)

**Fourth Order Ignorance (4OI): Meta Ignorance**

* Complete and utter darkness.

![bg right contain](./images/4OI.jpg)

---

# Developing a project plan

## 1. Understand the business context

What are companies or organizations in your industry trying to achieve? What is your organization trying to achieve?

---

## 1. Understand the business context

* What are companies or organizations in your industry trying to achieve?
* What is your organization trying to achieve?
* Align your goals with company values.

~~**Bad Example:** We work in finance. Our company wants to make more money so we should spent half of our working days coming up with a side hustle that our company can implement.~~

**Good Example:** We work in finance. Our team is not client facing and does not impact revenue directly, but our department manages overhead costs for the company and we can help try to reduce those costs.

---

## 2. Identify an opportunity

* Where can you add business value?
* How do you enable informed decision making?

---

## 2. Identify an opportunity

* Where can you add business value?
* How do you enable informed decision making?

~~**Bad Example:** We see that employees in the Sales Department only work from the office about half the time. Therefore we should cut their office space in half and leave every other team's space as is.~~

**Good Example:** We hypthesize that office space is under-utilized, or not utilized as efficiently as it good be. We want to explore the idea of reducing overall office space while maintaining the same level of productivity and comfort for employees.

---

## 3. Scope your analysis

* What data do you need?
* Do you have the resources to acquire additional data?

---

## 3. Scope your analysis

* What data do you need?
* Do you have the resources to acquire additional data?

~~**Bad Example:** We should interview everyone to get their opinions on how office space is utilized.~~

**Good Example:** We want to explore the data on:

1. How often employees work from the office vs. work from home.
2. Whether teams tend to all work in the office on the same days.
3. The cost to acquire new office spaces vs. modifying existing ones.
4. How our rate of working remotely compares with other companies and other industries.

---

## 4. Develop your solution

* Integrate your data.
* Illustrate your key findings in an easily interpretable way.

---

## 4. Develop your solution

* Integrate your data.
* Illustrate your key findings in an easily interpretable way.

~~**Bad Example:** We will compile the list of people who have offices, mark down whether or not they have shown up at the office for every day in the last month, and create a spreadsheet with those data.~~

**Good Example:** We can compare the available office space to the space being used under a variety of conditions. This could include breaking the data down by building, floor, team, day of the week, month, and weather. We can investigate the capacity of different office layouts, and analyze the tradeoffs involved.

---

## 5. Present results and recommendations (more on this tomorrow!)

* Know your audience.
* Clearly articulate the takeaways.
* Highlight the value added.

---

## 5. Present results and recommendations (more on this tomorrow!)

* Know your audience.
* Clearly articulate the takeaways.
* Highlight the value added.

~~**Bad Example:** We inform our department leaders that managers should tell employees specific days on which they need to come into the office.~~

**Good Example:** You find that since office usage varies, it would be more efficient to have less office space overall but design it in a more flexible way. Each department could have designated office space and manage the allocation for individual teams.

---

## Check: are your insights actionable?

Insights are far more impactful if they are ***actionable***.

* What recommendations are you making that are *within the jurisdiction* of your audience?
* Eg. We are presenting this to our departments heads; do they have the power to implement and enforce what we are recommending?

---

## Check: how robust is your analysis?

How can you quantify the value that you are providing?

* Eg. what % of operating costs do you expect to save in a year?
* How are you justifying your metrics?

---

## Check: what are the risks/caveats/unknowns?

Are you missing data that would provide more insight?

* Eg. Are there policies that have changed at the team level?

Is there a risk of false correlation?

* Eg. What other factors may be influencing office usage during the period of study?
    * Vacation season?

How do we monitor whether these trends continue?

* Eg. How do we continue to track office space usage in a meaningful way with flexible seating?

___

# Summary: Developing a project plan

1. Understand the business context.
2. Identify an opportunity.
3. Scope your analysis.
4. Develop your solution.
5. Present results and recommendations.

### To keep in mind:

* Are your insights *actionable?*
* How robust is your analysis? *Quantify!*
* What are the *risks/caveats/unknowns?*

---

## `Git Review: Resolving Merge Conflicts`