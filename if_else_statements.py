def scan_type_classification():
    """
    Given modality = "MRI", write an if-elif-else statement that prints:
    "Magnetic Resonance Imaging" for "MRI",
    "Computed Tomography" for "CT",
    "Other imaging modality" otherwise.
    
    Returns:
        str: The classification of the imaging modality.
    """
    modality = None
    return None

def patient_risk_level():
    """
    Given age = 65, classify the patient’s risk level:
    "High risk" if age > 60,
    "Moderate risk" if 40 ≤ age ≤ 60,
    "Low risk" otherwise.
    
    Returns:
        str: The patient risk classification.
    """
    age = None
    return None

def image_resolution_classification():
    """
    Given resolution = "512x512", write an if-elif-else statement that classifies it as:
    "Low Resolution" if width < 512,
    "Medium Resolution" for 512 ≤ width ≤ 1024,
    "High Resolution" otherwise.
    
    Returns:
        str: The resolution classification.
    """
    resolution = None
    return None

def determine_contrast_type():
    """
    Determine Contrast Type for MRI:
    If patient_age < 10, use "Pediatric contrast",
    If 10 ≤ patient_age < 60, use "Standard contrast",
    Otherwise, use "Low-dose contrast".
    
    Returns:
        str: The contrast type.
    """
    patient_age = None
    return None

def scan_time_warning():
    """
    Given scan_time in minutes, print:
    "Fast scan" if time < 10,
    "Optimal scan" if 10 ≤ time ≤ 20,
    "Long scan, check settings" otherwise.
    
    Returns:
        str: The scan time classification.
    """
    scan_time = None
    return None

def detect_motion_artifacts():
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

def check_scan_time():
    """
    Given scan_time = 12.5 (in minutes), write an if-else statement that prints "Scan completed successfully" 
    if the scan time is less than 15 minutes, otherwise print "Scan took too long".
    
    Returns:
        str: The scan completion status.
    """
    scan_time = None
    return None

def contrast_injection_decision():
    """
    A CT scan requires contrast if the patient’s weight is above 70 kg. Write an if-else statement that prints 
    "Inject contrast" if patient_weight > 70, otherwise "No contrast needed".
    
    Returns:
        str: The contrast injection decision.
    """
    patient_weight = None
    return None

def abnormal_suv_detection():
    """
    Given a PET scan SUV value suv = 4.2, print "Abnormal" if the SUV value is greater than 3.5, otherwise "Normal".
    
    Returns:
        str: The SUV classification.
    """
    suv = None
    return None

def patient_age_validation():
    """
    Given age = 16, write an if-else statement that prints "Eligible for MRI" if the patient is 18 or older, 
    otherwise "MRI not recommended for minors".
    
    Returns:
        str: The MRI eligibility decision.
    """
    age = None
    return None

def check_if_grayscale():
    """
    Given channels = 1, write an if-else statement to print "Grayscale Image" if channels == 1, 
    otherwise print "Color Image".
    
    Returns:
        str: The image type classification.
    """
    channels = None
    return None

def check_scan_urgency():
    """
    If a scan has "high" priority, print "Urgent scan, process immediately", otherwise print 
    "Regular scan, process as scheduled".
    
    Returns:
        str: The scan urgency classification.
    """
    priority = None
    return None