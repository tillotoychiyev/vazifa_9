print("__________________________________")
print("_________ 1-topshiriq ____________")

numbers = [1,2,3,4]
res = list(map(lambda value: value * 3, numbers))
print(res)

print("__________________________________")
print("_________ 2-topshiriq ____________")

numbers = [1,2,3,4]
k_num = list(map(lambda value: value ** 2, numbers))
print(k_num)

print("__________________________________")
print("_________ 3-topshiriq ____________")

satrlar = ["salom", "dunyo", "hello", "world"]
uppers = list(map(lambda value: value.upper(), satrlar))
print(uppers)

print("__________________________________")
print("_________ 4-topshiriq ____________")

ism_list = ["Toxir", "Aziz", "Vali"]
res = list(map(lambda value: (value, len(value)), ism_list))
print(res)

print("__________________________________")
print("_________ 5-topshiriq ____________")

numbers = [1 ,-2, 3, -4, 5 -6]
result = list(map(lambda x: -x if x < 0 else x, numbers))
print(result)

print("__________________________________")
print("_________ 6-topshiriq ____________")

price = [5000, 10000, 15000, 20000]
res = list(map(lambda value: value/100*15+value, price))
print(res)

print("__________________________________")
print("_________ 7-topshiriq ____________")


print("__________________________________")
print("__________ 7-topshiriq ___________")
numbers_list = [1,2,3,4,5,6,7,8,9,10]
res_nom_list = list(map(lambda value: 0 if value % 2 == 0  else  value, numbers_list))

print(res_nom_list)

print("__________________________________")
print("__________ 8-topshiriq ___________")
words_list = ["hello", "salomat", "O'zbekiston", "hayr "]
words_list_res = list(map(lambda value: value+"!" if 9<=len(value)>=15  else value, words_list))
print(words_list_res)

print("__________________________________")
print("__________ 9-topshiriq ___________")
number_list = [1,2,3,4,5,6,7,8,9,10 ]
res_n_l = list(filter(lambda value: value % 2 == 0, number_list))
print(res_n_l)

print("__________________________________")
print("__________ 10-topshiriq __________")
numbers_list = [1,-2,3,-4,5,-6,7,-8,9,-10]
num_res_list = list(filter(lambda value: value>0, numbers_list))

print(num_res_list)

print("__________________________________")
print("__________ 11-topshiriq __________")
words_list = ["hello", "salomat", "O'zbekiston", "hayr "]
words_list_res = list(filter(lambda value: len(value)>5, words_list))

print(words_list_res)

print("__________________________________")
print("__________ 12-topshiriq __________")
numbers_list = [1,-2,3,-4,5,-6,7,-8,9,10]
numbers_list_res = list(filter(lambda value: value%5==0, numbers_list))
print(numbers_list_res)

print("__________________________________")
print("__________ 13-topshiriq __________")
name_list = ["Ali", "Toxir", "Jasur", "Aziz"]
names_res = list(filter(lambda value: value[0]=="A", name_list))
print(names_res)

print("__________________________________")
print("__________ 14-topshiriq __________")
numbers_list = [-1,2,-3,4,-5,6,0,-7,8,-9,10]
res_num_list = list(filter(lambda value: value>=0, numbers_list))
print(res_num_list)

print("__________________________________")
print("__________ 15-topshiriq __________")
words_list = ["hello world","salom python", "salom dunyo", "print python"]
words_list_res = list(filter(lambda value: "python" in value, words_list))
print(words_list_res)