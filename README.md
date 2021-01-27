# dataproject-sqlalchemy

## This is same data project but with the usage of sqlalchemy DBAPI and Postgres as the data source for extracting data.

1. **Context of this Project**:
   * This Project is meant to represent the data of IPL of 10 seasons(2008-2017) in bar charts on browser using JavaScript while extracting data from Postgres using SQLAlchemy DB API.
   * 4 questions are given to chart respective processed data from database 'ipl project' using sqlalchemy and python to create json objects.
   * Question 1 is about Plotting a bar chart of all IPL teams and their sum total runs from all seasons.
   * Question 2 is about Plotting a bar chart of Top 15 batsman of RCB in terms of scored runs for the RCB team in all seasons.
   * Question 3 is about Plotting a bar chart of all Umpires of foreign origin who participated in IPL coutry wise in descending order of count
   * Question 4 is about Plotting a bar chart of All IPL teams and total number of matches played by each team separated by season in a stacked bar chart format.

2. **Setting up Environment**
   * clone this repo to your local directory with clone command
   * command: `git clone git@gitlab.com:mountblue/cohort-14-python/vijay_yarramsetty/dataproject-sqlalchemy.git`
   * we require CSV files for writing all the data to iplproject database and from there we process it using SQL Alchemy DB API and create Json files for plotting the bar charts. so the downloadable csv files are present in the following link
   * [Download csv files from this link](https://drive.google.com/drive/folders/1ZVGo8JMkQ3aMRxYl5ttyb-MSuzXahaCp?usp=sharing)
   * One **Important** thing to make note is that the 3 CSV files should be kept in sub directory `data` in the local repository for running python script files 'main.py', 'schema.py' to write the csv data to database tables using SQL Alchemy engine, and querying that data and creating Json files.
   * Create a Virtual Environment for this project as we require some dependency packages to be installed.
     * `python3 -m virtualenv env` - creates a virtual environment in the root directory of cloned project
     * `source env/bin/activate` - activates virtual environment
   * We have 2 essential dependency packages 'sqlalchemy', 'psycopg2' to be installed using **pip** command on terminal. There is a 'requrirements.txt' file in the cloned root directory. Using the following command you can install those dependency packages. 
     * `pip install sqlalchemy` 
     * `pip install psycopg2`
   * We require a Database and a User  who is owner for that database. For this there are two helper SQL script files present in **sql_scripts** directory. The file names of these two files are self explanatory as one creates a user and a database and the other script file deletes the user and database from Postgres. To run this commands we must go to the same directory in command line(cd ~/sql_scripts) and then follow the below commands.
     * `sudo -su postgres` - we login as a postgres user from command line
     * `psql -U postgres -f create_user-db.sql` - creates a rol and DB. Both will have same names as per conventionn 'iplproject'
     * `psql -U postgres -f drop_user-db.sql` - for dropping both user and database from Postgres when work is done. 
   * Now, go to the **data** directory from command line and run `schema.py` file which creates 3 tables in **iplproject** database.
   * Now, run the `main.py` file that will first write the **csv** data to databse and in turn query the data from databse using SQL Alchemy DB AP and creates 4 json files that are needed for JavaScript file to fetch the json data.
   * Now from Terminal comback to Project root directory and create a local web server using python command `python3 -m http.server 8000`
   * Now access localhost url in browser by typing [http://0.0.0.0:8000](http://0.0.0.0:8000)
   * After that click on [main.html](http://0.0.0.0:8000/main.html)
   * For each Question there is a dedicated button and when we click on it, the bar chart of that context will be displated using Javascript Highcharts library in the backend.