
def convert_temperature(
    value: float,
    from_scale: str,
    to_scale: str
    ) -> float:
    """_summary_
    Convert temperature between Celsius and Fahrenheit scales.
    
    Args:
        value (float): The temperature value to convert
        from_scale (str): Original scale - 'C' for Celsius or 'F' for Fahrenheit
        to_scale (str): Target scale - 'C' for Celsius or 'F' for Fahrenheit

    Returns:
        float: The converted temperature value.
        
    Raises:
        ValueError: If either scale is not 'C' or 'F'

    Examples:
        >>> convert_temperature(0, 'C', 'F')
        32.0
        >>> convert_temperature(100, 'C', 'F')
        212.0
        >>> convert_temperature(32, 'F', 'C')
        0.0
    """

    # Convert scales to uppercase for case-insensitive comparison
    from_scale = from_scale.upper()
    to_scale = to_scale.upper()

    # Validate input scales
    valid_scales = ['C','F']
    
    if not from_scale in valid_scales or not to_scale in valid_scales:
        raise ValueError(f"Scales must be 'C' or 'F', got '{from_scale}' and '{to_scale}'")

    # If the scales are the same, return original value
    if from_scale == to_scale:
        return float(value)

    # Perform conversion
    if from_scale == 'C' and to_scale == 'F':
        return (value * (9/5)) + 32
    elif from_scale == 'F' and to_scale == 'C':
        return ((value - 32) * (5/9))


            
