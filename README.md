These are the instructions for accessing the application.
1. If you have not already installed python, please do. I used version 3.10.11 for the code, so make sure to install the same version. Here is the link to the installation: https://www.python.org/downloads/release/python-31011/
2. Download pip to install other libaries using ```python -m ensurepip --upgrade```
3. There are several python libraries I used to develop the app. Please install the following using the code provided on your terminal:  
```pip install ShopifyAPI```\
```pip install pandas```\
```pip install requests```\
```pip install PySimpleGUI```\
```pip install jinja2```
If an error occurs during the installation 
4. Once everything is installed, download everything in the github rep aside from the README.md file.
5. Run ```python GUI.py``` on the terminal and everything should work. If it does not work, it is likely that you need to provide the file path to GUI.py, so replace GUI.py with the file path.

Fulfillment Orders Rules
1. Add a p next to any order number that is a partial order (for now, these orders have to be done manually).
2. Add an e next to any order number that is an exchange.
3. Add a + between the order numbers for packages that have two or more orders being fulfilled.
