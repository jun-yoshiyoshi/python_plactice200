set_val = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, }
set_val_2 = {10, 5, 20, 40, 100}

res_1 = set_val | set_val_2
res_2 = set_val.union(set_val_2)
res_3 = set_val & set_val_2
res_4 = set_val.intersection(set_val_2)
res_5 = set_val - set_val_2
res_6 = set_val.difference(set_val_2)
res_7 = set_val ^ set_val_2
res_8 = set_val.symmetric_difference(set_val_2)
res_9 = set_val <= set_val_2
res_10 = set_val.issubset(set_val_2)
res_11 = set_val >= set_val_2
res_12 = set_val.issuperset(set_val_2)


print(f"set_val | setval_2:{res_1}")
print(f"set_val.union(set_val_2):{res_2}")
print(f"set_val & setval_2:{res_3}")
print(f"set_val.intersection(set_val_2):{res_4}")
print(f"set_val - setval_2:{res_5}")
print(f"set_val.difference(set_val_2):{res_6}")
print(f"set_val ^ setval_2:{res_7}")
print(f"set_val.symmetric_difference(set_val_2):{res_8}")
print(f"set_val <= setval_2:{res_9}")
print(f"set_val.issubset(set_val_2):{res_10}")
print(f"set_val>=setval_2:{res_11}")
print(f"set_val.issuperset(set_val_2):{res_12}")
