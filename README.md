** Obsolete - No longer in use. **

# AM-Traffic-Portal
Django project to create AM-Traffic-Portal user-interface.

Use Python 3.6 or similar version.

## Installation

Installation to development:

```sh
# Linux installation
sudo apt-get install python3 python3-pip virtualenvwrapper
# Python installation
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
# Run the development server with manage.py
python3 manage.py runserver 0.0.0.0:8080
# Keep requirements.txt up-to-date
pip freeze > requirements.txt
```

Installation to production:

```sh
TODO: Document all the steps.
```

## Usage

Access the user-interface http://13.53.204.251:8080/app/ (use IP address of the server).
