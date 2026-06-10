#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    dub = list(set(set_1) & set(set_2))
    for i in set_1:
        if (list(i) != dub):
            new.append(i)
    for i in set_2:
        if (list(i) != dub):
            new.append(i)
    return new
    

print(only_diff_elements({ "Python", "C", "Javascript" },{ "Bash", "C", "Ruby", "Perl" }))