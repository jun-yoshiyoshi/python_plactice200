set_val = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, }
set_val_2 = {10, 5, 20, 40, 100}
set_tmp = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

set_tmp.add(11)
print(f"        {set_val}")
print(f"add(11):{set_tmp}")
set_tmp.update(set_val_2)
print(f"update(set_val_2):{set_tmp}")
set_tmp.remove(0)
print(f"remove(0):{set_tmp}")
set_tmp.clear()
print(f"clear():{set_tmp}")
