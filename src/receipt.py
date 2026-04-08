def print_receipt(data, result):
    """Печатаем красивый чек"""
    
    print("\n" + "=" * 40)
    print("           ЧЕК")
    print("=" * 40)
    
    print(f"Модель: {data['model']}")
    print(f"Ремонт: {data['repair']}")
    
    print("-" * 40)
    print(f"Работа:           {result['labor']} руб")
    print(f"Запчасти:         {result['parts']} руб")
    
    if result['diagnostics'] > 0:
        print(f"Диагностика:      {result['diagnostics']} руб")
    
    if result['services'] > 0:
        print(f"Услуги:           {result['services']} руб")
    
    print(f"Промежуточно:     {result['subtotal']} руб")
    
    if result['multiplier'] > 1:
        print(f"Срочность (x{result['multiplier']})")
    
    if result['discount'] > 0:
        print(f"Скидка:          -{result['discount']} руб")
    
    print("-" * 40)
    print(f"ИТОГО:            {result['total']} руб")
    print("=" * 40)
    print("Спасибо за обращение!")
