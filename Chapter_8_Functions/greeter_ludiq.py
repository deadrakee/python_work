def append_name(names):
    """append to list items"""
    indx = 0
    for name in names:
        names[indx] = f"{names[indx]} ludiq"
        indx += 1

names = ['ramboto', 'pesho', 'painera']
append_name(names)
print(names)