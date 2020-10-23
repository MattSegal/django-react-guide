# Example code for a Django / React guide 

Example code for a Django / React [setup guide](https://mattsegal.dev/django-react.html)

This branch represents the project with a minimal Webpack setup, but no React or Babel yet.

## Setup instructions

```bash
# Enter Django project folder
cd backend
# Setup and activate virtualenv
virtualenv env
. env/bin/activate
# Install requirements
pip install -r requirements.txt
# Setup Django
./manage.py migrate
./manage.py runserver
# Then visit http://localhost:8000
```
