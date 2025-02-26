import pytest
from manipulation_variable import basic_variable, calculate_mri_difference, modify_scan_type, check_abnormality, convert_suv


if __name__ == "__main__":
    # Test Exercise 1
    result = basic_variable()
    assert result == str, f"Expected: {str}, Got: {result}"
    
    # Test Exercise 2
    result = calculate_mri_difference()
    assert result == 5.5, f"Expected: 5.5, Got: {result}"
    
    # Test Exercise 3
    result = modify_scan_type()
    assert result == "FMRI MRI", f"Expected: FMRI MRI, Got: {result}"
    
    # Test Exercise 4
    result = check_abnormality()
    assert result == "Abnormality detected in the CT scan. Further investigation required.", \
           f"Expected: Abnormality message, Got: {result}"
    
    # Test Exercise 5
    result = convert_suv()
    assert round(result, 2) == 4.18, f"Expected: 4.18, Got: {round(result, 2)}"
    
    print("All tests passed!")