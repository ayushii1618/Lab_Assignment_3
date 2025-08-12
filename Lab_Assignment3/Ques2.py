def valuesort(d):
    """
    Sorts the values of a dictionary based on its keys.

    Args:
        d (dict): The input dictionary.

    Returns:
        list: List of values sorted by key.
    """
    return [d[key] for key in sorted(d.keys())]

# Example usage:
if __name__ == "__main__":
    sample_dict = {'b': 2, 'a': 1, 'c': 3}
    print(valuesort(sample_dict))  # Output: [1,