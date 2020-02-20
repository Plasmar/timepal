from setuptools import setup

setup(
    name='timepal',
    version='0.1',
    py_modules=['timepal'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        timepal=timepal:cli
    ''',
)

