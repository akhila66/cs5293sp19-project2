from project2 import redactor
import pytest
import glob
path = "project2/test/pos/*.txt"
files = glob.glob(path)
file1 = open("project2/test/pos/12174_10.txt","r+") 
data = file1.read() 
# path = "*.txt"
print(file1)
def test_get_entity():
    returndata = redactor.get_entity(data)
    assert returndata == ['Erkan', 'Stefan']
    assert len(returndata) == 2
def test_doredact():
    redactedtext = redactor.doredact(path)
    assert redactedtext == True