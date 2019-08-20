## About
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## In This Repo
This project has one main Python module `application.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module and you can populate the database with test data using `lotsofitems.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application. CSS/JS/Images are stored in the static directory.


## Installation
There are some dependancies and a few instructions on how to run the application.
Seperate instructions are provided to get GConnect working also.

## Dependencies
- Vagrant
- Udacity Vagrantfile
- VirtualBox

## How to Install
1. Install Vagrant & VirtualBox
2. Go to Vagrant directory and download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd /vagrant` as instructed in terminal
6. Setup application database `catalog/database_setup.py`
7. Insert fake data `catalog/lotsofitems.py`
8. Run application using `catalog/application.py`
9. Access the application locally using http://localhost:8000


## JSON Endpoints
The following are open to the public:

Catalog JSON: `/catagories/JSON`
    - Displays all catagories.

Category Items JSON: `/categories/<int:category_id>/items/JSON`
    - Displays items for a specific category.

Category Item JSON: `/categories/<int:category_id>/items/<int:item_id>/JSON`
    - Displays a specific category item.


NOTE :	Many parts of this application contains code that I have used from
	the Udacity lessons. Most of it isa standard code like /login, /gconnect,
	/gdisconnect. All the logical parts of code have been written
	by me myself.
