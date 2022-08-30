# How to contribute

### First setup
* Clone repository:
```
git clone git@github.com:MSoftwaree/modbus-history-chart.git
```
* Create a virtualenv:
```
python -m virtualenv virtualenv
```
* Activate virtualenv:
```
venv\Scripts\actibate.bat
```
* Install requirements:
```
pip install -r requirements.txt
```

#
### Working
* Create new branch:
```
git checkout -b branch_name
```
* Add local changes:
```
git add file_name.py
```
* Commit your changes:
```
git commit -m "comments"
```
* Push your changes:
```
git push 
```
* Create a merge request

#
### Packing to exe
* Use following template to create the executable file:
```
pyinstaller -n Modbus-history-chart --noconsole --onefile GUI\main.py
```