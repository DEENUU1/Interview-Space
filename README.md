
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





### Project is based on technologies such as:
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

### Postman 





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

