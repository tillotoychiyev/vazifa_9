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