# Week 3

## What has been done:

### Bill (Database Architect):

#### Done
Write down what was done during the week.

#### Not done, why?
Write down what was not done during the week and why (difficulties).


### Brioche (Database Engineer):

#### Done
Write down what was done during the week.

#### Not done, why?
Write down what was not done during the week and why (difficulties).


### Carlos (Architecture Tester):

#### Done
Write down what was done during the week.

#### Not done, why?
Write down what was not done during the week and why (difficulties).


### Maxwell (Infrastructure Tester):

#### Done
Write down what was done during the week.

#### Not done, why?
Write down what was not done during the week and why (difficulties).


### Still (Database Developers):

#### Done
-  This week I have learned how to use docker 
- I have created the production and test database in the postgres container
- I have registered on the dockerhub

#### Not done, why?
- Now I can't commit my DB container to the dockerhub.

  > my method is :
  >
  > 1.  use  "docker commit" to commit the container to the image
  > 2. login the dockerhub
  > 3. push the image

  It can push to the dockerhub successfully. But I find it's an empty image. The databases I created  have lost.

- I can't  understand why the database lost when I commit the container to a image

- I searched on the net but it only has the solution to MySQL about this problem.

- I spend a lot of time trying to address this problem. But I failed. (crying) 


### Watson  (Database Developers):

#### Done
I have learned how to use docker.
I have created the production and test database in the postgres container


#### Not done, why?
I had the same problem as Still.I find that when I commit the container to image, there is no data in the image. 
I think the reason is that the image of postgres saves the database in a file which will not be committed when you commit the container to a image. 
There may be some way to solve this problem. But why we need use the docker to creat database? Do we often need to migrate databases?


## Next goals:

### Bill (Database Architect):

- [ ] task

### Brioche (Database Engineer):

- [ ] task

### Carlos (Architecture Tester):

- [ ] task

### Maxwell (Infrastructure Tester):

- [ ] task

### Still and Watson (Database Developers):

- [ ] task
