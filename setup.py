from setuptools import setup

setup(
    name='lamzip',
    version='0.3.7',
    author='Sean Sydow',
    description='A simple packaging utility that creates an AWS Lambda zip for distribution',
    packages=['lamzip'],
    url='https://github.com/seans11/lambda-zip',
    license='MIT',
    author_email='',
    entry_points={'console_scripts': ['lamzip = lamzip.lamzip:main']},
    keywords=['aws', 'lambda', 'package', 'function', 'zip'],
)
