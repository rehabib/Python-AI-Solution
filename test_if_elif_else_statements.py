import pytest
from if_elif_else_statements import scan_type_classification, patient_risk_level, image_resolution_classification, determine_contrast_type, scan_time_warning, detect_motion_artifacts


if __name__ == "__main__":
    # Tests
    assert scan_type_classification() == str, "Expected: str, Got: " + str(type(scan_type_classification()))
    assert patient_risk_level() == str, "Expected: str, Got: " + str(type(patient_risk_level()))
    assert image_resolution_classification() == str, "Expected: str, Got: " + str(type(image_resolution_classification()))
    assert determine_contrast_type() == str, "Expected: str, Got: " + str(type(determine_contrast_type()))
    assert scan_time_warning() == str, "Expected: str, Got: " + str(type(scan_time_warning()))
    assert detect_motion_artifacts() == str, "Expected: str, Got: " + str(type(detect_motion_artifacts()))
    
    print("All tests passed!")