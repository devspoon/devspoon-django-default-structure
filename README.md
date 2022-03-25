# devspoon-django-default-structure
this repository is for base structure of django. settings.py files support for case of Local(dev), Test, Stage, Product .

# How to use
## export mode on console
Support mode
1. enter command "export DJANGO_SETTINGS_MODULE=django_basic.settings.dev"
2. enter command "export DJANGO_SETTINGS_MODULE=django_basic.settings.test"
3. enter command "export DJANGO_SETTINGS_MODULE=django_basic.settings.stage"
4. enter command "export DJANGO_SETTINGS_MODULE=django_basic.settings.prod"

## modify mode status
> manage.py and wsgi.py update comment like bellow

Development mode
- os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basic.settings.dev')

Test mode
-  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basic.settings.test')

Stage mode
-  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basic.settings.stage')

Product mode
-  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basic.settings.prod')