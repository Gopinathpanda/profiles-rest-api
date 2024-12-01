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

### 3. Creating Django Application
1. Create Python virtual environment in vagrant server under /vagrant folder.

>  python -m venv ~/env (It will create the virtual machine under in home directory of vagrant server (~ will do it))
2. Activate the virtual environment
> source ~/env/bin/activate

3. Create requirements.txt and install requirements by typing below commands:-
> pip install -r requirements.txtb  
4. Create Django Project
>  django-admin.py startproject profiles_project . ('.' represents the location if we don't specify this it will create a sub folder)
5. Create a application
>  python manage.py startapp profiles_api
6. Enable Django settings by adding below under INSTALLED_APPS
> 'rest_framework',
    'rest_framework.authtoken',
    'profiles_api'
7. Test the Django project under vagrant server where virtual environment enabled
> python manage.py runserver 0.0.0.0:8000
8. Go to localhost from your browser.

> localhost:8000 or 127.0.0.1:8000
9. commit and push changes

### 3. Setup Database
1. In models.py file add code
2. Add below line in settings.py for authentication
> AUTH_USER_MODEL =  'profiles_api.UserProfile'

3. Create migrations under vagrant server when the virtual environment is activated
>  python manage.py makemigrations profiles_api

4. Migrate changes

> python manage.py migrate

### 4. Setup Django Admin
1. Create a super user -> A user with max privileges over the DB

> python manage.py createsuperuser

2. Enable Django admin

Add changes to admin.py by registering the model

3. run the server on vagrant env and go to http://127.0.0.1:8000/admin url and log in using pandagopina****@gmail.com and pass is 
G********0. The UserProfile model shown as User profiles


### 5. Intro to APIView
1. Basic type of view to build our APIs. Describe the logic to make API endpoint.
2. It uses standard HTTP methods for functions. get , post,put,patch(partially update an item.),delete
3. Gives most control on our application logic. Perfect for implementing complex logic and calling other APIs 
and working with local files.
4. For processing files and rendering a synchronous response and accessing local files or data it is best suited.
5. Write the HelloApiView class as APIView for demonstration and also include the profiles_api urls.py file in the root urls.py
6. Then run the server and go the url for HelloApiView.(http://localhost:8000/api/hello-view/)




