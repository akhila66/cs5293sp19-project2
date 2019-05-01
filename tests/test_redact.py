from project2 import redactor
import pytest
import glob
files = glob.glob("tests/*.txt")
file1 = open("project2/test/pos/0_10.txt","r+") 
data = file1.read() 
# path = "*.txt"
print(file1)
def test_get_entity():
    returndata = redactor.get_entity(data)
    assert returndata == ['Ashton', 'Kutcher', 'Jake Fischer', 'Kevin Costner', 'Ben Randall']
    assert len(returndata) == 5
def test_doredact():
    datatoredact = redactor.get_entity(data)
    redactedtext = redactor.doredact(datatoredact,data)
    assert type(redactedtext) == str