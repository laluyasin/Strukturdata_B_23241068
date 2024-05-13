# Tabel kebenaran (logika bolean)
# not and or xor

# NOT

print("*****Logika NOT*****")
x = False
y = True 
print('value x =', x)
print('***********NOT')
print('value y =', y)

# OR (semua bernilai true asalkan ada truenya)
print("*****Logika OR*****")
x = False
y = False
z = x or y
print(x, 'OR' , y , '=', z)
x = False
y = True
z = x or y
print(x, 'OR' , y , '=', z)
x = True
y = False
z = x or y
print(x, 'OR' , y , '=', z)
x = True
y = True
z = x or y
print(x, 'OR' , y , '=', z)

# OR (semua bernilai true asalkan ada truenya)
# berlaku untuk wanita
print("*****Logika OR*****")
x = False
y = False
z = x or y
print(x, 'OR' , y , '=', z)
x = False
y = True
z = x or y
print(x, 'OR' , y , '=', z)
x = True
y = False
z = x or y
print(x, 'OR' , y , '=', z)
x = True
y = True
z = x or y
print(x, 'OR' , y , '=', z)

# AND (hanya bernilai true, ketika keduanya true)
# berlaku untuk lelaki
print("*****Logika AND*****")
x = False
y = False
z = x and y
print(x, 'and' , y , '=', z)
x = False
y = True
z = x and y
print(x, 'and' , y , '=', z)
x = True
y = False
z = x and y
print(x, 'and' , y , '=', z)
x = True
y = True
z = x and y
print(x, 'and' , y , '=', z)
