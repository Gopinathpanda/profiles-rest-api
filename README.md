# Profiles REST API

Profiles REST API course.

### 1. Initialize git and Push the README.md, LICENCE and .gitignore files
1. git init
2. ssh key generation 
> ssh-keygen -t rsa -b 4096 -C "pandagopinath95@gmail.com"
3. Create README.md and LICENSE file, .gitignore file and do git commit
4. add id_rsa.pub key to git if not added.
5. Create a github repo and push the commited code. ( 
> git remote add origin https://github.com/Gopinathpanda/profiles-rest-api.git)

### 2. Creating a development server to run and test API(Vagrant)
1. Run the below command to create the Vagrantfile from base image ubuntu/bionic64
 > vagrant init ubuntu/bionic64
2. Download the base image mentioned in the Vagrant file and create a virtual machine using virtualbox and run the script
 > vagrant up
3. To connect to the vagrant server
> vagrant ssh 
4. In this guest OS we can run our application and exit to go to local machine.
5. To create any file which is point to profiles-rest-api do cd /vagrant