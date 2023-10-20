This is all the code used to develop the Okayama Denim in-house application. 
Some files are not necessary for the application's functionality, so they are split into different folders.
- main: All the scripts necessary for the application to function
- template: The templates used for the application
- archive: All the code used within application development and testing

These are the instructions for accessing the application by code.
1. If you have not already installed python, please do. I used version 3.10.11 for the code, so make sure to install the same version. Here is the link to the installation: https://www.python.org/downloads/release/python-31011/
2. Download pip to install other libaries using ```python3 -m ensurepip --upgrade```
3. There are several python libraries I used to develop the app. Please install the following using the code provided on your terminal:  
```pip install ShopifyAPI```\
```pip install pandas```\
```pip install requests```\
```pip install PySimpleGUI```\
```pip install jinja2```
4. Once everything is installed, download everything in the Code folder of the github rep.
5. Run ```python3 GUI.py``` on the terminal and everything should work. If it does not work, it is likely that you need to provide the file path to GUI.py, so replace GUI.py with the file path.

Fulfillment Orders Rules
1. Add a p next to any order number that is a partial order (for now, these orders have to be done manually).
2. Add an e next to any order number that is an exchange.
3. Add a + between the order numbers for packages that have two or more orders being fulfilled.

Measurement Edit Rules
1. Table for the measurement must already be created within shopify
2. Copy and paste another table already written in google slides or excel for the program to work (I will try to add the other option)

