
# Interview Space
### This project enables developers of all levels to study for an interview. 

### This is a REST API created using the Django Rest Framework which will later be used as a backend for my React application. 
### The application has questions grouped by:
- advancement level
- technology
- the field of programming
 
### The user also has the option of creating an account, which allows him to add new questions, answer questions, save questions to favourites and delete them.


## Database diagram

<img src="/images/database.png"/>

## Endpoints

<img src="/images/endpoints.png"/>

### GET /levels/
Returns a list of levels 
### GET /comments/<question_id>/
Returns a list of comments for the specified question
### POST /comments/create/{question_id}
Allow user to create a new comment for a specified question id
### POST /favourites/add/{question_id}/ 
Allow authenticated users to add questions to their favourite list
### POST /favourites/delete/{question_id}/ 
Allow authenticated users to delete saved question from their list
### GET /languages/ 
Returns a list of all programming languages
### GET /questions/ 
Returns a list of all questions parameters: lang, level, category
### GET /questions/{question_id}
Returns a single question objects based on id 
### POST /questions/create 
Allow authenticated users to add a new question
### POST /user/login/ 
Allow user to log in 
### POST /user/logout/
Allow logged user to logout 
### GET /user/profile/ 
Allow authenticated user to get their list of saved questions 
### POST /user/register/ 
Allow user to create a new account with username, email and password


## Project is based on technologies such as:
- Python
- Django
- Django Rest Framework






## Installation

Clone the repository

```bash
git clone <link>
```

Install the requirements

```bash
pip install -r requirements.txt
```

Inside base (setting.py) folder add .env file. It should looks like this:

```bash
SECRET_KEY=XXXXXXXX
```

Now run Django server using this command 

```bash
py manage.py runserver
```

## Postman 

https://api.postman.com/collections/26593763-780af17f-042e-4275-9999-026babea8eca?access_key=PMAT-01GX8XG9EEMNQB5KYFHVYX0FR9

## Running Tests

To run tests, run the following command

```bash
  py manage.py test <APP NAME>.tests 
```

For example to run tests for "base" application you can type: 

```bash
py manage.py test base.tests
```


## Authors

- [@DEENUU1](https://www.github.com/DEENUU1)

