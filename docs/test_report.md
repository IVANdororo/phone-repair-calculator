# Отчёт о тестировании


## Окружение

- ОС: Windows
- Python: 3.8+
- Проект: Калькулятор стоимости ремонта телефона

## Результаты тестов

| Модуль | Тестов | Пройдено | Не пройдено | Успех |
|--------|--------|----------|-------------|-------|
| calculator.py | 9 | 9 | 0 | 100% |
| input_handler.py | 2 | 2 | 0 | 100% |
| logger.py | 3 | 3 | 0 | 100% |
| receipt.py | 1 | 1 | 0 | 100% |
| **Итого** | **15** | **15** | **0** | **100%** |

## Детали

### calculator.py (9 тестов)
- test_calc_labor: ПРОЙДЕН
- test_calc_total: ПРОЙДЕН
- test_calc_total_with_urgency: ПРОЙДЕН
- test_calc_total_with_emergency: ПРОЙДЕН
- test_promocode_SERVICE10: ПРОЙДЕН
- test_promocode_REMONT26: ПРОЙДЕН
- test_compare_options: ПРОЙДЕН
- test_diagnostics_motherboard: ПРОЙДЕН
- test_services: ПРОЙДЕН

### input_handler.py (2 теста)
- test_get_parts_price: ПРОЙДЕН
- test_get_parts_price_default: ПРОЙДЕН

### logger.py (3 теста)
- test_write_log: ПРОЙДЕН
- test_log_start: ПРОЙДЕН
- test_log_error: ПРОЙДЕН

### receipt.py (1 тест)
- test_print_receipt: ПРОЙДЕН

## Найденные ошибки

Ошибок не найдено.

## Вывод

Все тесты пройдены успешно. Программа стабильна и готова к использованию.
