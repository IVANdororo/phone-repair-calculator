from config import PRICES, URGENCY, PROMOCODES
from logger import log_start, log_input, log_result, log_error
from receipt import print_receipt

LABOR_PRICES = PRICES

PARTS_PRICES = {
    "iPhone": {"screen": 5000, "battery": 2500, "motherboard": 8000, "charging_port": 1500, "buttons": 800, "water_damage": 0},
    "Samsung": {"screen": 4000, "battery": 2000, "motherboard": 7000, "charging_port": 1200, "buttons": 700, "water_damage": 0},
    "Xiaomi": {"screen": 3000, "battery": 1500, "motherboard": 6000, "charging_port": 1000, "buttons": 600, "water_damage": 0},
    "Google Pixel": {"screen": 4500, "battery": 2200, "motherboard": 7500, "charging_port": 1300, "buttons": 750, "water_damage": 0},
    "Other": {"screen": 2500, "battery": 1200, "motherboard": 5000, "charging_port": 800, "buttons": 500, "water_damage": 0}
}

PARTS_ANALOG = {
    "iPhone": {"screen": 3500, "battery": 1800, "motherboard": 5000, "charging_port": 1000, "buttons": 500, "water_damage": 0},
    "Samsung": {"screen": 3000, "battery": 1500, "motherboard": 4500, "charging_port": 800, "buttons": 450, "water_damage": 0},
    "Xiaomi": {"screen": 2500, "battery": 1200, "motherboard": 4000, "charging_port": 700, "buttons": 400, "water_damage": 0},
    "Google Pixel": {"screen": 3200, "battery": 1600, "motherboard": 4800, "charging_port": 900, "buttons": 500, "water_damage": 0},
    "Other": {"screen": 2000, "battery": 1000, "motherboard": 3500, "charging_port": 600, "buttons": 350, "water_damage": 0}
}

REPAIR_LIST = ["Замена экрана", "Замена аккумулятора", "Ремонт материнской платы", "Замена разъема зарядки", "Ремонт кнопок", "Восстановление после воды"]
REPAIR_KEYS = ["screen", "battery", "motherboard", "charging_port", "buttons", "water_damage"]

MODEL_LIST = ["iPhone", "Samsung", "Xiaomi", "Google Pixel", "Другие"]
MODEL_KEYS = ["iPhone", "Samsung", "Xiaomi", "Google Pixel", "Other"]

URGENCY_LIST = ["Обычный", "Срочный (+30%)", "Экстренный (+50%)"]
URGENCY_KEYS = ["normal", "urgent", "emergency"]
URGENCY_VALUES = [1.0, 1.3, 1.5]

PARTS_TYPE_LIST = ["Оригинал", "Аналог"]

def get_model_key(name):
    for i, n in enumerate(MODEL_LIST):
        if n == name:
            return MODEL_KEYS[i]
    return "Other"

def get_repair_key(name):
    for i, n in enumerate(REPAIR_LIST):
        if n == name:
            return REPAIR_KEYS[i]
    return "screen"

def get_urgency_value(name):
    for i, n in enumerate(URGENCY_LIST):
        if n == name:
            return URGENCY_VALUES[i]
    return 1.0

def get_urgency_key(name):
    for i, n in enumerate(URGENCY_LIST):
        if n == name:
            return URGENCY_KEYS[i]
    return "normal"

def get_model():
    print("\nВыберите модель телефона:")
    for i, model in enumerate(MODEL_LIST, 1):
        print(f"{i}. {model}")
    
    while True:
        try:
            choice = int(input("Введите номер (1-5): "))
            if 1 <= choice <= len(MODEL_LIST):
                return MODEL_LIST[choice - 1]
            print("Ошибка: введите число от 1 до 5")
        except ValueError:
            print("Ошибка: введите число")

def get_repair():
    print("\nВыберите тип ремонта:")
    for i, repair in enumerate(REPAIR_LIST, 1):
        print(f"{i}. {repair}")
    
    while True:
        try:
            choice = int(input("Введите номер (1-6): "))
            if 1 <= choice <= len(REPAIR_LIST):
                return REPAIR_LIST[choice - 1]
            print("Ошибка: введите число от 1 до 6")
        except ValueError:
            print("Ошибка: введите число")

def get_parts_type():
    print("\nВыберите тип запчасти:")
    for i, ptype in enumerate(PARTS_TYPE_LIST, 1):
        print(f"{i}. {ptype}")
    
    while True:
        try:
            choice = int(input("Введите номер (1-2): "))
            if 1 <= choice <= len(PARTS_TYPE_LIST):
                return PARTS_TYPE_LIST[choice - 1]
            print("Ошибка: введите число от 1 до 2")
        except ValueError:
            print("Ошибка: введите число")

def get_urgency():
    print("\nВыберите срочность:")
    for i, urgency in enumerate(URGENCY_LIST, 1):
        print(f"{i}. {urgency}")
    
    while True:
        try:
            choice = int(input("Введите номер (1-3): "))
            if 1 <= choice <= len(URGENCY_LIST):
                return URGENCY_LIST[choice - 1]
            print("Ошибка: введите число от 1 до 3")
        except ValueError:
            print("Ошибка: введите число")

def get_services():
    print("\nДополнительные услуги:")
    visit = input("Выезд мастера (+500 руб)? (y/n): ").lower()
    glass = input("Защитное стекло (+300 руб)? (y/n): ").lower()
    
    total = 0
    if visit == 'y':
        total += 500
    if glass == 'y':
        total += 300
    return total

def get_promocode():
    return input("Введите промокод (или Enter): ").strip().upper()

def calculate_total():
    model_name = get_model()
    model = get_model_key(model_name)
    
    repair_name = get_repair()
    repair = get_repair_key(repair_name)
    
    parts_type = get_parts_type()
    
    if repair == "water_damage":
        parts = 0
        print("\nЗапчасти не требуются")
    else:
        if parts_type == "Оригинал":
            parts = PARTS_PRICES.get(model, {}).get(repair, 3000)
        else:
            parts = PARTS_ANALOG.get(model, {}).get(repair, 2000)
        print(f"\nСтоимость запчасти: {parts} руб")
    
    labor = LABOR_PRICES.get(model, {}).get(repair, 1500)
    print(f"Стоимость работы: {labor} руб")
    
    diagnostics = 0 if repair == "motherboard" else 500
    if diagnostics > 0:
        print(f"Диагностика: {diagnostics} руб")
    
    services = get_services()
    if services > 0:
        print(f"Услуги: {services} руб")
    
    urgency_name = get_urgency()
    urgency = get_urgency_key(urgency_name)
    multiplier = get_urgency_value(urgency_name)
    
    promocode = get_promocode()
    
    subtotal = labor + parts + diagnostics + services
    total = subtotal * multiplier
    
    discount = 0
    if promocode == "SERVICE10":
        discount = total * 0.10
        total = total - discount
        print(f"Промокод SERVICE10: скидка 10% ({discount} руб)")
    elif promocode == "REMONT26":
        discount = labor * 0.15
        total = total - discount
        print(f"Промокод REMONT26: скидка 15% на работу ({discount} руб)")
    
    print("\n" + "=" * 40)
    print("           ЧЕК")
    print("=" * 40)
    print(f"Модель: {model_name}")
    print(f"Ремонт: {repair_name}")
    print(f"Тип запчасти: {parts_type}")
    print("-" * 40)
    print(f"Стоимость работы:     {labor} руб")
    print(f"Стоимость запчасти:   {parts} руб")
    print(f"Диагностика:          {diagnostics} руб")
    print(f"Услуги:               {services} руб")
    print(f"Срочность:            {urgency_name}")
    print(f"Коэффициент:          x{multiplier}")
    if discount > 0:
        print(f"Скидка:               -{discount} руб")
    print("-" * 40)
    print(f"ИТОГО К ОПЛАТЕ:       {total:.2f} руб")
    print("=" * 40)
    print("Спасибо за обращение!")

def main():
    try:
        log_start()
        calculate_total()
    except Exception as e:
        log_error(str(e))
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
