# SaaSproject

#
#1. Navigate to Project Folder in terminal
#2. Install or Sync virtual environment
##$ pipenv install
##$ pipenv sync
#3. Start virtual environment
##$ pipenv shell
#3. Execute the bootup script within the virtual environment
##$ ./bootstrap.sh
#4. Navigate to the desired URL from the three provided below
##http://127.0.0.1:5000/chartdatacsvpost/home/kxa/PycharmProjects/UofMProject/idlist.csv
###URL For task 1.1 accepting the PATH location of a CSV list of Ids as a URL parameter and returning data for the give Ids
###The URL variable is the location of the CSV file to be parsed. 
###A sample CSV (idlist.csv) has been provided in the project folder
##http://127.0.0.1:5000/smdataqu
### The URL for task 1.2, accepts no parameters, and returns a summary of admissions grouped by Observation Type and Unit of Measure. This data object was returned from the database using a SQL query
##http://127.0.0.1:5000/smdatapd
### The URL for task 1.3, accepts no parameters, and returns a summary of admissions grouped by Observation Type and Unit of Measure. This data object was returned from the database using a SQL query to pull the data and pandas to filter and group the data.

#Challenge Part 2
#Summary

#1. Navigate to Project Folder in terminal
#2. Install or Sync virtual environment
##$ pipenv install
##$ pipenv sync
#3. Start virtual environment
##$ pipenv shell
#4. Build the image based on the Dockerfile included within the application
## $ docker build -t chartdata .
$5. Save docker image
$$$ docker save chartdata > chartdata.tar
#6. Load docker image (not necessary if still in virtual environment)
$$$ docker load < chartdata.tar
#7. Run the docker image
##docker run --publish 5000:5000 chartdata
