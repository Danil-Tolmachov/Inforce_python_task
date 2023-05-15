# Menu API
**Task:** A company needs internal service for its 'employees which helps them to make a decision at the lunch place. Each restaurant will be uploading menus using the system every day over API. Employees will vote for the menu before leaving for lunch on a mobile app for whom the backend has to be implemented. There are users who did not update the app to the latest version and the backend has to support both versions. The mobile app always sends the build version in headers.

## Setup and run API (Docker)
To get started with this API, you'll need to follow these steps:

1.  Clone this repository. 
	<code>git clone *link*</code>

2.  Edit environment variables (**optional**).
3.  Run docker-compose.
	<code>docker-compose up</code>
5.  localhost:8000.


## Endpoints

API version header: **Access-version: v1**


|http               | method | required data      | response|
| ------------------| -------| -------------------|---------|
|/menu              | GET    |                    |200      |
|/results           | GET    |                    |200      |
|/create-restaurant | POST   | Body: name, address|201      |
|/update-menu       | POST   | Query: restaurant  |201      |
|                   |        |Body: items = {dict}|         |
----

|http               | method | required data                  | response|
| ------------------| -------| -------------------------------|---------|
|/register          | POST   | Body: username, password, email|201      |
|/login             | POST   | Body: username, password       |200      |
|/refresh           | POST   | Body: refresh                  |200      |
|/verify            | POST   | Body: token                    |200      |
|/vote              | GET    | Query: menu                    |200      |


## Run Tests
1. Create virtual environment (python 3.10 peferable).
`python -m venv .venv`
2.  Activate virtual environment.
`./.venv/Scripts/activate`
or
`source ./venv/bin/activate`
3. Install required packages.
`cd menu_api`
`pip install -r ./requirements.txt`
4. Run pytest.
`pytest ./tests/`