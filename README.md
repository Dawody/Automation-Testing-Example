# Automation-Testing-Example
This is an example on automation testing that test a signUp process for a web site


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```bash
$ pip install selenium
```

## Usage

```bash
$ python main.py

```

## Components

This project is devided into 4 components :
1. `Reader` : class responsible for reading test cases from jscon file called testCases.json
2. `RequestManager` : class responsible for opening broswer, closing broswer, sending requests and evaluate the request to decide the test result
3. `CaseMonitor` : class responsible for detecting the expected test result according to some specifications.
4. `Main` : the main function that loop on all test cases, use previous components to finally report the testing results.



## Features

- Failed test cases will be taken as screenshot in a new directory called FailureCases\_testDate\_testtTime (e.g FailureCases\_Sep-14-2020\_23:43:10) so you dont have to save this directory in other location because of possible overwriting, I saved it for you.
- More specifications had been added like:
  - Only valid Emails can be accepted (valid emails often follow this regex pattern ``` ^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$``` )
  - Only valid Phone Numbers can be accepted (valid phone numbers contain 11 difit only and starts with 01 )
  - Password should be at least 8 chars
  - internal set had been used to map emails data base to check that only unique emails can sign up.



## Limitation

- test cases should be provided in a json file called testCases.json next to the project source files.
- failures screenshouts will be saved at run time but final report will not be generated before the last test case done.


## License
[MIT](https://choosealicense.com/licenses/mit/)
