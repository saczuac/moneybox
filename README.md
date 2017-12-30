# Six Counts Saver

A project in order to help people to take control and knowledge over their own expenses

## DEVELOP 

### Up & Running

#### Server

In the console run the following commands

+ Activate your virtualenv...
+ `pip install -r requirements.txt`
+ `cp moneybox/settings_env.example.py moneybox/settings_env.py`
+ `python manage.py migrate`
+ `python manage.py loaddata fixtures/algorithms.json`  **Not provided yet**
+ Create some users with: `python manage.py createsuperuser`
+ `python manage.py runserver`
+ You can go to [localhost](http://localhost:8000/admin) and do crud from here but it could be better if you use the existing client for this

#### Client

In the console run the following commands in order to develop

+ `python manage.py runserver`
+ `cd static/moneybox-client`
+ `npm install -g @angular/cli`
+ `npm install`
+ `ng serve --open`
