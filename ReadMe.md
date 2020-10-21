# DirctLineApplication
Name: Simple Rest App
Introduction:
This projects aims to create a simple app in Flask using Python 3 
It Returns sum of Numbers  provided in python List into total in Json format.
For simplicity purpose the range is hardcoded.using range function to create a python List of numbers
The url to access is http://127.0.0.1:5000/total

Prerequisites:
Python >= 3.6
create virtual environment python -m venv env
Activate env : source .env\Scripts\Activate.bat
Install the Python modules : pip install -r requirements.txt
Run:
Go to {ProjectDir}/
python app.py
Access http://127.0.0.1:5000/total
Testing:
python -m pytest

Requiments consideration:
I used default python Sum function to sum of numbers in List,
we can do same in multiple ways such as
using for loop,
or python lambda expresions etc.
but default option  was already optimzed.

