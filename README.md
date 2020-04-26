
Install Notes
-------------
To install using pip:

```shell script
pip install lamzip
```

To update using pip:
```shell script
pip install lamzip --upgrade
```

Using LamZip
------------
#### Initial Project Setup
Create a defaults file in your project directory to simplify packaging:
```
lamzip make-config [--config-name .altname]
```
Just using `lamzip make-config` without any arguments will create the default
config file `.lamzip.yaml`.  Contained in the default config is an example
setup that looks like the following:
```yaml
# Lambda-Zip (lamzip)
#
# Defaults for packaging your AWS Lambda function
#

source-directory: ./appsrc
destination-directory: ./dist
package-prefix: foo
package-version: 0.0.1
```

#### Configure LamZip
Your project structure should look something like the following:
```
Main-Project-Folder\
   dist\
   appsrc\
      lib1\
      lib2\
      app.py
   .bumpversion
   .lamzip.yaml
   .gitignore
   LICENSE
   README
   requirements.txt
   setup.py
```

In this example you would use the following settings:<br>
`source-directory` to `./appsrc`<br>
`destination-directory` to `./dist` # the default is typically the case here<br>
`package-prefix` to `app` # zip file package name pre-pended to the version<br>
`package-version` to `0.0.1` # current app version

#### Run LamZip (Package your function)
Once configured, you can just run LamZip in the following way:
```
# lamzip use-config

LamZip using existing config file: .lamzip.yaml
  Source Dir: ./appsrc
  Destination Dir: ./dist
  Package Prefix: app
  Package Version: 0.0.1

Creating Archive: ./dist\app-0.0.1.zip
  adding: ./appsrc\app.py

``` 

#### Pass all parameters using CLI
It is not required to use the LamZip config file.  All arguments can be passed
using the CLI in the following way:
```shell script
lamzip specify --src-dir ./appsrc --dest-dir ./dist --zip-prefix app --zip-version 0.0.1
```

Integration
-----------
Now that you have the LamZip config deployed to your project folder it is
recommended to use a versioning utility like "Bumpversion" to easily maintain the version
configuration within the LamZip config file (.lamzip.yaml).<br>
https://github.com/peritus/bumpversion

Important
---------
Ensure the python "Scripts" directory is located in your system path, as this library
installs LamZip to that location for global use.

**Verify the path:**<br>
Use the version response to verify the interpreter location on your system.
```shell script
# pip3 -V

pip 20.0.2 from c:\program files\python37\lib\site-packages\pip (python 3.7)
```

```
Using BASH: "echo $PATH" to verify "<path-to-python-base>/scripts" exists
Using PowerShell: "$ENV:$PATH" to verify "<path-to-python-base>\Scripts" exists
```
