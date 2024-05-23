1. Create auth folder in the home directory
2. Create app.py and copy content from web_server_auth.py
3. Create a folder "templates" and copy html files inside
4. create flaskapp.service in etc/systemd/system/ folder and paste the following:
[Unit]
Description=Data472 web server flask app
After=network.target
[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/auth
ExecStart=/home/ubuntu/auth/venv/bin/gunicorn -b 0.0.0.0:8000 app:app
[Install]
WantedBy=multi-user.target

5. Enable gunicorn (follow Hua's instructions)
6. Check status of flaskapp. If it is running, you should be good to go and test it in the browser