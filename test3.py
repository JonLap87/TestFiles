import requests
import pytest
from main import max_val

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

stats_resul = ('yandex')

class TestVisit:
    def test_task1(self):
        result = len(max_val(stats))
        assert result == len (stats_resul)