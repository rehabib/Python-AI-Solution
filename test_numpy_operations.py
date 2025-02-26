import pytest
from numpy_operations import find_scan_time_range, calculate_mean_suv, normalize_suv_values, threshold_scan_times, transform_pixel_intensities, count_threshold_pixels


if __name__ == "__main__":
    # Test Exercise 21
    min_time, max_time = find_scan_time_range()
    assert min_time == 8.0 and max_time == 15.2, \
           f"Expected: (8.0, 15.2), Got: ({min_time}, {max_time})"
    
    # Test Exercise 22
    result = calculate_mean_suv()
    assert abs(result - 3.54) < 0.01, f"Expected: 3.54, Got: {result}"
    
    # Test Exercise 23
    result = normalize_suv_values()
    assert len(result) == 5, f"Expected array of length 5, Got: {len(result)}"
    assert 0 <= np.min(result) <= np.max(result) <= 1, "Values not properly normalized"
    
    # Test Exercise 24
    result = threshold_scan_times()
    assert all(x in ["Long", "Short"] for x in result), \
           f"Expected only 'Long' and 'Short' values, Got: {result}"
    
    # Test Exercise 25
    result = transform_pixel_intensities()
    assert len(result) == 4, f"Expected array of length 4, Got: {len(result)}"
    
    # Test Exercise 26
    result = count_threshold_pixels()
    assert result == 2, f"Expected: 2, Got: {result}"
    
    print("All tests passed!")