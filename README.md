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

##### 4. Create initial superuser
`django-admin.py createsuperuser`

##### 5. Initialize local server
`python manage.py runserver`

##### 6. Set you Google API key
Add your the API key for your Google Developer account to a file named `.googleapikey`.

##### 7. Add or modify quality of life issues
http://127.0.0.1:8000/admin/visualize/incident/

##### 8. View quality of life issues
http://127.0.0.1:8000/
