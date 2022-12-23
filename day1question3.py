"""Write a program that generates all possible subsets of a given list"""
def generate_subsets(lst):
    # Base case: empty list
    if not lst:
        return [[]]
    
    # Recursive case: list with at least one element
    subsets = []
    for subset in generate_subsets(lst[1:]):
        # Add the current element to each subset
        subsets.append(subset + [lst[0]])
        # Add the current subset without the element
        subsets.append(subset)
    return subsets


print(generate_subsets([1, 2, 3]))

