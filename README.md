# `Fire Predictions in Christchurch` Group Project for DATA472 course at the University of Canterbury

## Contributors

Jess - developer of the model
Anirudh - developer of the website
Roman - creating and integration of Model/WebServer/S3/RDS together
Ruben - developer of the scrapper
Dimitrii - developer of the authorization part, integration Auth and Web servers.

All of contributors participated in continuous generation of the idea of the project, develop documentation etc.

## Presentation

The presentation of our group project is available in the folder "Presentation"


## The pipeline how to deploy web server environments and web application into Amazon Cloud (AWS) is below


### 1. Clone this repository into `PATH-YOUR-LOCAL-DIRECTORY` on local computer

git clone https://github.com/UC-JARRD/iFireTracker.git


### 2. Create a AWS EC2 instance

Follow the instructions from Paul Benden, access on LEARN (University of Canterbury internal page, only for students) in the AWS Resources chapter of this course.   

Additionally, basic information how to create and tune your EC2 instance you can find on the official AWS website here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html


### 3. AWS setup

1. To work with EC2 instance you should connect to this virtual environment. You can do it using `ssh` or just use AWS web interface to click the `Connect` button on the top right corner of EC2 instance page and select the tab `EC2 Instance Connect` by default, you will be able to connect to the instance without any further setup.

![AWS connection](./images_for_readme/aws-conn.png)

2. Copy the folder from `PATH-YOUR-LOCAL-DIRECTORY` to EC2 home directory running the command below on your local machine in terminal

```
cd <PATH-YOUR-LOCAL-DIRECTORY>
scp -i <PATH-TO-YOUR-PEM-KEY-ON-LOCAL-MACHINE> -r iFireTracker ubuntu@<EC2-PUBLIC-IP-ADDRESS>:/home/ubuntu/
```


### 4. Setup Flask app environment on EC2

1. Using bash on EC2 create the `venv` folder in the `iConferenceGame` folder and activate this environment using the following commands:
2. Enter to the folder `iConferenceGame` using the command `cd iConferenceGame`

```bash
sudo apt-get update
sudo apt install python3-virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

3. Install the required packages using the command: 

```bash
pip install requirements.txt
```

4. Finally, your app folder should be like the following:

![Files structure](./images_for_readme/aws-files.png)


### 5. Setup Gunicorn environment on EC2

1. Copy a `flaskapp.service` file from `iConferenceGame` to the `/etc/systemd/system/` folder using the command 

```bash
sudo mv flaskapp.service /etc/systemd/system/
```

Note: If your EC2 instance image is not buntu, you should replace the `ubuntu` with the correct user name in the `flaskapp.service` file.

2. Enable the service by running the following command:

```bash
sudo systemctl start flaskapp
sudo systemctl enable flaskapp
```

### 6. Setup Nginx environment on EC2 

1. Install nginx by running the following command:

```bash
sudo apt-get update
sudo apt-get install nginx
```

2. Start Nginx:

```bash
sudo systemctl start nginx
```

3. Enable Nginx reverse proxy by updating a file named `default` in the `/etc/nginx/sites-available/` folder. You should replace the IP address in the file with your `EC2-PUBLIC-IP-ADDRESS` IP address.

```bash
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name <EC2-PUBLIC-IP-ADDRESS>;

        location / {
                proxy_pass         http://127.0.0.1:8000/;
                proxy_redirect     off;

                proxy_set_header   Host                 $host;
                proxy_set_header   X-Real-IP            $remote_addr;
                proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Proto    $scheme;
        }
}
```

4. Restart Nginx by running the following command:

```bash
sudo systemctl restart nginx
```

![Nginx and Flask status](./images_for_readme/nginx_flask_status.png)

Now the game will be avalable at the EC2 public IP address from the browser. `http://<EC2-PUBLIC-IP-ADDRESS>`


### 7. Workflow of the Conference Mini Game

You can see the workflow (screenshots) of the Conference Mini Game below

![Page 1](./images_for_readme/page1.jpg)

![Page 2](./images_for_readme/page2.jpg)

![Page 3](./images_for_readme/page3.jpg)

![Page 4](./images_for_readme/page4.jpg)

![Page 5](./images_for_readme/page5.jpg)

![Page 6](./images_for_readme/page6.jpg)

![Page 7](./images_for_readme/page7.jpg)


## Conclusion

This Mini Game is one of the part of our group prototype at the HITD603 course. Another parts of full Conference Game prototype include Arduino and Unreal Engine technologies. The whole Conference Game prototype was developed from scratch (from idea to implementation) within 2.5 weeks. If you have any questions, please feel free to ask me.