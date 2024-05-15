# iFireTracker Group Project current state

### Access to our Servers and RDS:

1. **Model server on EC2-1 (DATA472-rna104-JARRD-Model-Server)** Public access for all, find the instance on AWS EC2
2. **WebServer on EC2-2 (DATA472-rna104-JARRD-WebServer)** Public access for all, find the instance on AWS EC2
3. **Auth server on EC2-3 (DATA472-dus15-JARRD-Auth-Server)** Public access for all, find the instance on AWS EC2
4. **MySQL server on RDS (data472-rna104-jarrd-db)**
   1. Run the command from any EC2 server to connect to MySQL DB. 
   2. Command: mysql -h data472-rna104-jarrd-db.cyi9p9kw8doa.ap-southeast-2.rds.amazonaws.com -P 3306 -u ucstudent -p
   3. Password: DATA472JARRDmads


Current state at 15.05.2024 12.00:

1. Created all instances.
2. Deployed the Jess model into Model Server on EC2-1.
3. Has been wrote Roman script for saving outputs table data into MySQL DB.

### Next week on Wednesday will be Final Presentation with Demo of all Group Projects.

#### Please see Architecture of our system (actual on this current moment) and Blocks description in Pictures on this folder.

### NEXT TO DO:

**Roman**:

1. Create **storage data472-jarrd-hdd on S3**
2. Write Roman script to send HTTP API request from WebServer to S3 with .csv and .html files to save on WebServer filesystem.

**Dmitrii**:

1. Process HTTP API "sign up" query from Web Server and save data to RDS (just create SQL **INSERT** query to MySQL DB on RDS). Return to Web Server answer that user was saved.
2. Process HTTP API "log in" query from Web Server and send **SELECT** query to MySQL on RDS. Return to Web Server answer that user was found or not.

**Ruben**:

1. Debug and run Ruben scrapping script on EC2 Model server and save into .csv files on EC2 file system. Check with the format of already existing files.

**Jess**:

1. Add logging information of the model.

**Anirudh**:

First of all:
1. On the **Main page** the User can choose the day using Calendar and can click on two possible options Map or Table (can be as a tabs) (just create a links to the files .html and .csv that you have got from Model Server).
2. On the **Auth page** the User can make "Sign Up" or "Log In" actions.

Then (I can help with this):
1. When "Sign Up" - send HTTP API "sign up" query to Auth Server on EC2-3 and process response (just display on the page is it OK/NOT OK)
2. When "Log In" - send HTTP API "log in" query to Auth Server on EC2-3 and process response (just display the Main page)



