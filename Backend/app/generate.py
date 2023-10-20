import random

def ft_shuffle(nb_groups: int):
    if nb_groups <= 0:
        return {"message": "nb_groups must be greater than 0"}
    list_students = []
    with open("./app/list_students.txt") as file:
        for line in file:
            line = line.rstrip()
            if line not in list_students:
                list_students.append(line)
        if len(list_students) < nb_groups:
            return {"message": "nb_groups must be less than the number of students"}
        random.shuffle(list_students)
    list_groups = []
    for i in range(0, len(list_students), nb_groups):
        list_groups.append(list_students[i:i+nb_groups])
        
    # for i in list_groups:
    #     print(f"Group {list_groups.index(i)+1}: {i}")
    return list_groups