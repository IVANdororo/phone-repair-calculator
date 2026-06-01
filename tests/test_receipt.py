import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from receipt import print_receipt
def test_print_receipt():
    data = {
        "model": "iPhone",
        "repair": "screen",
        "parts": 5000,
        "urgency": "normal",
        "services": 0,
        "promocode": ""
    }
    result = {
        "labor": 2500,
        "parts": 5000,
        "diagnostics": 500,
        "services": 0,
        "subtotal": 8000,
        "multiplier": 1.0,
        "discount": 0,
        "total": 8000
    }
    print_receipt(data, result)
    print("test_print_receipt OK")
if __name__ == "__main__":
    test_print_receipt()
    print("All tests passed")
