import pytest
from unittest.mock import patch
import lab_02 as app 

def test_add_element():
    """Тест додавання нового студента"""
    app.student_list.clear()
    inputs = ["TestUser", "123456", "01.01.2000", "TestSurname"]
    with patch('builtins.input', side_effect=inputs):
        app.addNewElement()
    assert len(app.student_list) == 1
    assert app.student_list[0]["name"] == "TestUser"
    assert app.student_list[0]["surname"] == "TestSurname"

def test_delete_element():
    """Тест видалення студента"""
    app.student_list = [{"name": "DeleteMe", "phone": "000", "birthday": "01.01", "surname": "None"}]
    with patch('builtins.input', return_value="DeleteMe"):
        app.deleteElement()
    assert len(app.student_list) == 0

def test_update_element():
    """Тест оновлення телефону"""
    app.student_list = [{"name": "UpdateMe", "phone": "111", "birthday": "01.01", "surname": "None"}]
    
    inputs = ["UpdateMe", "999"]
    
    with patch('builtins.input', side_effect=inputs):
        app.changeElement()
        
    assert app.student_list[0]["phone"] == "999"