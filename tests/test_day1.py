from src.day1 import main

def mock_get_input_lines():
    return ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

def test_main(monkeypatch):
    monkeypatch.setattr('src.day1.get_input_lines', mock_get_input_lines)
    
    assert main() == 281
