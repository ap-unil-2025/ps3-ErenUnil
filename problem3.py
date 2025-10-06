"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """Get numbers from user until they type 'done'."""
    numbers = []

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == "done":
            break  # sort de la boucle

        try:
            number = float(user_input)  # convertit la saisie en nombre
            numbers.append(number)      # ajoute à la liste
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers

    return analysis
def analyze_numbers(numbers):
    """Analyze the list and return a dictionary with summary statistics."""
    if not numbers:
        return None

    analysis = {}
    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = sum(numbers) / len(numbers)
    analysis["min"] = min(numbers)
    analysis["max"] = max(numbers)
    analysis["even_count"] = len([n for n in numbers if n % 2 == 0])
    analysis["odd_count"] = len([n for n in numbers if n % 2 != 0])

    return analysis

def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
def display_analysis(analysis):
    """Display all analysis results in a nice format."""
    if not analysis:
        return

    print("Analysis Results:")
    print("-" * 20)
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Min: {analysis['min']}")
    print(f"Max: {analysis['max']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()