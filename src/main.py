from input_handler import get_all_data
from calculator import calc_total, compare_options
from logger import log_start, log_input, log_result, log_error
from receipt import print_receipt


def main():
    try:
        log_start()                           # 1. Логируем запуск
        
        data = get_all_data()                 # 2. Спрашиваем пользователя
        log_input(data)                       # 3. Логируем ввод
        
        result = calc_total(data)             # 4. Считаем стоимость
        log_result(result)                    # 5. Логируем результат
        
        comparison = compare_options(         # 6. Сравниваем варианты
            data['model'], 
            data['repair'], 
            data['urgency']
        )
        
        print_receipt(data, result)           # 7. Печатаем чек
        
        # 8. Печатаем рекомендацию
        print("\n" + "=" * 40)
        print("       РЕКОМЕНДАЦИЯ")
        print("=" * 40)
        print(f"Оригинал: {comparison['original']} руб")
        print(f"Аналог:   {comparison['analog']} руб")
        print(f"Лучше взять: {comparison['best']}")
        print(f"Экономия: {comparison['savings']} руб")
        print("=" * 40)
        
    except Exception as e:
        log_error(str(e))
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
