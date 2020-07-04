from pprint import pprint

cook_book = dict()

with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_title = f.readline().rstrip()
        count_of_ingr = f.readline().rstrip()
        if not dish_title:
            break
        count = 0
        ingridient_info_list = []

        while count < int(count_of_ingr):
            ing_str = f.readline().rstrip()
            ingridient_info = dict()
            ingridient = list(ing_str.split('|'))
            ingridient_info['ingridient_name'] = ingridient[0]
            ingridient_info['quantity'] = int(ingridient[1])
            ingridient_info['measure'] = ingridient[2]
            ingridient_info_list.append(ingridient_info)
            count += 1

        f.readline()
        cook_book[dish_title] = ingridient_info_list


def get_shop_list_by_dishes(dishes, person_count):
    ingridient_dict = {}
    for dish in dishes:
        for key, value in cook_book.items():
            if dish == key:
                for ingr_info in value:
                    if ingr_info['ingridient_name'] in ingridient_dict:
                        ingr_info['quantity'] += ingr_info['quantity']
                    ingridient_dict[ingr_info['ingridient_name']] = \
                        {'measure': ingr_info['measure'], 'quantity': ingr_info['quantity'] * person_count}

    return ingridient_dict


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Утка по-пекински'], 3))
