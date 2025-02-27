def scan_type_classification(modality):
    """
    Given modality = "MRI", write an if-elif-else statement that prints:
    "Magnetic Resonance Imaging" for "MRI",
    "Computed Tomography" for "CT",
    "Other imaging modality" otherwise.
    
    Returns:
        str: The classification of the imaging modality.
    """
    if modality == "MRI":
        return "Magnetic Resonance Imaging"
    elif modality == "CT":
        return "Computed Tomography"
    else:
        return "Other Imaging Modality"



def patient_risk_level(age):
    """
    Given age = 65, classify the patient’s risk level:
    "High risk" if age > 60,
    "Moderate risk" if 40 ≤ age ≤ 60,
    "Low risk" otherwise.
    
    Returns:
        str: The patient risk classification.
    """
    if age > 60:
       return "High risk"
    elif 40<= age <=60:
       return "Moderate risk"
    else:
       return "Low risk"

#def image_resolution_classification():
    """
    Given resolution = "512x512", write an if-elif-else statement that classifies it as:
    "Low Resolution" if width < 512,
    "Medium Resolution" for 512 ≤ width ≤ 1024,
    "High Resolution" otherwise.
    
    Returns:
        str: The resolution classification.
    """


#def determine_contrast_type():
    """
    Determine Contrast Type for MRI:
    If patient_age < 10, use "Pediatric contrast",
    If 10 ≤ patient_age < 60, use "Standard contrast",
    Otherwise, use "Low-dose contrast".
    
    Returns:
        str: The contrast type.
    """
 

#def scan_time_warning():
    """
    Given scan_time in minutes, print:
    "Fast scan" if time < 10,
    "Optimal scan" if 10 ≤ time ≤ 20,
    "Long scan, check settings" otherwise.
    
    Returns:
        str: The scan time classification.
    """
  

#def detect_motion_artifacts():
    """
    Given motion_level (ranging from 1 to 5), classify as:
    "Minimal artifact" if motion_level == 1,
    "Moderate artifact" if 2 ≤ motion_level ≤ 3,
    "Severe artifact, re-scan required" otherwise.
    
    Returns:
        str: The motion artifact classification.
    """
    motion_level = None
    return None

def image_resolution_classification(width):
    if width < 512:
        return "Low Resolution"
    elif 512 <= width <= 1024:
        return "Medium Resolution"
    else:
        return "High Resolution"  # No need for extra lines after this


#def determine_contrast_type():
    """
    Determine Contrast Type for MRI:
    If patient_age < 10, use "Pediatric contrast",
    If 10 ≤ patient_age < 60, use "Standard contrast",
    Otherwise, use "Low-dose contrast".

    Returns:
        str: The contrast type.
    """
def determine_contrast_type(patient_age):
    if patient_age < 10:
      return "Pediatric contrast"
    elif  10 <= patient_age < 60:
      return "Standard contrast"
    else:
       return "Low-dose contrast"



#def scan_time_warning():
    """
    Given scan_time in minutes, print:
    "Fast scan" if time < 10,
    "Optimal scan" if 10 ≤ time ≤ 20,
    "Long scan, check settings" otherwise.

    Returns:
        str: The scan time classification.
    """

def scan_time_warning(scan_time):
    if scan_time < 10:
      return "Fast scan"
    elif 10 <= scan_time <=20:
      return "Optimal scan"
    else:
     return "Long scan, check settings"
   

#def detect_motion_artifacts():
    """
    Given motion_level (ranging from 1 to 5), classify as:
    "Minimal artifact" if motion_level == 1,
    "Moderate artifact" if 2 ≤ motion_level ≤ 3,
    "Severe artifact, re-scan required" otherwise.

    Returns:
        str: The motion artifact classification.
    """
def detect_motion_artifacts(motion_level):
    #if not isinstance(motion_level, int) or not(1<=motion_level<=5):
     #return "invalid motion level"

    if motion_level == 1:
      return "Minimal artifact"
    elif 2 <= motion_level <= 3:
      return "Moderate artifact"
    else:
       return "Severe artifact, rescan required"
    
print(detect_motion_artifacts(6))


#Testing with assertions

def detect_motion_artifacts(motion_level):
    if not isinstance(motion_level, int) or not (1 <= motion_level <= 5):
        return "Invalid motion level"

    if motion_level == 1:
        return "Minimal artifact"
    elif 2 <= motion_level <= 3:
        return "Moderate artifact"
    else:
        return "Severe artifact, re-scan required"



def test_detect_motion_artifacts():
    assert detect_motion_artifacts(1) == "Minimal artifact"
    assert detect_motion_artifacts(2) == "Moderate artifact"
    assert detect_motion_artifacts(3) == "Moderate artifact"
    assert detect_motion_artifacts(4) == "Severe artifact, re-scan required"
    assert detect_motion_artifacts(5) == "Severe artifact, re-scan required"
    assert detect_motion_artifacts(0) == "Invalid motion level"
    assert detect_motion_artifacts("3") == "Invalid motion level"

# Run the test
import pytest
pytest.main(["-q", "--tb=short"])
#-q (quiet mode): Reduces the amount of output to show only essential test results.
#--tb=short (short traceback): If a test fails, it shows a short version of the error instead of the full traceback.

assert detect_motion_artifacts(1) == "Minimal artifact"
assert detect_motion_artifacts(2) == "Moderate artifact"
assert detect_motion_artifacts(3) == "Moderate artifact"
assert detect_motion_artifacts(4) == "Severe artifact, re-scan required"
assert detect_motion_artifacts(5) == "Severe artifact, re-scan required"
assert detect_motion_artifacts(0) == "Invalid motion level"
assert detect_motion_artifacts("3") == "Invalid motion level"

print("All tests passed!")

assert scan_time_warning(5) == "Fast scan"
assert scan_time_warning(10) == "Optimal scan"
assert scan_time_warning(15) == "Optimal scan"
assert scan_time_warning(20) == "Optimal scan"
assert scan_time_warning(25) == "Long scan, check settings"

print("All tests passed successfully! ")

assert determine_contrast_type(8) == "Pediatric contrast"
assert determine_contrast_type(10) == "Standard contrast"
assert determine_contrast_type(50) == "Standard contrast"
assert determine_contrast_type(75) == "Low-dose contrast"
assert determine_contrast_type(59) == "Standard contrast"

def determine_contrast_type(patient_age):
    if patient_age < 10:
        return "Pediatric contrast"
    elif 10 <= patient_age < 60:
        return "Standard contrast"
    else:
        return "Low-dose contrast"  # No need for extra lines after this


assert determine_contrast_type(5) == "Pediatric contrast"
assert determine_contrast_type(10) == "Standard contrast"
assert determine_contrast_type(30) == "Standard contrast"
assert determine_contrast_type(59) == "Standard contrast"
assert determine_contrast_type(60) == "Low-dose contrast"
assert determine_contrast_type(75) == "Low-dose contrast"

print("All tests passed successfully!")


assert image_resolution_classification(300) == "Low Resolution"
assert image_resolution_classification(512) == "Medium Resolution"
assert image_resolution_classification(800) == "Medium Resolution"
assert image_resolution_classification(1024) == "Medium Resolution"
assert image_resolution_classification(1200) == "High Resolution"

print("All tests passed successfully!")


# Test scan_type_classification
assert scan_type_classification("MRI") == "Magnetic Resonance Imaging"
assert scan_type_classification("CT") == "Computed Tomography"
assert scan_type_classification("X-ray") == "Other Imaging Modality"

# Test patient_risk_level
assert patient_risk_level(65) == "High risk"
assert patient_risk_level(50) == "Moderate risk"
assert patient_risk_level(40) == "Moderate risk"
assert patient_risk_level(30) == "Low risk"

print("All tests passed successfully!")


