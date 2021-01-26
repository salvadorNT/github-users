# Flask Github Users

Flask application for bringing the firsts users using the Github API.

## Features

 - Load to a database, the first "n" users from github.
 - Retrieve a list of previously loaded users of github on a view.
 - Select the number of result per page and page desided.
 - Use the users resource of the API for bringing users, ordering by (ascending or descending):
	 - username
	 - id
    
## Screen Shot
index page

<a href="https://drive.google.com/uc?export=view&id=1qp97OeRYu0rJ-O9Fh1uKc7uasXrr0PvB"><img src="https://drive.google.com/uc?export=view&id=1qp97OeRYu0rJ-O9Fh1uKc7uasXrr0PvB" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

Selecting page

<a href="https://drive.google.com/uc?export=view&id=1U_Yqlv9xABzGtWP1Qj-M_OEnKhgw1HYb"><img src="https://drive.google.com/uc?export=view&id=1U_Yqlv9xABzGtWP1Qj-M_OEnKhgw1HYb" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

Mobile responsive view

<a href="https://drive.google.com/uc?export=view&id=1rHVrvM1R7xamL3Mn7WCC1k3No7uzeW8K"><img src="https://drive.google.com/uc?export=view&id=1rHVrvM1R7xamL3Mn7WCC1k3No7uzeW8K" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
API Users resource response

<a href="https://drive.google.com/uc?export=view&id=1v694kIE9WgQbmDyFfOXKXW8cYcqjGtvL"><img src="https://drive.google.com/uc?export=view&id=1v694kIE9WgQbmDyFfOXKXW8cYcqjGtvL" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

## How to run

 1. Clone the repo via https or ssh
 
 - **git clone [https://github.com/salvadorNT/github-users.git](https://github.com/salvadorNT/github-users.git)**
 - **git clone git@github.com:salvadorNT/github-users.git**

2. Create a virtual env to install dependencies
   

3. Run command to install dependencies under project directory

    `pip install -r requirements.txt`
   

4. Create env variables

    `export FLASK_APP=server.py`

    `export FLASK_DEBUG=1`

    `export FLASK_ENV=development`


5. Configure app/default_config.py for development purposes or use as it is. By default this file configures sqlite database.
For deployment create a file application.cfg.py at app/instance/ and configure the database connexion and secret string. This file must not be added to versioning.


6. Create database and database structure by running the migrations files using dbmanager.py

    `python dbmanager.py db upgrade`


7.  Populate the database with the script seed.py, optionally you can pass it a parameter indicating the desired users to be added to the database. By default the total of users is 150 if no parameter is passed. Consider the limitations for github API requests, for no authenticated users, the limit is 60 requests per hour.


usage: `python seed.py <int:users_amount>`


example: `python seed.py 650`
	This example will populate with the first 650 users.
	
This script uses a custom personal library to easily do requests to retrieve users from github users. This library was uploaded to [https://test.pypi.org/](https://test.pypi.org/) at [https://test.pypi.org/project/github-sdk/](https://test.pypi.org/project/github-sdk/) and also is added in requirements.txt as github-sdk @ [https://test-files.pythonhosted.org/packages/a1/9f/d8b84edc9355562a6664dd4990c10288c1b6ec46efbe40fd4036e9807cdc/github_sdk-0.0.21-py3-none-any.whl](https://test-files.pythonhosted.org/packages/a1/9f/d8b84edc9355562a6664dd4990c10288c1b6ec46efbe40fd4036e9807cdc/github_sdk-0.0.21-py3-none-any.whl)

  

When the script starts adding users will print “Populating database...” if an user can not be added it will print the username. If all were ok, will print at the end “Database populated”.

8. Run tests to verify the functionality of the app.Use the next command.

`flask test`
9. Run an instance of the application and go to a browser to verify that the application is working.

`flask run` 

## App Demo

You can also visit the example at [https://github-usrs.herokuapp.com/](https://github-usrs.herokuapp.com/) for a kick view.

## API endpoint

`/api/users`

The endpoint accepts the next parameters:

`<int:page>`: page to retrieve from the query of users, default is 1

`<int:page_size>`: amount of users per page, default is 25

`<string:order_by>`: choices are id and username, by default is id if none is passed

`<string:order>`: orders the results ascending(asc) or descending(desc), default is ascending

  
Also you can try testing at:  
  
https://github-usrs.herokuapp.com/api/users?page=2&page_size=5&order_by=username&order=desc

## Testing

When running the command `flask test` will run all test under tests directory. If all tests passes will show the next message.

<a href="https://drive.google.com/uc?export=view&id=1c5NPHVTgWpBSTK9f6x7-z7klQVQJXmod"><img src="https://drive.google.com/uc?export=view&id=1c5NPHVTgWpBSTK9f6x7-z7klQVQJXmod" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>