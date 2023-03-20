#  Blog between users
The application allows you to create blog entries for registered users, edit and delete them, as well as leave comments.

## Images

## Technology Stack
* Python 3.7.x
* Django Web Framework 4.1.x
* BootStrap 5.2.x
* HTML/CSS


## Functionalities
* Authentication and authorization model for users
* Users can create edit and delete (CRUD)  blog posts

## ⚙️ Project structure
* `accounts` Contains basic information about for creating a user account
* `pages` The main pages of the application
* `posts` Creating editing deleting blog posts
*   `static` CSS styles
*  `templates` HTML project templates

## Deployment
Clone this repository

`$ git clone https://github.com/natarovvar/pet-django.git`

create a `.env` file in your project directory and add  `SECRET_KEY`

```python
#your_project_directory/.env

SECRET_KEY = YOUR_SECRET_KEY
```


Install additional packages
* `python-decouple`
* `Django`
* `django-extensions`
* `django-crispy-forms`
* `crispy-bootstrap4`

Now run the makemigrations command, execute the makemigrations command to perform data migration to save the "Bridges" in the database. then perform the migration to load the data migration operations into the database.

`$ python manage.py makemigrations`

`$ python manage.py migrate`

create  `superuser`

`$ python manage.py createsuperuser`

Start the local server

`$ python manage.py runserver`

the server will be available at  http://127.0.0.1:8000/


