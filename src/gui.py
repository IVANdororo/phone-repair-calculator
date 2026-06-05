import tkinter as tk
from calculator import calc_total
from config import PRICES, URGENCY, PROMOCODES

def calculate():
    try:
        model = model_var.get()
        repair = repair_var.get()
        parts = float(parts_entry.get())
        urgency = urgency_var.get()
        services = 0
        if home_visit_var.get():
            services += 500
        if glass_var.get():
            services += 300
        promocode = promo_entry.get()

        data = {
            "model": model,
            "repair": repair,
            "parts": parts,
            "urgency": urgency,
            "services": services,
            "promocode": promocode
        }

        result = calc_total(data)
        result_label.config(text=f"ИТОГО: {result['total']:.2f} руб", fg="green")

    except Exception as e:
        result_label.config(text=f"Ошибка: {e}", fg="red")

window = tk.Tk()
window.title("Калькулятор ремонта телефона")
window.geometry("400x500")

model_var = tk.StringVar(value="iPhone")
repair_var = tk.StringVar(value="screen")
urgency_var = tk.StringVar(value="normal")
home_visit_var = tk.BooleanVar()
glass_var = tk.BooleanVar()

tk.Label(window, text="Модель телефона:", font=("Arial", 12)).pack(pady=5)
model_menu = tk.OptionMenu(window, model_var, "iPhone", "Samsung", "Xiaomi", "Google Pixel", "Other")
model_menu.pack()

tk.Label(window, text="Тип ремонта:", font=("Arial", 12)).pack(pady=5)
repair_menu = tk.OptionMenu(window, repair_var, "screen", "battery", "motherboard")
repair_menu.pack()

tk.Label(window, text="Стоимость запчастей (руб):", font=("Arial", 12)).pack(pady=5)
parts_entry = tk.Entry(window)
parts_entry.pack()

tk.Label(window, text="Срочность:", font=("Arial", 12)).pack(pady=5)
urgency_menu = tk.OptionMenu(window, urgency_var, "normal", "urgent", "emergency")
urgency_menu.pack()

tk.Label(window, text="Дополнительные услуги:", font=("Arial", 12)).pack(pady=5)
tk.Checkbutton(window, text="Выезд мастера (+500 руб)", variable=home_visit_var).pack()
tk.Checkbutton(window, text="Защитное стекло (+300 руб)", variable=glass_var).pack()

tk.Label(window, text="Промокод:", font=("Arial", 12)).pack(pady=5)
promo_entry = tk.Entry(window)
promo_entry.pack()

tk.Button(window, text="Рассчитать", command=calculate, bg="lightblue", font=("Arial", 12)).pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

window.mainloop()
