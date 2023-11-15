u_list = []

with open('medium.txt') as f:
    items = f.readlines()
    
    for item in items:
        if item not in u_list:
            u_list.append(item)

with open('large_final.txt', 'w') as file:
    for i in u_list:
        file.write(i)
    