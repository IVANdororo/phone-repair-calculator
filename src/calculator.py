from config import PRICES, URGENCY, PROMOCODES

PARTS_PRICES = {
    "iPhone": {"screen": 5000, "battery": 2500, "motherboard": 8000},
    "Samsung": {"screen": 4000, "battery": 2000, "motherboard": 7000},
    "Xiaomi": {"screen": 3000, "battery": 1500, "motherboard": 6000},
    "Google Pixel": {"screen": 4500, "battery": 2200, "motherboard": 7500},
    "Other": {"screen": 2500, "battery": 1200, "motherboard": 5000}
}

PARTS_ANALOG = {
    "iPhone": {"screen": 3500, "battery": 1800, "motherboard": 5000},
    "Samsung": {"screen": 3000, "battery": 1500, "motherboard": 4500},
    "Xiaomi": {"screen": 2500, "battery": 1200, "motherboard": 4000},
    "Google Pixel": {"screen": 3200, "battery": 1600, "motherboard": 4800},
    "Other": {"screen": 2000, "battery": 1000, "motherboard": 3500}
}

def calc_labor(model, repair):
    if model in PRICES:
        model_prices = PRICES[model]
    else:
        model_prices = PRICES["Other"]
    return model_prices.get(repair, 0)

def calc_total(data):
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
    
    return {
        "labor": labor,
        "parts": parts,
        "diagnostics": diagnostics,
        "services": services,
        "subtotal": subtotal,
        "multiplier": multiplier,
        "discount": discount,
        "total": total
    }

def compare_options(model, repair, urgency):
    original_parts = PARTS_PRICES.get(model, {}).get(repair, 3000)
    analog_parts = PARTS_ANALOG.get(model, {}).get(repair, 2000)
    
    labor = calc_labor(model, repair)
    
    if repair == "motherboard":
        diagnostics = 0
    else:
        diagnostics = 500
    
    multiplier = URGENCY[urgency]
    
    original_total = (labor + original_parts + diagnostics) * multiplier
    analog_total = (labor + analog_parts + diagnostics) * multiplier
    
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
