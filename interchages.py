def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    
  s
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst


input_list = [12, 35, 9, 56, 24]
output_list = interchange_first_last(input_list)
print("Input:", input_list)
print("Output:", output_list)
