from date_module.date import Date

def test_calculate_date():
    test_date1 = Date(2024, 12, 19, 9, 14)
    test_date2 = Date(2024, 12, 19, 16, 14)
    test_date3 = Date(2024, 12, 19, 8, 14)
    test_date4 = Date(2024, 12, 20, 17, 14)
    test_date5 = Date(2024, 12, 31, 15, 14)
    test_date6 = Date(2024, 12, 21, 1, 14)
    test_date7 = Date(2024, 12, 20, 9, 14)

    valid_date1 = Date(2024, 12, 19, 13, 14)
    valid_date2 = Date(2024, 12, 20, 10, 14)
    valid_date3 = Date(2024, 12, 19, 10, 0)
    valid_date4 = Date(2024, 12, 23, 11, 0)
    valid_date5 = Date(2025, 1, 2, 14, 14)
    valid_date6 = Date(2024, 12, 23, 13, 0)
    valid_date7 = Date(2025, 1, 1, 11, 14)

    predict_date1 = test_date1.calculate_date(4)
    predict_date2 = test_date2.calculate_date(2)
    predict_date3 = test_date3.calculate_date(1)
    predict_date4 = test_date4.calculate_date(2)
    predict_date5 = test_date5.calculate_date(15)
    predict_date6 = test_date6.calculate_date(4)
    predict_date7 = test_date7.calculate_date(66)

    assert valid_date1 == predict_date1, f"Test 1 failed. Expected: {valid_date1}, got: {predict_date1}"
    assert valid_date2 == predict_date2, f"Test 2 failed. Expected: {valid_date2}, got: {predict_date2}"
    assert valid_date3 == predict_date3, f"Test 3 failed. Expected: {valid_date3}, got: {predict_date3}"
    assert valid_date4 == predict_date4, f"Test 4 failed. Expected: {valid_date4}, got: {predict_date4}"
    assert valid_date5 == predict_date5, f"Test 5 failed. Expected: {valid_date5}, got: {predict_date5}"
    assert valid_date6 == predict_date6, f"Test 6 failed. Expected: {valid_date6}, got: {predict_date6}"
    assert valid_date7 == predict_date7, f"Test 7 failed. Expected: {valid_date7}, got: {predict_date7}"