import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from input_handler import get_parts_price
def test_get_parts_price():
    assert get_parts_price("iPhone", "screen") == 5000
    assert get_parts_price("iPhone", "battery") == 2500
    assert get_parts_price("Samsung", "screen") == 4000
    assert get_parts_price("Samsung", "battery") == 2000
    assert get_parts_price("Xiaomi", "screen") == 3000
    assert get_parts_price("Google Pixel", "screen") == 4500
    assert get_parts_price("Unknown", "screen") == 2500
    print("test_get_parts_price OK")
def test_get_parts_price_default():
    assert get_parts_price("iPhone", "unknown") == 3000
    print("test_get_parts_price_default OK")
if __name__ == "__main__":
    test_get_parts_price()
    test_get_parts_price_default()
    print("All tests passed")
