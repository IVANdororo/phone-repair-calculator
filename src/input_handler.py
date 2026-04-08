def get_model():
    """Спрашиваем модель телефона"""
    print("\nВыберите модель:")
    print("1. iPhone")
    print("2. Samsung")
    print("3. Xiaomi")
    print("4. Google Pixel")
    print("5. Другое")
    
    choice = input("Введите номер (1-5): ")
    
    if choice == "1":
        return "iPhone"
    elif choice == "2":
        return "Samsung"
    elif choice == "3":
        return "Xiaomi"
    elif choice == "4":
        return "Google Pixel"
    else:
        return "Other"

def get_repair():
    """Спрашиваем тип ремонта"""
    print("\nВыберите тип ремонта:")
    print("1. Замена экрана")
    print("2. Замена аккумулятора")
    print("3. Ремонт материнской платы")
    
    choice = input("Введите номер (1-3): ")
    
    if choice == "1":
        return "screen"
    elif choice == "2":
        return "battery"
    else:
        return "motherboard"

def get_parts():
    """Спрашиваем стоимость запчастей"""
    cost = input("Введите стоимость запчастей (руб): ")
    return float(cost)

def get_urgency():
    """Спрашиваем срочность"""
    print("\nСрочность:")
    print("1. Обычный (3-5 дней)")
    print("2. Срочный (1 день, +30%)")
    print("3. Экстренный (2-4 часа, +50%)")
    
    choice = input("Введите номер (1-3): ")
    
    if choice == "1":
        return "normal"
    elif choice == "2":
        return "urgent"
    else:
        return "emergency"

def get_services():
    """Спрашиваем доп услуги"""
    print("\nДополнительные услуги:")
    
    visit = input("Выезд мастера? (+500 руб) (y/n): ")
    glass = input("Защитное стекло? (+300 руб) (y/n): ")
    
    total = 0
    if visit == "y":
        total = total + 500
    if glass == "y":
        total = total + 300
    
    return total

def get_promocode():
    """Спрашиваем промокод"""
    code = input("Введите промокод (или Enter): ")
    return code

def get_all_data():
    """Собираем все данные"""
    print("=" * 40)
    print("КАЛЬКУЛЯТОР РЕМОНТА ТЕЛЕФОНА")
    print("=" * 40)
    
    data = {
        "model": get_model(),
        "repair": get_repair(),
        "parts": get_parts(),
        "urgency": get_urgency(),
        "services": get_services(),
        "promocode": get_promocode()
    }
    return data
