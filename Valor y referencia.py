# Tipos de datos por valor

my_int_a = 10
my_int_b = my_int_a
#my_int_b = 20
my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de datos por referencia

my_list_a = [10,20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor

def_int_a = 10

def func_int(my_int: int):
    my_int = 20
    print(my_int)

func_int(def_int_a)
print(def_int_a)

# Funciones con datos por referencia

def my_list_fun(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    my_list_e = my_list
    my_list_d.append(50)

    print(my_list)
    print(my_list_d)
    print(my_list_e)

my_list_c = [10,20]
my_list_fun(my_list_c)
print(my_list_c)

# Por valor

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Por referencia

def ref(ref_a: list, ref_b: list) -> tuple:
    temp = ref_a
    ref_a = ref_b
    ref_b = temp
    return ref_a, ref_b

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")