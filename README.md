# sendIT
[![Maintainability](https://api.codeclimate.com/v1/badges/db4df351dbe833d147b0/maintainability)](https://codeclimate.com/github/ipaullly/sendIT/maintainability)
 [![Build Status](https://travis-ci.com/ipaullly/sendIT.svg?branch=ft-GET-user-orders-161858618)](https://travis-ci.com/ipaullly/sendIT) [![codecov](https://codecov.io/gh/ipaullly/sendIT/branch/ch-code-climates-161921842/graph/badge.svg)](https://codecov.io/gh/ipaullly/sendIT) 

The sendIT app is built using flask to make RESTful APIs to achieve basic functionalities for the app 

## RESTful API Endpoints for sendIT


| Method        |       Endpoint                        |         Description                           |
| ------------- |       -------------                   |         -------------                         |
| `POST`        | `/api/v1/parcels`                     |   Create a new parcel order                   |
| `GET`         | `/api/v1/parcels`                     |   Get a all parcel delivery orders            |
| `GET`         | `/api/v1/parcels/<int:id>`            |   Get a single delivery order by id           |
| `POST`        | `/auth/v1/register`                   |   Register a new user                         |
| `POST`        | `/auth/v1/login`                      |   log a user into account                     |
| `PUT`         | `/api/v1/parcels/<parcelId>/cancel`   |   Cancel a specific parcel delivery order     |


# Development Configuration

Ensure that you have python 3.6.5, pip and virtualenv running

# Initial Setup

Create a project directory in your local machine

```
mkdir sendIT
```

Move into your directory:

```
cd sendIT
```

## Initialize a virtual python Environment to House all your Dependencies

create the virtual environment

```
python3 -p virtualenv venv 
```
activate the environment before cloning the project from github

```
source venv/bin/activate
```

## Clone and Configure a the sendIT flask Project

Provided you have a github account, login before entering the command to create a local copy of the repo

```
git clone https://github.com/ipaullly/sendIT.git
```

Next, install the requirements by typing:

```
pip install -r requirements.txt
```
## Running the sendIT flask app locally

Once you are in a virtual environment with all the dependencies installed, set the environmental variables:
```
export FLASK_APP=run.py
export FLASK_ENV=development
```
initialize the server with the command:
```
flask run
```

## Testing
To test the endpointsensure that the following tools are available the follow steps below

### Tool:
    Postman

  with the flask server running power up POSTMAN to test your endpoints. set the localhost:
  ```
  http://127.0.0.1:5000/
  ```
  append the localhost with urls for the various endpoints, for example:
  ```
  http://127.0.0.1:5000/api/v1/parcels
  ```
  ensure to set the correct HTTP method before sending the request.
  
  Alternatively you can access the API documentation via this [link](https://documenter.getpostman.com/view/4014888/RzZCCwun#22450978-87c5-be21-e538-51cd4100035a).
     
### Commands
  The application was tested using `pytest` and code cov.
  run the command
  ```
  pytest --cov app
  ```
  this generates a detailed log of the tests in your app directory
