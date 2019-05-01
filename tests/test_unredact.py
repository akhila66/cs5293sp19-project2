from project2 import unredactor
import glob
import pytest
import re,io
files = glob.glob("project2/train/pos/*.txt")
trainpath = "project2/train/pos/*.txt"
redactpath = "project2/test/redact/*.redactor"
def test_doextraction():
    returndata = unredactor.doextraction(trainpath)
    assert len(returndata) >= 0

def test_doprediction():
    trainData = unredactor.doextraction(trainpath)
    unredactor.doprediction(redactpath,trainData)
    unredactpath = "project2/test/unredact/*.unredactor"
    assert len(glob.glob(unredactpath)) == len(glob.glob(redactpath))