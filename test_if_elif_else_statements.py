"""import pytest
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

    """

import pytest
from if_elif_else_statements import scan_type_classification, patient_risk_level, image_resolution_classification, determine_contrast_type, scan_time_warning, detect_motion_artifacts


if __name__ == "__main__":
    # Test scan_type_classification with "MRI"
    assert scan_type_classification("MRI") == "Magnetic Resonance Imaging", "Expected: Magnetic Resonance Imaging"
    assert scan_type_classification("CT") == "Computed Tomography", "Expected: Computed Tomography"
    assert scan_type_classification("X-ray") == "Other Imaging Modality", "Expected: Other Imaging Modality"

    # Test patient_risk_level with age
    assert patient_risk_level(65) == "High risk", "Expected: High risk"
    assert patient_risk_level(50) == "Moderate risk", "Expected: Moderate risk"
    assert patient_risk_level(30) == "Low risk", "Expected: Low risk"

    # Test image_resolution_classification with width
    assert image_resolution_classification(300) == "Low Resolution", "Expected: Low Resolution"
    assert image_resolution_classification(512) == "Medium Resolution", "Expected: Medium Resolution"
    assert image_resolution_classification(1200) == "High Resolution", "Expected: High Resolution"

    # Test determine_contrast_type with patient age
    assert determine_contrast_type(5) == "Pediatric contrast", "Expected: Pediatric contrast"
    assert determine_contrast_type(30) == "Standard contrast", "Expected: Standard contrast"
    assert determine_contrast_type(75) == "Low-dose contrast", "Expected: Low-dose contrast"

    # Test scan_time_warning with scan time
    assert scan_time_warning(5) == "Fast scan", "Expected: Fast scan"
    assert scan_time_warning(15) == "Optimal scan", "Expected: Optimal scan"
    assert scan_time_warning(25) == "Long scan, check settings", "Expected: Long scan, check settings"

    # Test detect_motion_artifacts with motion level
    assert detect_motion_artifacts(1) == "Minimal artifact", "Expected: Minimal artifact"
    assert detect_motion_artifacts(3) == "Moderate artifact", "Expected: Moderate artifact"
    assert detect_motion_artifacts(5) == "Severe artifact, re-scan required", "Expected: Severe artifact, re-scan required"

    print("All tests passed!")
