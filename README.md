Installation guide:

1) create and activate virtualenv:
virtualenv -p=3.4.3 <venv_name>
source <venv_name>/bin/activate

2) clone project:
git clone https://github.com/pahom-berdyansk/cp_management.git

3) install dependencies:
cd cp/management/CPManagement
run pip install -r requirements.txt

4) create postgresql database:
     sudo -i -u postgres psql
     in psql console:

CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

in settings.py add db configuration settings:
DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': 'myproject',
  'USER': 'myprojectuser',
  'PASSWORD': 'password',
  'HOST': 'localhost',
  'PORT': '',
  }
}

4) run project:
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

and go to http://127.0.0.1:8000/
