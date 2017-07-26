# Lazada API entrance test
> Create some API test cases and execute them automatically using **Python** language and **Behave Framework**.
> API test URL : `https://jsonplaceholder.typicode.com/users`
> API documents: `https://github.com/typicode/jsonplaceholder`

## Libraries

- PyHamcrest (User for assertion)
- Behave (BDD with gherkin language)
- Requests (Interact with API)
- Allure-behave

## Pre-requisites
- [Python 2.7.13](https://www.python.org/downloads/release/python-2713/)
- [Scoop](http://scoop.sh/)
- [Allure-report](#report)

## Installation
1/ Clone this repo to your local

2/ Install requirements

- Open **command-line** in the Root folder

```sh
pip install -r requirements.txt
```

3/ Execute  this command to run all the test scenarios (test cases) in the feature file
```sh
behave
```

## Usage example

Test cases can be run by categories, currently there are 2 **categories** for these test cases.
1. `happy`
2. `negative`

To run specific category just add `--tags=@categoryname` after `behave` command
*Examples:*

```sh
behave --tags=@happy
```
*Explain: This will run all the test cases with category `"happy"`*

## Reporting
> Because the **Behave** framework itself only support xml output, so we will use an Allure Report plugin to generate HTML report

### <a name="report"></a>1. Installing Allure CMD application
- To install Allure, download and install [Scoop](http://scoop.sh/) and then execute in the Powershell:
```
scoop install allure
```
- In case the `Allure` command is not executeable , try adding this allure binary path to PATH environments of windows
```
C:\Users\{current user}\scoop\apps\allure\{version}\bin
```
### 2. Generate HTML report from Test Result
- In the Root folder of this repo, open CMD and execute the test with output:
```
behave -f allure_behave.formatter:AllureFormatter -o Reports_Temp ./features 
```
- Generate report by executing this command
```
allure serve Reports_Temp
```
`Reports_Temp` is the folder contains temporary files for test result

Example:
Overview page:
![alt text](https://github.com/vietphamqq/LazadaTest/tree/master/.github/Report1.png "Overview")

Scenario/Package page:
![alt text](https://github.com/vietphamqq/LazadaTest/tree/master/.github/Report2.png "Package")


## Testcases
##### 1/ Happy cases
- Verify get list users by sending `GET` request to API server
- Verify get a specific user by sending `GET` request to API server
- Verify create an user by sending `POST` request to API server
- Verify update an exited user by sending `PUT` request to API server
- Verify delete an exited user by sending `DELETE` request to API server

##### 2/ Negative cases
- Verify a `GET` request to search for invalid/non-exist username will response empty
- Verify a `POST` request to create a new user is fail when there is no user data/information
- Verify a `PUT` request to update an user will return 404 status code when using invalid user id
- Verify a `GET` request will return 404 status code when sending to an invalid hostname
- Verify a `DELETE` request will return 404 status code when deleting an invalid/non-exist user id


## File & Folder Structure
+ `features` contains all the feature file (scenario/test cases are put inside each feature file )
+ `features\steps` contains all step definitions for feature files
+ `models` contains all .py file for actions when interacting with API
+ `helpers` contains all .py file for helping methods\functions (Send PUT/POST/GET request action,...)
+ `environment_constants.py` a .py file contains all constants variable that used through the framework
+ `requirements.txt` a text file contains all required lib for the framework

## Release History

* 0.0.1
    * CREATE: Design and write API automation test cases 
    * CREATE: Write documentation


## Meta

Viet Pham - [Email](mailto:phamquangquocviet@gmail.com) - [Github](https://github.com/vietphamqq)

