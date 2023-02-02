########

# Enumerate : otomatik Counter/ Index ile for loop

########

students = ["John", "Mark", "Venessa", "Mariam"]

for index, student in enumerate(students, 1):
    # enumerate fonksiyonu iki parametre aldı.
    # Birincisi döndüreceği Loop
    # İkincisi başlayacağı index
    print(index, student)

########

# Uygulama - Mülakat Sorusu

########

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    a = [[],[]]


    for index, student in enumerate(students):
        if index % 2 == 0:
            a[0].append(student)
        else:
            a[1].append(student)

    return a

divide_students(students)

