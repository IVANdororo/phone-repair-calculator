def compare_options(model, repair, urgency):
    """Сравниваем оригинал и аналог, возвращаем лучший вариант"""
    
    # Цены на оригинальные запчасти (руб)
    original_parts = {
        "iPhone": 8000,
        "Samsung": 6000,
        "Xiaomi": 4500,
        "Google Pixel": 7000,
        "Other": 5000
    }
    
    # Цены на аналоги (руб)
    analog_parts = {
        "iPhone": 3500,
        "Samsung": 3000,
        "Xiaomi": 2500,
        "Google Pixel": 3200,
        "Other": 2500
    }
    
    # Стоимость работы
    labor = calc_labor(model, repair)
    
    # Диагностика
    if repair == "motherboard":
        diagnostics = 0
    else:
        diagnostics = 500
    
    # Коэффициент срочности
    multiplier = URGENCY[urgency]
    
    # Считаем два варианта
    original_total = (labor + original_parts.get(model, 5000) + diagnostics) * multiplier
    analog_total = (labor + analog_parts.get(model, 2500) + diagnostics) * multiplier
    
    # Определяем лучший
    if original_total <= analog_total:
        best = "оригинал"
        best_price = original_total
        savings = analog_total - original_total
    else:
        best = "аналог"
        best_price = analog_total
        savings = original_total - analog_total
    
    return {
        "original": original_total,
        "analog": analog_total,
        "best": best,
        "best_price": best_price,
        "savings": savings
    }
