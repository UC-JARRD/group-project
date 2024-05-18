# iFireTracker Group Project current state

### Access to our Servers and RDS:

1. **Model server on EC2-1 (DATA472-rna104-jarrdmodelserver2)** Public access for all, find the instance on AWS EC2
2. **WebServer on EC2-2 (DATA472-rna104-jarrdwebserver2)** Public access for all, find the instance on AWS EC2
3. **File server on S3 (data472-rna104-jarrd-hdd)** Public access for all, find the instance on AWS EC2
4. **Auth server on EC2-3 (DATA472-dus15-JARRD-Auth-Server)** Public access for all, find the instance on AWS EC2
5. **MySQL server on RDS (data472-rna104-jarrd-db)**
   1. Run the command from any EC2 server to connect to MySQL DB. 
   2. Command: mysql -h data472-rna104-jarrd-db.cyi9p9kw8doa.ap-southeast-2.rds.amazonaws.com -P 3306 -u ucstudent -p
   3. Password: DATA472JARRDmads


Current state at 18.05.2024 18.00:

1. Created all entities on AWS, EC2s, S3, RDS.
2. Deployed the Jess model into Model Server on EC2-1 - working.
3. Jess added logging to her code - working. 
4. Has written scripts to transfer data between ModelServer and S3, between S3 and WebServer, between ModelServer and RDS - working.
5. WebServer was deployd based on Flask, Gunicorn and Nginx - working. You can see the result on the following addresses:
   1. http://54.66.144.170/query?format=html
   2. http://54.66.144.170/query?format=csv

### Next week on Wednesday will be Final Presentation with Demo of all Group Projects.

#### Please see Architecture of our system (actual on this current moment) and Blocks description in Pictures on this folder.

### NEXT TO DO:

**Roman**:

When Ruben made a Scapping:
1. Make cron to run model everyday
2. Make cron to save data on S3
3. Make cron to get data from S3 and save into WebServer filesystem. 

**Dmitrii**:

1. Process HTTP API "sign up" query from Web Server and save data to RDS (just create SQL **INSERT** query to MySQL DB on RDS). Return to Web Server answer that user was saved.
2. Process HTTP API "log in" query from Web Server and send **SELECT** query to MySQL on RDS. Return to Web Server answer that user was found or not.

**Ruben**:

1. Debug and run Ruben scrapping script on EC2 Model server and save into .csv files on EC2 file system. Check with the format of already existing files.

**Jess**
When Ruben made a Scapping:
1. Take a new file with a new date from Ruben scrapped file.
2. Save a new file with a new date prefix.

**Anirudh**:

First of all:
1. On the **Main page** the User can choose the day using Calendar and can click on two possible options Map or Table (can be as a tabs) (just create a links to the files .html and .csv that you have got from Model Server).
2. On the **Auth page** the User can make "Sign Up" or "Log In" actions.

Then (I or Dmitrii can help with this):
1. When "Sign Up" - send HTTP API "sign up" query to Auth Server on EC2-3 and process response (just display on the page is it OK/NOT OK)
2. When "Log In" - send HTTP API "log in" query to Auth Server on EC2-3 and process response (just display the Main page)



