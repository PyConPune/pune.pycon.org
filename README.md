PyCon Pune 2018
===============

# Development Environment
To setup the development environment follow these steps:

1. First [install virtualenv](https://virtualenv.pypa.io/en/stable/installation/).
```bash
# For Ubuntu
sudo apt install python3-pip
pip3 install virtualenv

# For Fedora
sudo dnf install python3-pip
pip3 install virtualenv
```

2. Then create a virtualenv using
```bash
mkdir ~/.virtualenvs
virtualenv --python=`which python3` ~/.virtualenvs/pycon
```

3. Then activate this virtualenv, you have to do this everytime you start
   working on the project
```
source ~/.virtualenvs/pycon/bin/activate
```

4. To start working you need to check out the development branch
```
git clone https://github.com/PyConPune/pune.pycon.org.git
cd pune.pycon.org
git fetch
git checkout feature/django
```

5. To install Django and all the packages related to this project
```
pip install -r requirements.txt
```

6. Once all the packages are installed you will need to setup the django database:
```
python3 manage.py migrate
```

7. Running the django server:
```
python3 manage.py runserver
```

8. Visit `http://127.0.0.1:8000/` on your browser and start working
