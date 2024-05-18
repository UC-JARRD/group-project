# How to run prototype

1. ## Navigate Directory: 
Navigate to the /iFireTracker/src/prototype directory in the terminal or command prompt.

2. ## Install Packages: 
Run the following command to install all the packages listed in requirements.txt:

``` pip install -r requirements.txt ```
This command will read the requirements.txt file and install each package listed in it.

3. ## Wait for Installation: 
Pip will display progress as it installs each package.

4. ## Run main.py:
Run main.py file.
It should result in the following output:

    Created a DB
    * Serving Flask app 'website'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with watchdog (fsevents)
    Created a DB
    * Debugger is active!
    * Debugger PIN: XXX-XXX-XX 


If this doesn't run you may have dependancy issues and have to update or install some other packages. 
For reference I (JN) had to do the following:
``` pip install flask_sqlalchemy flask_login ```
``` pip install --upgrade watchdog ```

5. ## Open development server

Pase the webaddress (http://127.0.0.1:5000) into a browser. 
From here you can create an account, login and logout.

6. ## Exit

To exit press CTRL+C.