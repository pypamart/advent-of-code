
def can_form_target(target, numbers):
    """
    Check if inserting '+' or '*' between the numbers (evaluated left-to-right)
    can produce the target value.
    
    This function tries all possible combinations of '+' and '*' operators 
    between the given numbers. The evaluation is strictly left-to-right 
    (no operator precedence).
    """
    from itertools import product
    
    # If there's only one number, just check if it equals the target directly
    if len(numbers) == 1:
        return numbers[0] == target
    
    # Generate all possible operator combinations: for n numbers, we have (n-1) slots for operators.
    # Each operator slot can be '+' or '*', so we have 2^(n-1) combinations.
    operators_combinations = product(['+', '*'], repeat=len(numbers)-1)
    
    for ops in operators_combinations:
        # Evaluate expression left-to-right
        value = numbers[0]
        for op, num in zip(ops, numbers[1:]):
            if op == '+':
                value = value + num
            else:
                value = value * num
        if value == target:
            return True
    return False


def solve_equations(lines):
    """
    Given a list of lines of the form:
    "<target>: <num1> <num2> ..."
    Determine which equations can possibly be true (by some combination of '+' and '*'),
    and sum their target values.
    """
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Parse the line
        # Format: "<target>: <n1> <n2> ..."
        left, right = line.split(':')
        target = int(left.strip())
        numbers = list(map(int, right.strip().split()))
        
        if can_form_target(target, numbers):
            total += target
    return total


if __name__ == "__main__":
    # Example usage based on the given sample:
    # Input lines (you can replace these with any input source you have)
    # lines = [
    #     "190: 10 19",
    #     "3267: 81 40 27",
    #     "83: 17 5",
    #     "156: 15 6",
    #     "7290: 6 8 6 15",
    #     "161011: 16 10 13",
    #     "192: 17 8 14",
    #     "21037: 9 7 18 13",
    #     "292: 11 6 16 20"
    # ]
    
    with open("day07.txt", "r") as file:
        lines = file.readlines()

    result = solve_equations(lines)
    print(result)  # For the given example, this should print 3749.
