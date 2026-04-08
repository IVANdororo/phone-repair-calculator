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
