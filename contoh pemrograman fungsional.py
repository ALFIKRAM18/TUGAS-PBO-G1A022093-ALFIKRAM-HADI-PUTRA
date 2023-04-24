# Contoh program fungsional sederhana di Python

# Fungsi untuk menghitung kuadrat bilangan
def square(x):
    return x ** 2

# Fungsi untuk menghitung jumlah dari dua bilangan
def add(x, y):
    return x + y

# Fungsi untuk mengaplikasikan fungsi square pada setiap elemen list
def map_square(func, lst):
    return [func(x) for x in lst]

# Fungsi untuk menghitung jumlah dari seluruh elemen list
def reduce_sum(lst):
    return reduce(lambda x, y: x + y, lst)

# Contoh penggunaan fungsi map_square dan reduce_sum
my_list = [1, 2, 3, 4, 5]
squared_list = map_square(square, my_list) # [1, 4, 9, 16, 25]
sum_of_squares = reduce_sum(squared_list) # 55

# Output hasil program
print("my_list: ", my_list)
print("squared_list: ", squared_list)
print("sum_of_squares: ", sum_of_squares)
