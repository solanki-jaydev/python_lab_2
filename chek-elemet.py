def check_element_in_list(lst, element):
    return element in lst

# Example usage:
my_list = [12, 35, 9, 56, 24]
element_to_check = 35

if check_element_in_list(my_list, element_to_check):
    print(f"Element {element_to_check} exists in the list.")
else:
    print(f"Element {element_to_check} does not exist in the list.")
 