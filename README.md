Akhila Podupuganti:

My folder structure

                ├── COLLABORATORS
                ├── LICENSE
                ├── Pipfile
                ├── Pipfile.lock
                ├── project2
                │   ├── redactor.py
                │   ├── test
                │   │   ├── pos
                │   │   │   ├── 12173_9.txt
                │   │   │   ├── 12174_10.txt
                │   │   │       . . . . 
                │   │   ├── redact
                │   │   │   ├── 12173_9.redactor
                │   │   │   ├── 12174_10.redactor
                │   │   │   ├── . . . .
                │   │   ├── redact.stats
                │   │   └── unredact
                │   │       ├── 12173_9.unredactor
                │   │       ├── 12174_10.unredactor
                │   │           . . . .
                │   │ 
                │   ├── train
                │   │   └── pos
                │   │       ├── 12260_10.txt
                │   │       ├── 12261_10.txt
                │   │           . . . .
                │   └── unredactor.py
                ├── setup.cfg
                ├── setup.py
                ├── tests
                │   ├── test_redact.py
                │   └── test_unredact.py

There are two .py main files :

    - redactor.py one is for redacting the text test files from the path "test/pos/*.txt"  and save the redacted files into "test/redact" folder. it also gives the redact.stats file to give the satistics. 
    - and another one is unredactor.py which is to unredact the redacted files from "test/redact" folder, unredact the files by comparing the train features , return with top 4 likely names and save it onto "test/unredact" folder. 

How features are extracted from train data : 

    - considering three features (length of name, no. of words in each review, no of spaces) from train data
    - calculating the same for redacted test files and finding the most similar matches from it.

Constaraints :

    Make sure to place all the train data in train/pos folder and test in test/pos folder. And also the redact and unredact folders in test is also mandatory to have. Then only it will save the redacted and unredacted files into the resprective folders. 

How to execute the .py files :

    redactor.py : python redactor.py (I already hard coded the path inside the file). First this file ahs to   be run and then only unredactor will unredact the files from the redact folder.
    unredactor.py : python unredactor.py 'train/pos/*.txt' 

Test files for my project :

    There are two test files with total 4 test cases
    - test_redact.py (to test for redacting the files)
    - test_unredact.py (to test for predcting/unredacting/training)

How to run project with test :
    pipenv run python setup.py test