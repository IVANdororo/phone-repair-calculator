import tkinter as tk
from tkinter import ttk
from calculator import calc_total, compare_options
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

LABOR_PRICES = {
    "iPhone": {"screen": 2500, "battery": 1200, "motherboard": 4500},
    "Samsung": {"screen": 2200, "battery": 1000, "motherboard": 4000},
    "Xiaomi": {"screen": 1800, "battery": 800, "motherboard": 3500},
    "Google Pixel": {"screen": 2400, "battery": 1100, "motherboard": 4200},
    "Other": {"screen": 1500, "battery": 700, "motherboard": 3000}
}

MODEL_LIST = ["iPhone", "Samsung", "Xiaomi", "Google Pixel", "Другие"]
MODEL_KEYS = ["iPhone", "Samsung", "Xiaomi", "Google Pixel", "Other"]

REPAIR_LIST = ["Замена экрана", "Замена аккумулятора", "Ремонт материнской платы"]
REPAIR_KEYS = ["screen", "battery", "motherboard"]

URGENCY_LIST = ["Обычный", "Срочный (+30%)", "Экстренный (+50%)"]
URGENCY_KEYS = ["normal", "urgent", "emergency"]
URGENCY_VALUES = [1.0, 1.3, 1.5]

PARTS_TYPE_LIST = ["Оригинал", "Аналог"]
PARTS_TYPE_KEYS = ["original", "analog"]


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


def update_parts(*args):
    model_name = model_var.get()
    model = get_model_key(model_name)
    repair_name = repair_var.get()
    repair = get_repair_key(repair_name)
    parts_type = parts_type_var.get()

    if parts_type == "Оригинал":
        price = PARTS_PRICES.get(model, {}).get(repair, 3000)
    else:
        price = PARTS_ANALOG.get(model, {}).get(repair, 2000)

    parts_var.set(f"{price} руб")
    return price


def update_labor(*args):
    model_name = model_var.get()
    model = get_model_key(model_name)
    repair_name = repair_var.get()
    repair = get_repair_key(repair_name)
    price = LABOR_PRICES.get(model, {}).get(repair, 1500)
    labor_var.set(f"{price} руб")


def calculate():
    try:
        model_name = model_var.get()
        model = get_model_key(model_name)
        repair_name = repair_var.get()
        repair = get_repair_key(repair_name)
        urgency_name = urgency_var.get()
        urgency = get_urgency_key(urgency_name)
        parts_type = parts_type_var.get()

        if parts_type == "Оригинал":
            parts = PARTS_PRICES.get(model, {}).get(repair, 3000)
        else:
            parts = PARTS_ANALOG.get(model, {}).get(repair, 2000)

        labor = LABOR_PRICES.get(model, {}).get(repair, 1500)

        diagnostics = 0 if repair == "motherboard" else 500

        services = 0
        if home_visit_var.get():
            services += 500
        if glass_var.get():
            services += 300

        promocode = promo_var.get()

        subtotal = labor + parts + diagnostics + services
        multiplier = get_urgency_value(urgency_name)
        total = subtotal * multiplier

        discount = 0
        if promocode == "SERVICE10":
            discount = total * 0.10
            total = total - discount
        elif promocode == "REMONT26":
            discount = labor * 0.15
            total = total - discount

        comparison = compare_options(model, repair, urgency)

        selected_text = f"ВЫБРАНО: {parts_type}"

        result_label.config(
            text=f"{selected_text}\n\n"
                 f"Стоимость работы: {labor} руб\n"
                 f"Стоимость запчасти: {parts} руб\n"
                 f"Диагностика: {diagnostics} руб\n"
                 f"Услуги: {services} руб\n"
                 f"Коэффициент срочности: {multiplier}\n"
                 f"Скидка: {discount} руб\n"
                 f"ИТОГО: {total:.2f} руб\n\n"
                 f"Для сравнения:\n"
                 f"Оригинал: {comparison['original']:.2f} руб\n"
                 f"Аналог: {comparison['analog']:.2f} руб\n"
                 f"Рекомендация: {comparison['best']}\n"
                 f"Экономия: {comparison['savings']:.2f} руб",
            fg="black"
        )

        total_label.config(text=f"ИТОГО К ОПЛАТЕ: {total:.2f} руб", fg="red", font=("Arial", 16, "bold"))

    except Exception as e:
        result_label.config(text=f"Ошибка: {e}", fg="red")
        total_label.config(text="")


window = tk.Tk()
window.title("Калькулятор ремонта телефона")
window.geometry("480x800")
window.configure(bg="#f0f0f0")

main_frame = tk.Frame(window, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(main_frame, text="Модель телефона", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))
model_var = tk.StringVar(value="iPhone")
model_menu = ttk.Combobox(main_frame, textvariable=model_var, values=MODEL_LIST, state="readonly", width=35)
model_menu.pack(fill="x", pady=(0, 10))
model_menu.bind("<<ComboboxSelected>>", lambda e: (update_parts(), update_labor()))

tk.Label(main_frame, text="Тип ремонта", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))
repair_var = tk.StringVar(value="Замена экрана")
repair_menu = ttk.Combobox(main_frame, textvariable=repair_var, values=REPAIR_LIST, state="readonly", width=35)
repair_menu.pack(fill="x", pady=(0, 10))
repair_menu.bind("<<ComboboxSelected>>", lambda e: (update_parts(), update_labor()))

tk.Label(main_frame, text="Тип запчасти", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))
parts_type_var = tk.StringVar(value="Оригинал")
parts_type_menu = ttk.Combobox(main_frame, textvariable=parts_type_var, values=PARTS_TYPE_LIST, state="readonly",
                               width=35)
parts_type_menu.pack(fill="x", pady=(0, 10))
parts_type_menu.bind("<<ComboboxSelected>>", update_parts)

tk.Label(main_frame, text="Стоимость запчасти", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))
parts_var = tk.StringVar(value="5000 руб")
parts_label = tk.Label(main_frame, textvariable=parts_var, font=("Arial", 11), bg="#ffffff", relief="sunken",
                       anchor="w")
parts_label.pack(fill="x", pady=(0, 10), ipady=5)

tk.Label(main_frame, text="Стоимость работы", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))
labor_var = tk.StringVar(value="2500 руб")
labor_label = tk.Label(main_frame, textvariable=labor_var, font=("Arial", 11), bg="#ffffff", relief="sunken",
                       anchor="w")
labor_label.pack(fill="x", pady=(0, 10), ipady=5)

tk.Label(main_frame, text="Срочность", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 5))
urgency_var = tk.StringVar(value="Обычный")
urgency_menu = ttk.Combobox(main_frame, textvariable=urgency_var, values=URGENCY_LIST, state="readonly", width=35)
urgency_menu.pack(fill="x", pady=(0, 10))

tk.Label(main_frame, text="Дополнительные услуги", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w",
                                                                                                  pady=(10, 5))
home_visit_var = tk.BooleanVar()
glass_var = tk.BooleanVar()
tk.Checkbutton(main_frame, text="Выезд мастера (+500 руб)", variable=home_visit_var, bg="#f0f0f0",
               font=("Arial", 10)).pack(anchor="w")
tk.Checkbutton(main_frame, text="Защитное стекло (+300 руб)", variable=glass_var, bg="#f0f0f0",
               font=("Arial", 10)).pack(anchor="w", pady=(0, 10))

tk.Label(main_frame, text="Промокод", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
promo_var = tk.StringVar()
promo_entry = tk.Entry(main_frame, textvariable=promo_var, font=("Arial", 11), width=35)
promo_entry.pack(fill="x", pady=(0, 10))

calc_button = tk.Button(main_frame, text="Рассчитать стоимость", command=calculate, bg="#4CAF50", fg="white",
                        font=("Arial", 12, "bold"), height=2)
calc_button.pack(fill="x", pady=(10, 20))

total_label = tk.Label(main_frame, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
total_label.pack(fill="x", pady=(0, 10))

result_label = tk.Label(main_frame, text="", font=("Arial", 11), bg="#ffffff", relief="sunken", justify="left",
                        anchor="nw")
result_label.pack(fill="both", expand=True, pady=(0, 10), ipady=10)

update_parts()
update_labor()

window.mainloop()
