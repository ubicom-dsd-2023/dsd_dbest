# Week 3

## What has been done:

### Bill (Database Architect):

#### Done
Write down what was done during the week.

#### Not done, why?
Write down what was not done during the week and why (difficulties).


### Brioche (Database Engineer):

#### Done
- finished writing Requirement Analysis, containing modifying most of the data flow and added several user cases.
- learned to use docker
- discussed with algorithm team to determine the duty we should do on data cleansing
- design a draft of E-R diagram (hand-writing version)

#### Not done, why?
- still cannot confirm the data type of each schema, since there is not clue in other team's RA to find out the data type
- didn't have enough cooperations with Bill to design the model, since I thought he was in his holiday, there is also my subjective problem.


### Carlos (Architecture Tester):

#### Done
- Learned more about PostgreSQL
- Learned more about Docker
- Tried to pull the database into my machine using docker

#### Not done, why?
- Unsuccessfull to pull the database into my machine, and I´m trying to fix the problems.


### Maxwell (Infrastructure Tester):

#### Done
- Learned to use Docker
- Learned some database testing methods online
- Tried and successfully pulled the database into my machine using Docker
- Helped Brioche finish Requirement Analysis

#### Not done, why?
- Haven't decided on a testing strategy that we'll use

### Still (Database Developers):

#### Done
-  This week I have learned how to use docker 
- I have created the production and test database in the postgres container
- I have registered on the dockerhub
- **we have solved the problem that the image pushed to the dockerhub is empty. Now we could push the image to the dockerhub successfully. ** 

#### Not done, why?
- We haven't accomplish the "readme.md" about how to create the database by using dockerhub. We will accomplish it as soon as possible.



### Watson  (Database Developers):

#### Done
I have learned how to use docker.\
I have created the production and test database in the postgres container.\
We have Submit the image to dockerhub

#### Not done, why?
We are writing the readme.We will finish it in these two days.


## Next goals:

- We need to improve communication and sharing among the team members.
- Another thing I ask of you is: 
  - to give my feedback on my working method as a team leader. I really need to have your feedback in order to improve.
  - To propose changes in the work method in order to make it more to your liking and to make our work easier. 
- Every time you complete a job, come to github and update the status of your job, don't leave it for the last day. That way, we all know where the team's work is.

I need you to talk among yourselves because your mission depends on it.

### Bill (Database Architect):

- [ ] This week I want the E-R model and the database requirements to be finalized. 
- [ ] You should discuss with Brioche the possible ways we can do our part of the job and decide the path to follow.

* Ask for feedback from the other teams.

### Brioche (Database Engineer):

- [ ] This week I want the E-R model and the database requirements to be finalized. 
- [ ] You should discuss with Bill the possible ways we can do our part of the job and decide the path to follow.

* Ask for feedback from the other teams.


### Still and Watson (Database Developers):

- [ ] During this week, you should continue to improve the database with new needs that come up. You should create one database for production and one for testing. 
- [ ] Improve the documentation so that it becomes easier to follow.
- [ ] You should also start creating database requests and documenting them. For example: 
    - Searching for a particular user
    - Searching for a particular user's password
    - Changing a certain field (name, password, etc) for a certain user
    - How to select the entire history of a particular user.
    - What are the last n (number) records
    - Which records for a given user as of the xpto date.
    - What is the last record
    - How many users (user being tested) are in the database
    - and more things that you remember and think are important

For this task, I need you to interact with Testers. You should publish documentation and a version of the database and the testers should be able to run the database on their own computer using only your documentation.

### Carlos (Architecture Tester) and Maxwell (Infrastructure Tester):

- [ ] This week you should support Bill and Brioche's tasks, be proactive and ask them what they need. You should also validate the documentation they produce.
- [ ] You should evaluate and give feedback regarding the documentation and the databases as quickly and accurately as possible. 

Your feedback is important for completing the tasks.
In the case of the programmers' task, you should follow the instructions to the letter, if you have any questions, you should point them out and report them so that they can improve.

- [ ] When analyzing the database architecture, you should look for errors or if anything is missing. They should report it as soon as possible.

- [ ] It is critical that they look at how they are going to test the database. All requirements must be validated.


If you have any questions or if you find any flaws, please report them. 

Thank you for your work and have a good week. 🚀
