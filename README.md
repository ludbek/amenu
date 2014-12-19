````python
amenu
    This is a menu plugins for DjangoCMS. It provides 4 different kinds of menu plugins.
    1. Menu Below Current Page
    2. Breadcrumb
    3. Generic Menu
    4. Selective Menu

Installation
    Download the package
        $ pip install amenu
    Register it to the INSTALLED_APPS
        For standard DjangoCMS project setting
            INSTALLED_APPS = (
                'amenu',
            )

        For "Djangocms Foundation"[https://github.com/ludbek/djangocms-foundation]
            DJANGO_CMS_APPS = (
            'amenu',
            )
    Migrate the plugin
        $ python manage.py migrate amenu
        
TODO
    - Test in Python 3
    - Add Multiple Selective Menu
````
