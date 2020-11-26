# Task3
# 1
x = {" Hema ": 20, " Deepa ": 20, " Shine ": 20}
y = {"Deepa": 20, "Shine": 20}
z = x.copy()
for key, value in y.items():
    z[key] = value
print(z)
# 2
y.pop("Deepa")  # Removes the specified key
x.popitem()  # Removes the last inserted item
print(x)
print(y)
# 3
Dog = {"Goldenretriver", "Pug"}
Colour = {"white", "black"}
new_dic = dict(zip(Dog, Colour))
print(new_dic)
# 4
a={"milkybar" ,"kitkat" ,"dairymilk"}
print(len(a))
# 5
b={"kitkat"}
print(a-b)