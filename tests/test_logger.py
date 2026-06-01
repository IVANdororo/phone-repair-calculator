import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from logger import write_log, log_start, log_error
def test_write_log():
    write_log("Test message")
    print("test_write_log OK")
def test_log_start():
    log_start()
    print("test_log_start OK")
def test_log_error():
    log_error("Test error")
    print("test_log_error OK")
if __name__ == "__main__":
    test_write_log()
    test_log_start()
    test_log_error()
    print("All tests passed")
