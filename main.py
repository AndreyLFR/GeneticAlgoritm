import random

# количество попыток (особей)
n = 100
reproduction_count = 5
mutation_count = 5
#min количество опытных
min_count_senior = 2
#минимальный объем производства
min_production = 1000
# максимальное число мест в офисе
max_place = 10
#производительность
dict_production = {'x': 200, 'y': 100, 'z': 40}
#зарплаты
dict_salary = {'x': 150, 'y': 100, 'z': 50}

def get_first_generation(n):
    gens = {}
    for i in range(0, n):
        x = random.randint(min_count_senior, max_place)
        y = random.randint(1, max_place)
        z = random.randint(1, max_place)
        gens[(x, y, z)] = dict_salary['x']*x + dict_salary['y']*y + dict_salary['z']*z
    print(f'Подобрали {len(gens)} возможных команд')
    return gens


def selection(dict_):
    gens_selection = {}
    for key, value in dict_.items():
        sum_production = dict_production['x'] * key[0] + dict_production['y'] * key[1] + dict_production['z'] * key[2]
        sum_place = sum(key)
        if sum_place <= max_place and sum_production >= min_production:
            gens_selection[key] = value
    print(f'Из {len(dict_)} возможных команд соответствуют ограничениям {len(gens_selection)}')
    return gens_selection


def reproduction(dict_):
    i = 0
    new_dict = {}
    for key in dict_:
        if i != 0:
            x_new = random.choice([key[0], x_previous])
            y_new = random.choice([key[1], y_previous])
            z_new = random.choice([key[2], z_previous])
            new_dict[(x_new, y_new, z_new)] = dict_salary['x']*x_new + dict_salary['y']*y_new + dict_salary['z']*z_new

        x_previous = key[0]
        y_previous = key[1]
        z_previous = key[2]
        i += 1
    return {**new_dict, **dict_}


def mutations(dict_):
    new_dict = {}
    for key in dict_:
        x_new = random.choice([key[0], random.randint(min_count_senior, max_place)])
        y_new = random.choice([key[1], random.randint(0, max_place)])
        z_new = random.choice([key[2], random.randint(0, max_place)])
        new_dict[(x_new, y_new, z_new)] = dict_salary['x'] * x_new + dict_salary['y'] * y_new + dict_salary['z'] * z_new
    return {**new_dict, **dict_}


gens = get_first_generation(n=n)
gens_selection = selection(dict_=gens)
gens_selection_sorted = dict(sorted(gens_selection.items(), key=lambda item: item[1]))
print(gens_selection_sorted)
for _ in range(0, reproduction_count):
    gens_reproduction = reproduction(dict_=gens_selection_sorted)
    gens_repr_selection = selection(dict_=gens_reproduction)
    gens_selection_sorted = dict(sorted(gens_repr_selection.items(), key=lambda item: item[1]))
    print(gens_selection_sorted)

for _ in range(0, mutation_count):
    gens_mutation = mutations(dict_=gens_selection_sorted)
    gens_mut_selection = selection(dict_=gens_mutation)
    gens_selection_sorted = dict(sorted(gens_mut_selection.items(), key=lambda item: item[1]))
    print(gens_selection_sorted)

for key, value in gens_selection_sorted.items():
    print(f'Минимальный ФОТ {value}. Количество опытных {key[0]}, средних {key[1]}, новичков {key[2]} ')
    break