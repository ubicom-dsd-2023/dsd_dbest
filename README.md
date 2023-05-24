
<div align="center">
    <img width="280px" src=".github/logo.png " style=" border-radius: 1rem; border: 2px solid ;"/>
</div>

# Database Team

## Organization

### Team Leader

- __Name__: Eduardo Queirós (Eduardo)
- __Github__: [code36u4r60](https://github.com/code36u4r60)

### Database Architect

- __Name__: Pedro Ferreira (Bill)
- __Github__: [pedrof98](https://github.com/pedrof98)

A database architect is a professional who designs and plans the structure of databases used by software applications and systems. They work with software engineers to determine the database requirements, select the appropriate database management systems, and ensure that the database design meets the business and technical requirements. Database architects also design the database security features and ensure that the database is scalable and efficient.

### Database Engineer

- __Name__: Kangjie Liu (Brioche)
- __Github__: [briocheKJ](https://github.com/briocheKJ)

Database engineer is a professional who creates, maintains, and optimizes databases for software applications and systems. They ensure that databases are secure, scalable, and meet the needs of the application or system. They work with other members of the development team to ensure that the database integrates seamlessly with the software system.

### Tester (Architecture Tester)

- __Name__: Carlos Sampaio (Carlos)
- __Github__: [CarlosSampaio23](https://github.com/CarlosSampaio23)

Responsible for validating the software architecture of the database and it's implementation

### Tester (Infrastructure Tester)

- __Name__: Wei Zhoujun (Maxwell)
- __Github__: []()

A Database Infrastructure Tester tests the hardware, network, and storage systems supporting the database to optimize its performance, availability, and scalability.

### Database Developers

- __Name__: Zhenhe Li (Still)
- __Github__: []()

- __Name__: Shiyu Wang (Watson)  
- __Github__: []()

A database developer is a professional who designs, implements, and maintains databases used by software applications and systems.



## document about DB's docker image 

**2023.4.19**  update the database  see **version2.0** below

**2023.5.11**  update the database  see **version3.0** below

2023.5.23  update the database  see **version4.0** below

### version 1.0

#### environments

we run the commands on the Linux terminal.

packages should be installed:

- postgresql
- docker

#### download the image

- run this command directly

```shell
docker pull sstillzh/pgsql
```

then we will get the image.

use

``` shell
docker images
```

to examine the download image

![image-20230405145356933](https://img-blog.csdnimg.cn/3d7edf01b4194759a2aaba78baf2106c.png)

#### run the container

- use "docker run" command to run the container

```shell
docker run -it --name postgres4 -e POSTGRES_PASSWORD='123456' -e ALLOW_IP_RANGE=0.0.0.0/0  -p 55333:5432 -d sstillzh/pgsql
```

- -it: interact with the terminal

- -name: the name of the container

- -e POSTGRES_PASSWORD='123456': set the database-user's password

- -p: the port mapping of host system and docker system.(When we want to remotely connect the database，we use the "55333"port of the host )



- use 

``` shell
docker ps
```

to examine the running container

![](https://img-blog.csdnimg.cn/fdfe8b6eac154a3791d4d5d7d06b13ae.png)







 

#### enter the container and examine the database

##### enter the container

- use

```shell
docker exec -it postgres4 bash
```

​				to enter the container "postgres4"

![image-20230405150911893](https://img-blog.csdnimg.cn/0f7452a55b524825a80acfb58f4d0d4e.png)



##### examine the database



- change the role from root to postgres (because only the "postgres" has the privilege to access the database)

  ![image-20230405151223838](https://img-blog.csdnimg.cn/e0f916fa317f400d93dda7b3b028614a.png)

- use 

  ```shell
  psql
  ```

  to enter the postgresql

  ![image-20230405151351751](https://img-blog.csdnimg.cn/c82457382adb4ef5956bf465b7cc07b9.png)

- our database

  - We now have two databases:
    1. production  :  save the data from server
    2. test : tester use the data to test
  - we haven't design the E-R model of data, so now there is only two relation tables in each database: 
    1. SENSOR: data from sensor
    2. USER : user's information
  - We will  improve our databases in the future

- common commands of psql

  

  - ```shel
    \l
    ```

    list all existing databases

    ![image-20230405151458073](https://img-blog.csdnimg.cn/a4462803d5954c4ebb96e335ba63503a.png)

  - ```shell
    \c dbname
    ```

    go into a database

    ![image-20230405152308037](https://img-blog.csdnimg.cn/9460af05ab3b4155af234d4501f525f7.png)

    

  - ```shell
    \dt
    ```

    examine all the tables of this database

    ![image-20230405152353367](https://img-blog.csdnimg.cn/ab3ecb47987f4cbeb79a9f492daf48b8.png)

    

  - ```shell
    \d "tablename"
    ```

    examine the structure of specified table

    ![image-20230405152647578](https://img-blog.csdnimg.cn/b54f724f17b240c082d960db71800de1.png)

    

  - query

    use the SQL to query

    ex:

    ```shell
    SELECT * from "SENSOR";
    ```

    

    ![image-20230405153023912](https://img-blog.csdnimg.cn/2735eea180ab452490886b4ef0a4fcc9.png)

 ### version 2.0
  - we update the table-structure of database. Use

```shell
docker pull sstillzh/pgsql:2.0
```

- then we get the new image. Check it.



- the rest thing is just like version1.0
- please notice that the new image's name is **sstillzh/pgsql:2.0**



- please check the structure of our relation tables and see if there exists the mistake.



- I use the **beekeeper**(recommended by Eduardo )to manage our database. Here is a presentation of our relation tables.

​		

- the tables of "production" database("test" database is the same)

![iF9h4P.png](https://i.328888.xyz/2023/04/20/iF9h4P.png)

- the structure of "User" table

![iF9MBV.png](https://i.328888.xyz/2023/04/20/iF9MBV.png)

- the structure of “Frame” table

![iFJzbw.png](https://i.328888.xyz/2023/04/20/iFJzbw.png)

![iFJeiz.png](https://i.328888.xyz/2023/04/20/iFJeiz.png)

- the structure of "MotionRecord" table

![iFKyQc.png](https://i.328888.xyz/2023/04/20/iFKyQc.png)

![iFKAlA.png](https://i.328888.xyz/2023/04/20/iFKAlA.png)

- the structure of "Device" table

![iFKtnV.png](https://i.328888.xyz/2023/04/20/iFKtnV.png)

![iFKWRd.png](https://i.328888.xyz/2023/04/20/iFKWRd.png)

### version 3.0

  - we update the table-structure of database. Use

```shell
docker pull sstillzh/pgsql:3.0
```

- then we get the new image. Check it
- we change the structure of "User" table to satisfy the Android APP team's needs. We delete the "age"  attribute.
- We have insert some training-data of Algorithm team to the "Frame" table.

![iqpnGp.png](https://i.328888.xyz/2023/05/11/iqpnGp.png)

### version 4.0

- we update the table-structure of database. Use

```shell
docker pull sstillzh/pgsql:4.0
```

then we get new image. Check it.

- We add new table "log" to satisfy the web-team's needs.

[![oJJCE0.png](https://www.helloimg.com/images/2023/05/24/oJJCE0.png)](https://www.helloimg.com/image/oJJCE0)

- We add a attribute "user_type" to the table "User"

[![oJJGOm.png](https://www.helloimg.com/images/2023/05/24/oJJGOm.png)](https://www.helloimg.com/image/oJJGOm)
