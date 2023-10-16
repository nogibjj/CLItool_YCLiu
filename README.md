[![CI](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml)
## Use Python Click to Develop Command-Line like Tool

This repository demos how to use the python *click* library to build command-line-like tool to get information from database. Two tables were created using SQLite to test the tool's functionalities. 

Below is an overview of the files in this project:

1. **Database setup**
   <br>a. _mylib/create.py_: **Build a database**, **create tables**, fill in values.
   
3. **Main functions for querying on databse**
   <br>b. _main.py_: execute command-line-like functions from ./mylib to create a database, tables, and to query on the created database. Specifically, it does the following:
<br>         1. Build a SQLite database _Transaction.db_.
<br>         2. Create a table named *Customer*, with the following columns: *cust_id*, *name*, *sex*. Below is the content of the resulted table.

**Customer table**

| cust_id | name | sex |
|---|---|---|
|001| John | Male |
|**_002_**| **_Devin_** | **_Female_** |
|**_003_**| **_Sharon_** | **_Female_** |
|004| Tim | Male | 
|**_005_**| **_Tina_** | **_Female_** |

   
4. **Github actions setup for continuous integration**
  <br>c. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

5. **Other files for development environment settings**
  <br>d. _.devcontainer_: set up the environment for development.
  <br>e. _.gitignore_: specify file names to ignore.
  <br>f. _requirements.txt_: list required packages for the project.

6. **Description of the project**
   <br>g. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


