def generate_power_set(input_set):
    """
    Generate the power set of the given set using bit manipulation.
    
    Args:
        input_set: A list of elements representing the set
        
    Returns:
        A list of lists representing all possible subsets
    """
    n = len(input_set)
    # Total number of subsets is 2^n
    power_set_size = 1 << n
    power_set = []
    
    # Loop through all binary combinations from 0 to 2^n - 1
    for i in range(power_set_size):
        subset = []
        
        # Check each bit position
        for j in range(n):
            # If jth bit is set, include jth element
            if (i & (1 << j)) > 0:
                subset.append(input_set[j])
        
        power_set.append(subset)
    
    return power_set

def main():
    """Main function to run the power set generator."""
    print("\n=== Power Set Generator ===\n")
    
    # Get user input
    user_input = input("Enter elements separated by commas (e.g., a,b,c): ")
    
    # Parse the input
    if not user_input.strip():
        print("Error: Empty input. Please enter at least one element.")
        return
    
    # Split by comma and remove whitespace
    elements = [item.strip() for item in user_input.split(',') if item.strip()]
    
    # Check for duplicates
    original_length = len(elements)
    unique_elements = list(set(elements))
    
    if len(unique_elements) < original_length:
        print("Note: Duplicate elements were removed.")
    
    # Check if set is too large
    if len(unique_elements) > 10:
        print("Error: Set is too large! Maximum 10 elements allowed to prevent performance issues.")
        return
    
    # Generate power set
    power_set = generate_power_set(unique_elements)
    
    # Display results
    print(f"\nOriginal Set: {{{', '.join(unique_elements)}}}")
    print(f"Number of subsets: {len(power_set)}")
    print("\nPower Set:")
    
    # Display all subsets
    for subset in power_set:
        if not subset:
            print("  {}")  # Empty set
        else:
            print(f"  {{{', '.join(subset)}}}")

# Run the program
if __name__ == "__main__":
    main()
    
    # Add some test cases as examples
    print("\n=== Test Cases ===")
    print("\nTest Case 1: {a, b, c}")
    test_set = ["a", "b", "c"]
    power_set = generate_power_set(test_set)
    print(f"Power set size: {len(power_set)}")
    
    print("\nTest Case 2: Empty Set")
    test_set = []
    power_set = generate_power_set(test_set)
    print(f"Power set size: {len(power_set)}")
    
    print("\nTest Case 3: {1, 2, 3, 4}")
    test_set = ["1", "2", "3", "4"]
    power_set = generate_power_set(test_set)
    print(f"Power set size: {len(power_set)}")
    
    print("\nPress Enter to exit...")
    input()