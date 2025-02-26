import pytest
from list_comprehension import generate_scan_ids, filter_scan_times, extract_patient_names, get_image_widths, classify_suv_values, generate_report_titles, filter_scan_durations, get_even_indexed_slices


if __name__ == "__main__":
    # Test Exercise 13
    result = generate_scan_ids()
    assert result == list(range(1001, 1011)), f"Expected scan IDs from 1001 to 1010, Got: {result}"
    
    # Test Exercise 14
    result = filter_scan_times()
    assert result == [12.8, 15.1], f"Expected: [12.8, 15.1], Got: {result}"
    
    # Test Exercise 15
    result = extract_patient_names()
    assert result == ["Alice", "Bob", "Charlie"], f"Expected: ['Alice', 'Bob', 'Charlie'], Got: {result}"
    
    # Test Exercise 16
    result = get_image_widths()
    assert result == [256, 512, 1024], f"Expected: [256, 512, 1024], Got: {result}"
    
    # Test Exercise 17
    result = classify_suv_values()
    assert result == ['low', 'high', 'low', 'high', 'high'], \
           f"Expected: ['low', 'high', 'low', 'high', 'high'], Got: {result}"
    
    # Test Exercise 18
    result = generate_report_titles()
    assert result == ['MRI Report', 'CT Report', 'X-ray Report'], \
           f"Expected: ['MRI Report', 'CT Report', 'X-ray Report'], Got: {result}"
    
    # Test Exercise 19
    result = filter_scan_durations()
    assert all(x <= 30 for x in result), f"Expected all durations <= 30, Got: {result}"
    
    # Test Exercise 20
    result = get_even_indexed_slices()
    assert result == [1.5, 2.5, 5.0], f"Expected: [1.5, 2.5, 5.0], Got: {result}"
    
    print("All tests passed!")