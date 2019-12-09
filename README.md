:satisfied:
# RENTALS
#### Application that allow users to find and serch for houses for renting, Monday December 9th 2019 
#### By **OPIYO TITUS**&trade;

## Description
Application that allow users to find and serch for houses for renting

## Project live site
  This is the live .[ Click for the link]()
 ![Image](/static/img/screen.png)
 
 ![alt text](/static/img/screenshort.png)
## Features
* User can log in to application and view available houses.
* A user can search for houses by location.
* A user can update profile.
* Admin can add users and give them paermissions to add houses.
* Admin can delete users



## Behavior Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the application and croll through  | User logs in to use the system | user can view available houses and features of a particular house | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |

|  Homepage loads | Click `profile` | User's profile appears | 
| Homepage loads | Click `upload image` icon | User's redirected to a page where they can upload an image | 
| Homepage loads | Click `settings` icon | A modal appears where one can change their password or logout | 



## Setup/Installation requirements
1.Clone or download and unzip the repository from github,https://github.com/costamay/Rentals.git

2. Activate virtual environment using python3.6 as default handler virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

3. Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
4. Create the Database
- psql
- CREATE DATABASE housefinder;

4. Create .env file and paste paste the following filling where appropriate:

-SECRET_KEY = '<Secret_key>'
-DBNAME = 'instacopy'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True
5. Run initial Migration
-python3.6 manage.py makemigrations instagram
-python3.6 manage.py migrate
6. Run the app
-python3.6 manage.py runserver
-Open terminal on localhost:8000



## Technologies Used
* PYTHON 3.6
* DJANGO FRAMEWORK
* BOOTSTRAP
* CSS
* POSTGRESS

## Prerequisite
* PYTHON 3.6
* DJANGO FRAMEWORK
* PYTHON VIRTULENV
* POSTGRESS
## Support and contact details
contact me @ titusouko@gmail.com
### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved
  