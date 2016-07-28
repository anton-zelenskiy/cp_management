<h2>Installation guide:</h2>

<h4>1) create and activate virtualenv:</h4>
<p>virtualenv -p=3.4.3 <venv_name></p>
<p>source <venv_name>/bin/activate</p>

<h4>2) clone project:</h4>
<p>git clone https://github.com/pahom-berdyansk/cp_management.git</p>

<h4>3) install dependencies:</h4>
<p>cd cp/management/CPManagement</p>
<p>run pip install -r requirements.txt</p>

<h4>4) create postgresql database:</h4>
     sudo -i -u postgres psql
     
<p>in psql console:</p>
<p>CREATE DATABASE myproject;</p>
<p>CREATE USER myprojectuser WITH PASSWORD 'password';</p>
<p>GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;</p>

<p>in settings.py add db configuration settings:</p>
<code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cp_management',
        'USER': 'cp_manager',
        'PASSWORD': '000000',
        'HOST': 'localhost',
        'PORT': '',
    }
}
</code>

<h4>4) run project:</h4>
<p>python manage.py migrate</p>
<p>python manage.py createsuperuser</p>
<p>python manage.py runserver</p>

<p>and go to http://127.0.0.1:8000/</p>
