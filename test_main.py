import pandas as pd
import main

def test_employee_creation():
    """Test basic employee creation"""
    try:
        employee = main.Employee("John Doe", 30, 50000.0)
        assert employee.name == "John Doe", f"Expected 'John Doe', got {employee.name}"
        assert employee.age == 30, f"Expected 30, got {employee.age}"
        assert employee.salary == 50000.0, f"Expected 50000.0, got {employee.salary}"
        print("✓ test_employee_creation passed")
        return True
    except Exception as e:
        print(f"✗ test_employee_creation failed: {e}")
        return False

def test_employee_validation():
    """Test employee validation errors"""
    test_cases = [
        # (test_name, function_call, expected_error)
        ("invalid name type", lambda: main.Employee(123, 30, 50000.0), TypeError),
        ("empty name", lambda: main.Employee("", 30, 50000.0), ValueError),
        ("age too young", lambda: main.Employee("John", 16, 50000.0), ValueError),
        ("negative salary", lambda: main.Employee("John", 30, -50000.0), ValueError),
    ]
    
    passed = 0
    for test_name, func, expected_error in test_cases:
        try:
            func()
            print(f"✗ test_employee_validation '{test_name}' failed: Expected {expected_error.__name__} but no error was raised")
        except expected_error:
            print(f"✓ test_employee_validation '{test_name}' passed")
            passed += 1
        except Exception as e:
            print(f"✗ test_employee_validation '{test_name}' failed: Expected {expected_error.__name__} but got {type(e).__name__}: {e}")
    
    return passed == len(test_cases)

def test_process_stock_data():
    """Test stock data processing"""
    try:
        # Create a sample DataFrame with enough data for rolling calculations
        close_prices = list(range(100, 300))  # 200 data points
        data = pd.DataFrame({'Close': close_prices})

        # Create employee and process data
        employee = main.Employee("Test Employee", 30, 50000.0)
        processed_data = employee.process_stock_data(data)

        # Validate the output
        required_columns = ['SMA_50', 'SMA_200', 'volatility', 'signals']
        for col in required_columns:
            assert col in processed_data.columns, f"Missing column: {col}"

        # Check that signals are generated correctly
        assert processed_data['signals'].isin([-1, 0, 1]).all(), "Signals should be -1, 0, or 1"
        
        print("✓ test_process_stock_data passed")
        return True
    except Exception as e:
        print(f"✗ test_process_stock_data failed: {e}")
        return False

def test_process_stock_data_edge_cases():
    """Test edge cases for stock data processing"""
    employee = main.Employee("Test Employee", 30, 50000.0)
    
    test_cases = [
        # (test_name, data, expected_error)
        ("empty DataFrame", pd.DataFrame(), ValueError),
        ("no Close column", pd.DataFrame({'Open': [100, 101]}), ValueError),
    ]
    
    passed = 0
    for test_name, data, expected_error in test_cases:
        try:
            employee.process_stock_data(data)
            print(f"✗ test_process_stock_data_edge_cases '{test_name}' failed: Expected {expected_error.__name__} but no error was raised")
        except expected_error:
            print(f"✓ test_process_stock_data_edge_cases '{test_name}' passed")
            passed += 1
        except Exception as e:
            print(f"✗ test_process_stock_data_edge_cases '{test_name}' failed: Expected {expected_error.__name__} but got {type(e).__name__}: {e}")
    
    return passed == len(test_cases)

def validate_trading_parameters(price: float, volume: int, symbol: str):
    """Validate trading parameters"""
    if not isinstance(price, float) or price <= 0:
        raise ValueError("Price must be a positive float")
    if not isinstance(volume, int) or volume <= 0:
        raise ValueError("Volume must be a positive integer")
    if not isinstance(symbol, str) or not symbol.isalpha():
        raise ValueError("Symbol must be a non-empty string of alphabetic characters")
    return True

def test_validate_trading_parameters():
    """Test trading parameter validation"""
    test_cases = [
        # (test_name, args, should_pass, expected_error)
        ("valid parameters", (100.5, 100, "AAPL"), True, None),
        ("invalid price", (-100.5, 100, "AAPL"), False, ValueError),
        ("invalid volume", (100.5, -100, "AAPL"), False, ValueError),
        ("invalid symbol", (100.5, 100, "AAPL123"), False, ValueError),
    ]
    
    passed = 0
    for test_name, args, should_pass, expected_error in test_cases:
        try:
            result = validate_trading_parameters(*args)
            if should_pass:
                assert result == True, f"Expected True, got {result}"
                print(f"✓ test_validate_trading_parameters '{test_name}' passed")
                passed += 1
            else:
                print(f"✗ test_validate_trading_parameters '{test_name}' failed: Expected {expected_error.__name__} but no error was raised")
        except Exception as e:
            if not should_pass and isinstance(e, expected_error):
                print(f"✓ test_validate_trading_parameters '{test_name}' passed")
                passed += 1
            else:
                print(f"✗ test_validate_trading_parameters '{test_name}' failed: {e}")
    
    return passed == len(test_cases)

def run_all_tests():
    """Run all tests and report results"""
    print("Running tests...\n")
    
    tests = [
        test_employee_creation,
        test_employee_validation,
        test_process_stock_data,
        test_process_stock_data_edge_cases,
        test_validate_trading_parameters
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "="*50)
    print("TEST SUMMARY:")
    print("="*50)
    
    passed = sum(results)
    total = len(results)
    
    for i, (test, result) in enumerate(zip(tests, results), 1):
        status = "PASS" if result else "FAIL"
        print(f"{i:2d}. {test.__name__}: {status}")
    
    print("="*50)
    print(f"Total: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed!")
        return False

if __name__ == "__main__":
    run_all_tests()