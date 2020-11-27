## About

The project was created using Python 3.8 and Django 3.1

Development environment: Linux

## Installation

1. Create the virtual environment: `python3 -m venv venv` (linux)  / `virtualenv venv` (windows)
2. Activate the environment: `source venv/bin/activate` (linux) / `venv\Scripts\activate.bat` (windows)
3. Install dependencies from the **requirements.txt** file: `pip install -r requirements.txt`

## Initialization/Configuration

1. With the activated environment navigate in the folder **tasks**
2. Rename the **`.env.demo`** file in **`.env`** and set the variables within the file
3. Run the following commands:
    - `python manage.py makemigrations core`
    - `python manage.py migrate`
    - `python manage.py createsuperuser` and set the username and password
    - `python manage.py runserver`

## What the project solves and where are the solutions within the source code

The project solves the following tasks:

> Given a list of blacklisted IPs, e.g.:
> 
>   blacklisted_ips = [“115.124.106.45”, “192.185.113.122”, “104.215.148.63”, ...]
>
> Implement a mechanism in your Django app that would check the IP where the requestis sent from and return a 403 Response in case the IP is in this list.
>
> Constraints:
> - Django 3.X, Python 3.4+
> - We want the check to be done on the app side, not on the web server or the appserver;
> - We want the check to be done ​before​ the request hits any view;
> - We want this done for ​all​ requests automatically;
> - We do ​not​ want to use any other 3rd-party libraries.

Solution:
- Created a middleware that checks for the IP of the request
- The middleware code is in the **`tasks/core/middleware.py`** file
- The blacklisted IPs can be set in the **`.env`** file
- Imported the middleware in the *MIDDLEWARE* variable in the **`settings.py`** file

> Given this function:
>
>```python
>import requests
>    
>def do_request(address):    
>   return requests.get(address)
>```
>Write a decorator that can decorate it and similar functions, such that:
> - If the function returns a response bearing a 408 Request Timeout status code,the function will be recalled X amount of times, where X is an integer argumentwe can pass to the decorator. If, at any time during those recalls, the functionreturns something else than a 408 response, then stop recalling it and return theresult.
> - If any other case, return the result.
>
>Nice to have:
> - a logger.Logger() instance logging each retry, success, failure (failure = all Xretries returned a 408 response)

Solution:
- Created the decorator located in the **`tasks/core/decorators.py`** file
- Decorated the function `do_request` implemented in the **`tasks/core/utils.py`** file
- Used the `do_request` function in the `test_view` function implemented in the **`tasks/core/views.py`** file

> You have a model ​CustomUser ​that inherits from django.contrib.auth.models.AbstractUser​. 
>
> The model has a ​status​ field(corresponding to a DB column, of course) with possible values NEW, ACTIVE,SUSPENDED, and ARCHIVED in your Django app. 
>
> Given these, you need to trigger anexternal service whenever the user status changes.For the sake of simplicity, assume that the call to the external service is handled by this function: 
>
>```python
>
>def sync_user_status(user_id, new_status):
>    ...
>
>```
> So you can just call this function and the status will be updated in the external service.
>
> Implement a mechanism in your Django application that detects whenever the status of a CustomUser changes and, if so, calls ​sync_user_status()​ automatically.
>
> Nice to have:
> - as few DB hits as possible, but still
> - don’t call the external service when there is no ​status​ change.
>
> Constraints:
> - Django 3.X, Python 3.4+;
> - We do ​not​ want to use any other 3rd-party libraries.

Solution:
- Created the *`​CustomUser`* in the **`tasks/core/models.py`** file
- Implemented the `sync_user_status` function **`tasks/core/utils.py`** file
- Implemented the mechanism in the **`tasks/core/signals.py`** file
