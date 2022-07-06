## PythonDocx

---

**Configuration** 

```
sudo apt install python3.7 python3-venv python3.7-venv
python3.7 -m venv envname

```
```
source envname/bin/activate
envname/bin/pip3.7 install -r requirements.txt

```
```
envname/bin/python3.7 create.py

```

---

**Tags** 

```
<PT %data path% >

```
we can use this tag to repalce texts using x path of data.

```
<TID %table id% >

```
we can assign a table id by adding this tag anywhere of the table. also we can use TID to specify the table id when we are doing some operations releated to tables.


```
<TUP %data path to update table% TID %table id% >

```

we can use this tag to update tables.
