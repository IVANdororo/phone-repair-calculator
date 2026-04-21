import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import calc_labor, calc_total, compare_options

def test_calc_labor():
    assert calc_labor("iPhone", "screen") == 2500
    assert calc_labor("Samsung", "battery") == 1000
    assert calc_labor("Xiaomi", "motherboard") == 3500
    assert calc_labor("Unknown", "screen") == 1500
    print("test_calc_labor OK")

def test_calc_total():
    data = {
        "model": "iPhone",
        "repair": "screen",
        "parts": 5000,
        "urgency": "normal",
        "services": 0,
        "promocode": ""
    }
    result = calc_total(data)
    assert result["total"] == 8000
    print("test_calc_total OK")

def test_calc_total_with_urgency():
    data = {
        "model": "iPhone",
        "repair": "screen",
        "parts": 5000,
        "urgency": "urgent",
        "services": 0,
        "promocode": ""
    }
    result = calc_total(data)
    assert result["total"] == 10400
    print("test_calc_total_with_urgency OK")

def test_promocode_SERVICE10():
    data = {
        "model": "iPhone",
        "repair": "screen",
        "parts": 5000,
        "urgency": "normal",
        "services": 0,
        "promocode": "SERVICE10"
    }
    result = calc_total(data)
    assert result["total"] == 7200
    assert result["discount"] == 800
    print("test_promocode_SERVICE10 OK")


def test_promocode_REMONT26():
    data = {
        "model": "iPhone",
        "repair": "screen",
        "parts": 5000,
        "urgency": "normal",
        "services": 0,
        "promocode": "REMONT26"
    }
    result = calc_total(data)
    assert result["total"] == 7625
    assert result["discount"] == 375
    print("test_promocode_REMONT26 OK")


def test_compare_options():
    comp = compare_options("iPhone", "screen", "normal")
    assert comp["original"] == 11000
    assert comp["analog"] == 6500
    assert comp["best"] == "аналог"
    assert comp["savings"] == 4500
    print("test_compare_options OK")

def test_diagnostics():
    data = {
        "model": "iPhone",
        "repair": "motherboard",
        "parts": 5000,
        "urgency": "normal",
        "services": 0,
        "promocode": ""
    }
    result = calc_total(data)
    assert result["total"] == 9500
    print("test_diagnostics OK")

def test_services():
    data = {
        "model": "iPhone",
        "repair": "screen",
        "parts": 5000,
        "urgency": "normal",
        "services": 800,
        "promocode": ""
    }
    result = calc_total(data)
    assert result["total"] == 8800
    print("test_services OK")

def run_all_tests():
    test_calc_labor()
    test_calc_total()
    test_calc_total_with_urgency()
    test_promocode_SERVICE10()
    test_promocode_REMONT26()
    test_compare_options()
    test_diagnostics()
    test_services()
    print("\n" + "=" * 40)
    print("ALL TESTS PASSED")
    print("=" * 40)

if __name__ == "__main__":
    run_all_tests()
