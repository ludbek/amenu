from distutils.core import setup

setup(
    name='amenu',
    version='1.0.1',
    author='ludbek',
    author_email='sth.srn@gmail.com',
    packages= ['amenu', 'amenu.migrations', 'amenu.templatetags'],
    scripts=[],
    url='https://github.com/ludbek/amenu',
    license='LICENSE.txt',
    description='A menu plugin for DjangoCMS.',
    long_description=open('README.md').read(),
    install_requires=[
        "South == 1.0.1",
        "django-cms >= 3.0.7",
        "django-classy-tags == 0.5.2",
    ],
    include_package_data=True,
)
