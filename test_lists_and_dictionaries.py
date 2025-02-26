import pytest
from lists_and_dictionaries import create_modalities_list, get_first_two_times, update_scan_quality, get_patient_info, update_scan_parameters, create_image_metadata, create_patients_data
# Test cases
if __name__ == "__main__":
    # Test Exercise 6
    result = create_modalities_list()
    assert "PET" in result and len(result) == 5, f"Expected list with 5 elements including PET, Got: {result}"
    
    # Test Exercise 7
    result = get_first_two_times()
    assert result == [12.5, 8.0], f"Expected: [12.5, 8.0], Got: {result}"
    
    # Test Exercise 8
    result = update_scan_quality()
    assert result == ["high", "medium", "high", "medium"], \
           f"Expected: ['high', 'medium', 'high', 'medium'], Got: {result}"
    
    # Test Exercise 9
    result = get_patient_info()
    expected = {"ID": 101, "Name": "Alice", "Age": 45, "Modality": "MRI"}
    assert result == expected, f"Expected: {expected}, Got: {result}"
    
    # Test Exercise 10
    result = update_scan_parameters()
    assert result["slice_thickness"] == 1.5 and result["contrast_used"] == True, \
           f"Expected updated parameters, Got: {result}"
    
    # Test Exercise 11
    result = create_image_metadata()
    expected = {"resolution": "512x512", "scan_type": "MRI", "bit_depth": 16}
    assert result == expected, f"Expected: {expected}, Got: {result}"
    
    # Test Exercise 12
    result = create_patients_data()
    assert len(result) == 2 and 101 in result and 102 in result, \
           f"Expected dictionary with two patients, Got: {result}"
    
    print("All tests passed!")