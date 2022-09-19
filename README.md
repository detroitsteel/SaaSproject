# uofmproject
#This project was created in response to the University of Michigan Software Developer Challenge Part 1. This project will create a RESTapi developed using python 3.8, a provided SQLite DB, and the web server Flask. Below is a detailed description of how to run the project, and the three endpoints to access the requested data.

#
#1. Navigate to Project Folder in terminal
##$ cd ~/PycharmProjects/UofMProject
#2. Start virtual environment
##$ pipenv shell
#3. Execute the bootup script within the virtual environment
##$ ./bootstrap.sh
#4. Navigate to the desired URL from the three provided below
##http://127.0.0.1:5000/chartdatacsvpost/home/kxa/PycharmProjects/UofMProject/idlist.csv
###URL For question 1.1 accepting the PATH location of a CSV of Ids as a URL parameter and returning data for the give Ids
###The URL variable is the location of the CSV file to be parsed. 
###A sample CSV (idlist.csv) has been provided in the project folder
##http://127.0.0.1:5000/smdataqu
###URL for question 1.2, accepts no parameters, and returns a summary of admissions grouped by Observation Type and Unit of Measure. This data object was returned from the database using a SQL query
##http://127.0.0.1:5000/smdatapd
###URL for question 1.3, accepts no parameters, and returns a summary of admissions grouped by Observation Type and Unit of Measure. This data object was returned from the database using a SQL query to pull the data and pandas to filter and group the data.
