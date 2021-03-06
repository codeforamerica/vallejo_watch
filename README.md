# VallejoWatch
View, create, and manage quality of life issues.

### Status
In development

### Getting started

##### 1. Setting up virtual environment
See [here](https://github.com/codeforamerica/howto/blob/master/Python-Virtualenv.md) for details.

##### 2. Install dependencies
`pip install -r requirements.txt`

##### 3. Collect static files
`python manage.py collectstatic`

##### 4. Setup database and create superuser
`python manage.py syncdb` (this will prompt you to create a new superuser)

##### 5. Initialize local server
`python manage.py runserver`

##### 6. Set your Google API key
Follow [these](https://developers.google.com/maps/documentation/geocoding/?csw=1#api_key) instructions for obtaining an API key if you don't already have one.

Add your API key for your Google Developer account to a file named `.google_api_key` for geocoding addresses.

##### 7. Add or modify quality of life issues
http://127.0.0.1:8000/admin/visualize/incident/

##### 8. View quality of life issues
http://127.0.0.1:8000/
