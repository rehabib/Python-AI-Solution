def print_scan_timer(scan_time):
    """
    Exercise 17: Use a while loop to simulate an MRI scan timer.
    Print "Scanning... X minutes remaining" until time reaches 0.
    
    Args:
        scan_time (int): Initial scan time in minutes
        
    Returns:
        list: List of status messages generated
    """
    messages = []
    # TODO: Implement while loop to generate timer messages
    
    messages.append("Scan complete!")
    return messages


def find_first_abnormal():
    """
    Exercise 18: Find first SUV value > 3.5 using while loop.
    
    Returns:
        float: First SUV value greater than 3.5
    """
    suv_values = [2.3, 3.2, 4.1, 5.6, 3.0]
    
    # TODO: Implement while loop to find first abnormal value
    return None


def reduce_motion_artifacts():
    """
    Exercise 19: Reduce motion_level from 5 to 1, printing each value.
    
    Returns:
        list: List of motion levels during reduction
    """
    motion_level = 5
    levels = []
    
    # TODO: Implement while loop to reduce motion level
    
    return levels


def print_patient_info():
    """
    Exercise 20: Use while loop to print patient information key-value pairs.
    
    Returns:
        list: List of formatted strings with patient information
    """
    patient = {
        "ID": 101,
        "Name": "Alice",
        "Age": 45,
        "Modality": "MRI"
    }
    info_strings = []
    
    # TODO: Implement while loop to format patient information
    
    return info_strings
