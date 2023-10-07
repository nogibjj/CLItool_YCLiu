[![CI](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml)
## Complex queries using SQL on SQL databases

This repository demonstrates SQL queries that **JOIN** tables and aggregate (**GROUPBY**) under some constraints (**WHERE**). Two toy databases were used to **test queries' functionalities**. 

Below is an overview of the files in this project:

1. **Database setup and Query**
   <br>a. _mylib/create.py_: **read** the csv produced by extract.py, **create database** and fill in values.
   <br>b. _mylib/query.py_: **Select** and ouput data.
   
3. **Main functions for querying on databse**
   <br>c. _main.py_: execute command-line-like functions from ./mylib to create Database and query on SQLite database. Specifically, it does the following:
<br>         1. Build and load SQLite database *Customer*, with the following columns: *id*, *name*, *sex*
<br>         2. Build and load SQLite database *Transaction*, with the following columns: *id*,*item*, *amount*
<br>         3. Query total sales by item (**SUM** of *amount* **GROUPBY** *item*) by descending order (**ORDER BY** *item* **DESC**).
<br>         4. Query total sales by female customers (**SUM** of *amount* **GROUPBY** *id* **WHERE** *sex* is *Female*) by descending order (**ORDER BY** *id* **DESC**).
   <br>d. _test_main.py_: Run all steps in main.py and test if the output query is correct.
   
5. **Github Actions Setup for continuous integration**
  <br>e. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

6. **Other files for development environment settings**
  <br>f. _.devcontainer_: set up the environment for development.
  <br>g. _.gitignore_: specify file names to ignore.
  <br>h. _requirements.txt_: list required packages for the project.

7. **Description of the project**
   <br>i. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


