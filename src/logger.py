from datetime import datetime

def write_log(message):
    """Записываем сообщение в файл лога"""
    # ФИКСИРОВАННАЯ ДАТА: 8 апреля 2026 года
    now = "2026-04-08 9:00:00"
    
    # Открываем файл для добавления
    with open("logs/log.txt", "a", encoding="utf-8") as file:
        file.write(f"{now} - {message}\n")


def log_start():
    """Логируем запуск"""
    write_log("Программа запущена")
    print("Логирование включено")


def log_input(data):
    """Логируем ввод пользователя"""
    write_log(f"Модель: {data['model']}")
    write_log(f"Ремонт: {data['repair']}")
    write_log(f"Запчасти: {data['parts']} руб")
    write_log(f"Срочность: {data['urgency']}")
    write_log(f"Услуги: {data['services']} руб")
    write_log(f"Промокод: {data['promocode']}")


def log_result(result):
    """Логируем результат"""
    write_log(f"Итоговая сумма: {result['total']} руб")
    write_log("=" * 30)


def log_error(error):
    """Логируем ошибку"""
    write_log(f"ОШИБКА: {error}")
