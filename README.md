## Using Python to Access Database and Perform ETL with SQLite

This repository demonstrates how **access database** and to **Extract**, **Transform**, and **Load** (**ETL**) data using python with **SQLite**.

Below is an overview of the files in this project:

1. **Libraries for Database setup and ETL**
   <br>a. /mylib/extract.py_: **extract** dataset from an online source (via URL) and save the dataset as csv.
   <br>b. /mylib/transform_load.py_: **read** the csv produced by extract.py, **create database** and fill in values.
   <br>c. /mylib/query.py_: **Select** data and display.
   <img width="454" alt="Screenshot 2023-10-01 at 10 28 32 PM" src="https://github.com/nogibjj/SQLite_YCLiu/assets/46064664/8e79d304-acc0-460b-81ae-42f3d0093d98">

2. **Main functions for CRUD on databse**
   <br>d. _main.py_: execute command-line-like functions from ./mylib for CRUD (Create, Read, Update, Delete) on SQLite database.
   <br>e. _test_main.py_: test if the main function successfully conducts ETL.
   Example output:

4. **Github Actions Setup to test different python versions**
  <br>f. _.github/workflows/main.yml: Development environment was set up using **different versions of python** for later actions. The actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

5. **Other files for development environment settings**
  <br>g. _.devcontainer_: contains devcontainer, setting up the environment for development.
  <br>h. _.gitignore_: specifies file names to ignore.
  <br>i. _requirements.txt_: lists required packages for the project.

6. **Description of the project**
   <br>j. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


