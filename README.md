# flask-content-advisor
Flask app to randomly suggest a type of content to review next

# Run in Container
docker run --name advisor -p 80:5000 flask-content-advisor

# Run Out of Container
[Ensure Flask is installed](http://flask.pocoo.org/docs/0.12/installation/#installation "Flask Installation") and check the instructions for your operating system

## Mac/Linux
```shell
export FLASK_APP=src/app.py
flask run
```

## Windows
```shell
set FLASK_APP=src/app.py
flask run
```

# Infrastructure
An Azure Resource Manager template is included to provision a Linux virtual machine if you prefer to use a machine in the cloud for working with Docker. Enter the following commands bootstrap the machine:
```
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum makecache fast
sudo yum -y install docker-ce
sudo systemctl start docker```