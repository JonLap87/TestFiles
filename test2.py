import requests
import pytest
from main import langs

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids_resul = {98, 35, 15, 213, 54, 119}


class TestVisit:
    def test_task1(self):
        result = len(langs(ids))
        assert result == len (ids_resul)