from setuptools import setup
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lamzip',
    version='0.4.1',
    author='Sean Sydow',
    description='A simple packaging utility that creates an AWS Lambda zip for distribution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['lamzip'],
    url='https://github.com/seans11/lambda-zip',
    license='MIT',
    author_email='',
    entry_points={'console_scripts': ['lamzip = lamzip.lamzip:main']},
    keywords=['aws', 'lambda', 'package', 'function', 'zip'],
)
