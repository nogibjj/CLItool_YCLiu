[![CI](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml)
## Complex queries using SQL on SQL databases

This repository demonstrates SQL queries that **JOIN** tables and aggregate (**GROUPBY**) under some constraints (**WHERE**). Two toy databases were used to **test queries' functionalities**. 

Below is an overview of the files in this project:

1. **Database setup and Query**
   <br>a. _mylib/create.py_: **read** the csv produced by extract.py, **create database** and fill in values.
   <br>b. _mylib/query.py_: **Select** and ouput data.
   
3. **Main functions for querying on databse**
   <br>c. _main.py_: execute command-line-like functions from ./mylib to create Database and query on SQLite database. Specifically, it does the following:
<br>         1. Build SQLite database Transaction.db.
<br>         2. Create table *Customer*, with the following columns: *cust_id*, *name*, *sex*. Below is the content of the resulted table.

**Customer table**

| cust_id | name | sex |
|---|---|---|
|001| John | Male |
|**_002_**| **_Devin_** | **_Female_** |
|**_003_**| **_Sharon_** | **_Female_** |
|004| Tim | Male | 
|**_005_**| **_Tina_** | **_Female_** |

<br>         2. Build and load SQLite database *Transaction*, with the following columns: *cust_id*,*item*, *amount*. Below is the content of the resulted table.

**TXR table**
| cust_id | item | amount |
|---|---|---|
|001| Hot Dog | 100 |
|001| Hot Dog | 20 |
|**_002_**| Hamburger | `80` |
|**_002_**| Hot Dog | `120` |

<br>         3. Query total sales by female customers (**SUM** of *amount* **GROUPBY** *id* **WHERE** *sex* is *Female*) by descending order (**ORDER BY** *id* **DESC**).

```
#SQL Query

SELECT t1.cust_id, t1.name, t1.sex,
        SUM(t2.amount) AS total_amount 
        FROM Customer t1
        INNER JOIN TXR t2
        ON t1.cust_id = t2.cust_id
        WHERE t1.sex ='Female'
        GROUP BY t1.cust_id
        ORDER BY total_amount DESC
```

**Query Result**

| cust_id | name | sex | amount |
|---|---|---|---|
|003| Sharon | Female | `260` |
|005| Tina | Female | `230` |
|002| Devin | Female | `200` |

   <br>d. _test_main.py_: Run all steps in main.py and test if the output query is correct.
   
5. **Github Actions Setup for continuous integration**
  <br>e. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

6. **Other files for development environment settings**
  <br>f. _.devcontainer_: set up the environment for development.
  <br>g. _.gitignore_: specify file names to ignore.
  <br>h. _requirements.txt_: list required packages for the project.

7. **Description of the project**
   <br>i. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


