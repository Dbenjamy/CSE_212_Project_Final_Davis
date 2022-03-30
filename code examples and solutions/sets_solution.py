def assemble_grocery_list(gro_one,gro_two):
    final_grocery_list = set()
    for item in gro_one:
        final_grocery_list.add(item)
    # Since sets cannot have duplicates, this will only add
    # new values.
    for item in gro_two:
        final_grocery_list.add(item)
    return final_grocery_list

first_grocery_list = {'eggs','milk','bread','apples','carrets','beef'}
second_grocery_list = {'milk','butter','cheese','lettuce','tomatos','carrets','onions','cabbage'}

combined_list = assemble_grocery_list(first_grocery_list, second_grocery_list)
print(combined_list)