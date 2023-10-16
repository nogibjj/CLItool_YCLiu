[![CI](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/SQLite_YCLiu/actions/workflows/cicd.yml)
## Use Python to Develop and *Distribute* A Command-Line-Like Tool

This repository demos how to use the python *click* library to build command-line-like tool to get information from database. Two tables were created using SQLite to test the tool's functionalities. The tool is then turned in to a **downloadable distribution** for users to use.

Below is an overview of the files in this project:

1. **The Downloadable Package to Browse Database Content**
   <br> a. _dist/database-browser-0.0.1.tar.gz_: ***Download this file***, following the step below, you can use the tool to ***output all table names in an existing SQLite database***.
   <br> Step 1: **Unzip** the file and put it in the desired directory.
   <br> Step 2: **Use the terminal to navigate to the directory** (where you can see the *main.py* file).
   <br> Step 3: **Enter the following command** in the terminal and **press enter**. The ***name of the tables*** in the specified SQLite database will be ***printed out line by line***.
   ```
          python3 main.py "directoryToASQLiteDb"
   ```

   **Example usage**:<br>
   <br> <img width="552" alt="Example Output" src="https://github.com/nogibjj/CLItool_YCLiu/assets/46064664/79a87923-1f44-46ca-96ed-4e9282f45838">
   
2. **Homebrew Library Setup**
   <br>b. _dbBrowser/create.py_: **Build a database**, **create tables**, fill in values.
   <br>c. _dbBrowser/main.py_: Execute create.py to create database and tables. Then use **python click** define a function to **print out all table names** in the specified *SQLite* database. Below are the details of the main function:
<br>         i. Build a SQLite database _Transactions.db_.
<br>         ii. Create a table named *Customer*, with the following columns: *cust_id*, *name*, *sex*. Below is the content of the resulted table.

**Customer table**

| cust_id | name | sex |
|---|---|---|
|001| John | Male |
|002| Devin | Female |
|003| Sharon | Female |
|004| Tim | Male | 
|005| Tina | Female |

<br>         iii. Create a table named *TXR* (short for transaction), with the following columns: *cust_id*, *item*, *amount*. Below is the content of the resulted table.

**TXR table**
| cust_id | item | amount |
|---|---|---|
|001| Hot Dog | 100 |
|001| Hot Dog | 20 |
|002| Hamburger | 80 |
|002| Hot Dog | 120 |
|003| Hamburger | 60 |
|003| Hot Dog | 200 |
|004| Hot Dog | 40 |
|004| Hamburger | 140 |
|005| Hamburger | 150 |
|005| Hamburger | 80 |

<br>         iv. Using **python click**, a function called *findTables* is defined to print out all the tables in the specified SQLite database. The **user manual** is detailed in **Section 1a**. Note that *if the input database directory does not exist*, the function will *throw an error*.
   
3. **Specification for Packaging Library**
  <br>d. *setup.py*: Details of for **packaging the dbBrowser** library (e.g. required dependencies, version name, author name etc.) were specified in the file. The *tar* file in **section 1a** is generated using *setup.py*.
4. **Test Main Function**
   <br>e. *test_main.py*: Test the code in the main function and check if the output is correct using *Transactions.db*.
5. **Github actions setup for continuous integration**
  <br>f. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of installing packages, linting, testing, formatting would be executed in order (specified in Makefile). 

6. **Other files for development environment settings**
  <br>g. _.devcontainer_: set up the environment for development.
  <br>h. _.gitignore_: specify file names to ignore.
  <br>i. _requirements.txt_: list required packages for the project.

7. **Description of the project**
   <br>j. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


