import pytest
from if_else_statements import scan_type_classification, patient_risk_level, image_resolution_classification, determine_contrast_type, scan_time_warning, detect_motion_artifacts, check_scan_time, contrast_injection_decision, abnormal_suv_detection, patient_age_validation, check_if_grayscale, check_scan_urgency


if __name__ == "__main__":
    # Tests
    assert scan_type_classification() == str, "Expected: str, Got: " + str(type(scan_type_classification()))
    assert patient_risk_level() == str, "Expected: str, Got: " + str(type(patient_risk_level()))
    assert image_resolution_classification() == str, "Expected: str, Got: " + str(type(image_resolution_classification()))
    assert determine_contrast_type() == str, "Expected: str, Got: " + str(type(determine_contrast_type()))
    assert scan_time_warning() == str, "Expected: str, Got: " + str(type(scan_time_warning()))
    assert detect_motion_artifacts() == str, "Expected: str, Got: " + str(type(detect_motion_artifacts()))
    assert check_scan_time() == str, "Expected: str, Got: " + str(type(check_scan_time()))
    assert contrast_injection_decision() == str, "Expected: str, Got: " + str(type(contrast_injection_decision()))
    assert abnormal_suv_detection() == str, "Expected: str, Got: " + str(type(abnormal_suv_detection()))
    assert patient_age_validation() == str, "Expected: str, Got: " + str(type(patient_age_validation()))
    assert check_if_grayscale() == str, "Expected: str, Got: " + str(type(check_if_grayscale()))
    assert check_scan_urgency() == str, "Expected: str, Got: " + str(type(check_scan_urgency()))
    
    print("All tests passed!")