"""
Elevator Dispatch System (elevator_dispatch.py)
Hardened implementation for Lab 7: Fuzzing for Input Validation Bugs
Student: Siri Sanikop (PES1UG24AM277)
"""

def parse_request(text):
    """
    Parse a floor request string formatted as 'FROM->TO'.
    
    Args:
        text (str): A string in the format 'FROM->TO' (e.g. '5->9').
        
    Returns:
        tuple[int, int] | None: A tuple of (start_floor, end_floor) as integers,
                                or None if input is invalid, malformed, or unparseable.
    """
    if not isinstance(text, str):
        return None
    if '->' not in text:
        return None
    parts = text.split('->')
    if len(parts) != 2:
        return None
    try:
        start = int(parts[0].strip())
        end = int(parts[1].strip())
        return start, end
    except (ValueError, TypeError):
        return None


def total_travel(floors_csv):
    """
    Calculate the total floors travelled given a comma-separated string of floor numbers.
    
    Args:
        floors_csv (str): Comma-separated floor sequence (e.g. '1,5,3,9').
        
    Returns:
        int: The sum of absolute differences between consecutive floors,
             or 0 if input is invalid, empty, or contains fewer than 2 floors.
    """
    if not isinstance(floors_csv, str):
        return 0
    if not floors_csv.strip():
        return 0
    try:
        floors = [int(f.strip()) for f in floors_csv.split(',') if f.strip()]
        if len(floors) < 2:
            return 0
        return sum(abs(floors[i + 1] - floors[i]) for i in range(len(floors) - 1))
    except (ValueError, TypeError):
        return 0


def load_percent(text):
    """
    Calculate the elevator load percentage from a string formatted as 'LOAD of CAPACITY'.
    
    Args:
        text (str): String formatted as 'LOAD of CAPACITY' (e.g. '450 of 630').
        
    Returns:
        int: Integer percentage (load * 100 // capacity),
             or 0 if input is invalid, non-numeric, or capacity <= 0.
    """
    if not isinstance(text, str):
        return 0
    if ' of ' not in text:
        return 0
    parts = text.split(' of ')
    if len(parts) != 2:
        return 0
    try:
        load = int(parts[0].strip())
        capacity = int(parts[1].strip())
        if capacity <= 0:
            return 0
        return load * 100 // capacity
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result)


if __name__ == "__main__":
    main()
