def find_common_elements(list1, list2):
    common_elements = []

    # Iterate through the first list
    for element1 in list1:
        # Check if the element is in the second list
        for element2 in list2:
            if element1 == element2 and element1 not in common_elements:
                common_elements.append(element1)
                break  # No need to check further once a match is found

    return common_elements


# Example usage
list1 = [1, 3, 4, 6, 7, 9]
list2 = [2, 3, 5, 6, 8, 9]
result = find_common_elements(list1, list2)
print("Common elements:",result)