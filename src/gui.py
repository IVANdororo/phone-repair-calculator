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

MODEL_NAMES = {
    "iPhone": "iPhone",
    "Samsung": "Samsung",
    "Xiaomi": "Xiaomi",
    "Google Pixel": "Google Pixel",
    "Other": "Другие"
}

REPAIR_NAMES = {
    "screen": "Замена экрана",
    "battery": "Замена аккумулятора",
    "motherboard": "Ремонт материнской платы"
}

URGENCY_NAMES = {
    "normal": "Обычный (3-5 дней)",
    "urgent": "Срочный (1 день, +30%)",
    "emergency": "Экстренный (2-4 часа, +50%)"
}

MODEL_LIST = ["iPhone", "Samsung", "Xiaomi", "Google Pixel", "Другие"]
MODEL_KEYS = ["iPhone", "Samsung", "Xiaomi", "Google Pixel", "Other"]

REPAIR_LIST = ["Замена экрана", "Замена аккумулятора", "Ремонт материнской платы"]
REPAIR_KEYS = ["screen", "battery", "motherboard"]

URGENCY_LIST = ["Обычный (3-5 дней)", "Срочный (1 день, +30%)", "Экстренный (2-4 часа, +50%)"]
URGENCY_KEYS = ["normal", "urgent", "emergency"]

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
    price = PARTS_PRICES.get(model, {}).get(repair, 3000)
    parts_var.set(f"{price} руб")
    return price

def calculate():
    try:
        model_name = model_var.get()
        model = get_model_key(model_name)
        repair_name = repair_var.get()
        repair = get_repair_key(repair_name)
        urgency_name = urgency_var.get()
        urgency = get_urgency_key(urgency_name)
        parts = PARTS_PRICES.get(model, {}).get(repair, 3000)
        
        services = 0
        if home_visit_var.get():
            services += 500
        if glass_var.get():
            services += 300
        
        promocode = promo_var.get()
        
        data = {
            "model": model,
            "repair": repair,
            "parts": parts,
            "urgency": urgency,
            "services": services,
            "promocode": promocode
        }
        
        result = calc_total(data)
        comparison = compare_options(model, repair, urgency)
        
        result_label.config(
            text=f"Оригинал: {comparison['original']:.2f} руб.\n"
                 f"Аналог: {comparison['analog']:.2f} руб.\n"
                 f"Рекомендация: {comparison['best']}\n"
                 f"Экономия: {comparison['savings']:.2f} руб.",
            fg="black"
        )
        
        total_label.config(text=f"ИТОГО К ОПЛАТЕ: {result['total']:.2f} руб.", fg="red", font=("Arial", 16, "bold"))
        
    except Exception as e:
        result_label.config(text=f"Ошибка: {e}", fg="red")
        total_label.config(text="")

window = tk.Tk()
window.title("Калькулятор ремонта телефона")
window.geometry("450x700")
window.configure(bg="#f0f0f0")

main_frame = tk.Frame(window, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(main_frame, text="Модель телефона", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0,5))
model_var = tk.StringVar(value="iPhone")
model_menu = ttk.Combobox(main_frame, textvariable=model_var, values=MODEL_LIST, state="readonly", width=30)
model_menu.pack(fill="x", pady=(0,10))
model_menu.bind("<<ComboboxSelected>>", update_parts)

tk.Label(main_frame, text="Тип ремонта", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0,5))
repair_var = tk.StringVar(value="Замена экрана")
repair_menu = ttk.Combobox(main_frame, textvariable=repair_var, values=REPAIR_LIST, state="readonly", width=30)
repair_menu.pack(fill="x", pady=(0,10))
repair_menu.bind("<<ComboboxSelected>>", update_parts)

tk.Label(main_frame, text="Стоимость запчастей", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0,5))
parts_var = tk.StringVar(value="5000 руб")
parts_label = tk.Label(main_frame, textvariable=parts_var, font=("Arial", 11), bg="#ffffff", relief="sunken", anchor="w")
parts_label.pack(fill="x", pady=(0,10), ipady=5)

tk.Label(main_frame, text="Срочность", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0,5))
urgency_var = tk.StringVar(value="Обычный (3-5 дней)")
urgency_menu = ttk.Combobox(main_frame, textvariable=urgency_var, values=URGENCY_LIST, state="readonly", width=30)
urgency_menu.pack(fill="x", pady=(0,10))

tk.Label(main_frame, text="Дополнительные услуги", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(10,5))
home_visit_var = tk.BooleanVar()
glass_var = tk.BooleanVar()
tk.Checkbutton(main_frame, text="Выезд мастера (+500 руб)", variable=home_visit_var, bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w")
tk.Checkbutton(main_frame, text="Защитное стекло (+300 руб)", variable=glass_var, bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w", pady=(0,10))

tk.Label(main_frame, text="Промокод", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(10,5))
promo_var = tk.StringVar()
promo_entry = tk.Entry(main_frame, textvariable=promo_var, font=("Arial", 11), width=30)
promo_entry.pack(fill="x", pady=(0,10))

calc_button = tk.Button(main_frame, text="Рассчитать стоимость", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), height=2)
calc_button.pack(fill="x", pady=(10,20))

total_label = tk.Label(main_frame, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
total_label.pack(fill="x", pady=(0,10))

result_label = tk.Label(main_frame, text="", font=("Arial", 11), bg="#ffffff", relief="sunken", justify="left", anchor="nw")
result_label.pack(fill="both", expand=True, pady=(0,10), ipady=10)

update_parts()

window.mainloop()
