##### Lambda
new_sum = lambda a, b: a + b

new_sum(4, 5)

##### Map

# İki parametre alır.
# 1. Bir fonksiyon
# 2. İteratif bir nesne
# For döngüsüne grek kalmadan kendisi fonksiyonu itertif nesne de uyguluyor


salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20/100 + x


##### Filter

# Filtreleme işlemi yapar

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))




list(map(new_salary,salaries))

# Lambda ve Map in ortak kullanımı

list(map(lambda x: x * 20 / 100 + x, salaries))
