from src.day1 import main

def mock_get_input_lines():
    return ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

def test_main(monkeypatch):
    monkeypatch.setattr('src.day1.get_input_lines', mock_get_input_lines)
    
    assert main() == 142
