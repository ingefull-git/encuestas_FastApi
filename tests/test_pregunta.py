from unittest import mock, TestCase
from app.models import Pregunta
from fastapi.testclient import TestClient



class Test_Pregunta(TestClient):
    
    def setUp(self):
        self.preg1 = Pregunta(1, 'Color favorito?')
    
    def test_pregunta_1(self):
        assert self.preg1.nombre == str
        