# Auto Email Teachers When Your Away
A simple program that emails teachers (or anyone else) based on what classes you have on the current day  
Currently gets recipent list from a CSV file but later will get the info from a webpage and cross reference classes with teachers to determine recipents  
- MS Exchange mail
- Reads webpage

# Required Libraries/Packages
- CSV (built in)
- [Exchangelib](https://pypi.org/project/exchangelib/)
- [Maskpass](https://pypi.org/project/maskpass/)
- [DearPyGUI](https://pypi.org/project/dearpygui/)

# Website Link
- https://apcom.tjh5.co/

# Usage
## Installation
1. Download repo
2. Extract files
3. Install [Python](https://www.python.org/downloads/)  
```https://www.python.org/downloads/```
4. Install required packages  
```pip install -r requirements.txt```  
5. coming soon...


# To-do
- [x] Send emails with Exchange
  - [x] Connect to MS Exchange email
  - [x] Customise emails based on recipent
- [x] Email list of people
  - [x] Read emails from CSV (temp)
  - [ ] ~~Scrape class info from simon/LMS~~
- [x] Add GUI
  - [x] Half decent GUI
  - [x] Customise Subject
  - [x] Customise Body

# Credits
- Me 
- 04Roberto
- Chanetic