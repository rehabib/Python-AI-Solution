import pytest
from loops import print_scan_timer, find_first_abnormal, reduce_motion_artifacts, print_patient_info


if __name__ == "__main__":
    # Test Exercise 17
    result = print_scan_timer(3)
    expected = [
        "Scanning... 3 minutes remaining",
        "Scanning... 2 minutes remaining",
        "Scanning... 1 minutes remaining",
        "Scan complete!"
    ]
    assert result == expected, f"Expected: {expected}, Got: {result}"
    
    # Test Exercise 18
    result = find_first_abnormal()
    assert result == 4.1, f"Expected: 4.1, Got: {result}"
    
    # Test Exercise 19
    result = reduce_motion_artifacts()
    expected = [5, 4, 3, 2, 1]
    assert result == expected, f"Expected: {expected}, Got: {result}"
    
    # Test Exercise 20
    result = print_patient_info()
    assert len(result) == 4, f"Expected 4 information strings, Got: {len(result)}"
    assert "ID: 101" in result, "Missing ID information"
    
    print("All tests passed!")