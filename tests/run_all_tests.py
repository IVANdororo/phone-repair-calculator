import subprocess
tests = [
    "test_calculator.py",
    "test_input_handler.py",
    "test_logger.py",
    "test_receipt.py"
]
for test in tests:
    print(f"\nRunning {test}...")
    subprocess.run(["python", f"tests/{test}"])
print("\nAll test suites completed")
