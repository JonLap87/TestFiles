import yadisk
import requests
import pytest
from main import y


y = yadisk.YaDisk(token="y0_AgAAAABtQNFaAAoFNwAAAADk6-VddQOjr9lpQNOlxCJpr-4ieacevKA")
y.remove("text.txt", permanently=True)
y.upload("text.txt", "/text.txt")
resul = y.mkdir("New")

class TestVisit:
    def test_task1(self):
        result = len(y())
        assert result == len (resul)
