from config import PRICES, URGENCY, PROMOCODES

def calc_labor(model, repair):
    """Считаем стоимость работы"""
    if model in PRICES:
        model_prices = PRICES[model]
    else:
        model_prices = PRICES["Other"]
    
    return model_prices.get(repair, 0)

def calc_total(data):
    """Главная функция расчета"""
    
    model = data["model"]
    repair = data["repair"]
    parts = data["parts"]
    urgency = data["urgency"]
    services = data["services"]
    promocode = data["promocode"]
    
    labor = calc_labor(model, repair)
    
    if repair == "motherboard":
        diagnostics = 0
    else:
        diagnostics = 500
    
    subtotal = labor + parts + diagnostics + services
    
    multiplier = URGENCY[urgency]
    total = subtotal * multiplier
    
    discount = 0
    if promocode == "SERVICE10":
        discount = total * 0.10
        total = total - discount
    elif promocode == "REMONT26":
        discount = labor * 0.15
        total = total - discount
    
    result = {
        "labor": labor,
        "parts": parts,
        "diagnostics": diagnostics,
        "services": services,
        "subtotal": subtotal,
        "multiplier": multiplier,
        "discount": discount,
        "total": total
    }
    
    return result

def compare_options(model, repair, urgency):
    """Сравниваем оригинал и аналог"""
    
    original_parts = {
        "iPhone": 8000,
        "Samsung": 6000,
        "Xiaomi": 4500,
        "Google Pixel": 7000,
        "Other": 5000
    }
    
    analog_parts = {
        "iPhone": 3500,
        "Samsung": 3000,
        "Xiaomi": 2500,
        "Google Pixel": 3200,
        "Other": 2500
    }
    
    labor = calc_labor(model, repair)
    
    if repair == "motherboard":
        diagnostics = 0
    else:
        diagnostics = 500
    
    multiplier = URGENCY[urgency]
    
    original_total = (labor + original_parts.get(model, 5000) + diagnostics) * multiplier
    analog_total = (labor + analog_parts.get(model, 2500) + diagnostics) * multiplier
    
    if original_total <= analog_total:
        best = "оригинал"
        savings = analog_total - original_total
    else:
        best = "аналог"
        savings = original_total - analog_total
    
    return {
        "original": original_total,
        "analog": analog_total,
        "best": best,
        "savings": savings
    }
