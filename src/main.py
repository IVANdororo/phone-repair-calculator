from input_handler import get_all_data
from calculator import calc_total
from logger import log_start, log_input, log_result, log_error
from receipt import print_receipt


def main():
    try:
        log_start()
        
        data = get_all_data()
        log_input(data)
        
        result = calc_total(data)
        log_result(result)
        
        print_receipt(data, result)
        
    except Exception as e:
        log_error(str(e))
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
