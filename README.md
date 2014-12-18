# amenu

This is a menu plugins for DjangoCMS. It provides 4 different kinds of menu plugins.

1. Menu Below Current Page
2. Breadcrumb
3. Generic Menu
4. Selective Menu

# Installation
1. Download the package
````
$ pip install amenu
````

2. Register it to the INSTALLED_APPS
2.1. For standard DjangoCMS project setting
````
INSTALLED_APPS = (
    'amenu',
)
````
2.2. For [Djangocms Foundation](https://github.com/ludbek/djangocms-foundation)
````
DJANGO_CMS_APPS = (
    'amenu',
)
````
3. Migrate the plugin
````
$ python manage.py migrate amenu
````
