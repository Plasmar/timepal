from setuptools import setup

setup(
    name='timepal',
    version='0.1',
    py_modules=['timepal'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        timepal=timepal:cli
    ''',
)
