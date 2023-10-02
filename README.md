[![CI](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml)
## Using Python to Access Database and Perform ETL with SQLite

This repository demonstrates how **access database** and to **Extract**, **Transform**, and **Load** (**ETL**) data using python with **SQLite**.

Below is an overview of the files in this project:

1. **Libraries for Database setup and ETL**
   <br>a. mylib/extract.py_: **extract** dataset from an online source (via URL) and save the dataset as csv.
   <br>b. mylib/transform_load.py_: **read** the csv produced by extract.py, **create database** and fill in values.
   <br>c. mylib/query.py_: **Select** and ouput data.
   <br>d. mylib/update.py_: **Update** values in the created database.
   <br>e. mylib/delete.py_: **Delete** and ouput data.
   

3. **Main functions for CRUD on databse**
   <br>f. _main.py_: execute command-line-like functions from ./mylib for CRUD (Create, Read, Update, Delete) on SQLite database. Specifically, it does the following:
<br>       1. Download a csv file
<br>       2. Build SQLite database and load data from csv to the database
<br>       3. Query the first 10 rows of the database
<br>       4. Update database content (replace '1' with 'one')
<br>       5. Query the first 10 rows of the database
<br>       6. Delete 1 row (the first row with 'id'
<br>       7. Query the first 10 rows of the database

<img width="604" alt="Main Output 1" src="https://github.com/nogibjj/SQLite_YCLiu/assets/46064664/4107594e-3e0e-4a53-8386-a180ff713c09">

   <br>g. _test_main.py_: Run all steps in main.py and test if the output query is correct.
   
4. **Github Actions Setup to test different python versions**
  <br>h. _.github/workflows/cicd.yml_: Development environment was set up using **different versions of python** for later actions. The actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

5. **Other files for development environment settings**
  <br>i. _.devcontainer_: contains devcontainer, setting up the environment for development.
  <br>j. _.gitignore_: specifies file names to ignore.
  <br>k. _requirements.txt_: lists required packages for the project.

6. **Description of the project**
   <br>l. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


