def shift_array():
    lst = [1, 2, 3, 4, 7,9,-2,6]
    add=5
    midpoint = len(lst)//2       
    lst = lst[0:midpoint] + [add] + lst[midpoint:]  
    print(lst)
shift_array()