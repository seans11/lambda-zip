#
# README.txt
#

Install Notes
-------------
To install on local system point pip to directory with "setup.py" file.
pip3 install c:\python\lamzip

To update:
pip3 install c:\python\lamzip --upgrade

Important
---------
Ensure the python "Scripts" directory is located in your system path, as this library installs LamZip to that location
for global use.

*To verify path exists:*
Run "pip3 -V"
Use the version response to verify the interpreter location on your system:
pip 20.0.2 from c:\program files\python37\lib\site-packages\pip (python 3.7)

Run (Using BASH): "echo $PATH" to verify "<path-to-python-base>/scripts" exists
Run (Using PowerShell): "$ENV:$PATH" to verify "<path-to-python-base>\Scripts" exists

