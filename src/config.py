"""
Модуль конфигурации - цены и промокоды
"""

# Базовые цены на работы (руб.)
LABOR_PRICES = {
    "iPhone": {
        "screen": 2500,
        "battery": 1200,
        "motherboard": 4500,
        "charging_port": 1500,
        "buttons": 1000,
        "water_damage": 4000
    },
    "Samsung": {
        "screen": 2200,
        "battery": 1000,
        "motherboard": 4000,
        "charging_port": 1200,
        "buttons": 800,
        "water_damage": 3500
    },
    "Xiaomi": {
        "screen": 1800,
        "battery": 800,
        "motherboard": 3500,
        "charging_port": 1000,
        "buttons": 700,
        "water_damage": 3000
    },
    "Google Pixel": {
        "screen": 2400,
        "battery": 1100,
        "motherboard": 4200,
        "charging_port": 1300,
        "buttons": 900,
        "water_damage": 3800
    },
    "Other": {
        "screen": 1500,
        "battery": 700,
        "motherboard": 3000,
        "charging_port": 800,
        "buttons": 600,
        "water_damage": 2500
    }
}

# Коэффициенты срочности
URGENCY_RATES = {
    "normal": 1.0,
    "urgent": 1.3,
    "emergency": 1.5
}

# Дополнительные услуги
ADDITIONAL_SERVICES_PRICES = {
    "home_visit": 500,
    "protective_glass": 300
}

# Промокоды
PROMOCODES = {
    "SERVICE10": {
        "type": "total",
        "rate": 0.10,
        "description": "10% на общую сумму"
    },
    "REMONT26": {
        "type": "labor",
        "rate": 0.15,
        "description": "15% на стоимость работ"
    }
}
