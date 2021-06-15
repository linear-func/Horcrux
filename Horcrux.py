#output
def result(hp,M):
	if hp <= 0 :
		return -1
	else:
		s = hp + M
		return s
#xác định số nguyên tố
def isprime(n):
	if n < 2 :
		return False
	elif n == 2:
		return True
	else:
		for i in range(2,n):
			if n%i == 0:
				return False
			else:
				return True
#tìm UCLN
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b)

#input
lst = []
R = int(input("R = "))
N = int(input("N = "))
ID = int(input("ID = "))
M = int(input("M = "))
n = int(input("số sự kiện xảy ra n = "))
for i in range(n):
	x = int(input())
	lst.append(x)
print(lst)

#list số nguyên
lst_integer = []
for i in range(100):
	if isprime(i) == True:
		lst_integer.append(i)
max_iprime = max(lst_integer)

#hp
def hp(ID):
	if ID == 1 :
		hp = 999
	elif ID == 2 :
		hp = 900
	elif ID == 3 :
		hp = 888
	else: 
		hp = 777
	return hp

#event_1
hp = hp(ID)
def event_1():
	if ID == 3:	
		hp += (M // max_iprime)
		M = M % max_iprime
	else:
		hp += M
		M = 0

#event_1xx
def even_1xx():
	h1 = i % (100+R)
	h2 = lst[i] % (100+R)
	if ID != 1 :
		if h1 >= h2 :
			M += int(lst[i])
			if M > 999:	
				M = 999
		else:
			hp -= lst[i]
	else:
		if isprime(h2) == True and h2 > M:
			hp -= lst[i]
		else:
			M += lst[i]
			if M > 999:
				M = 999
#event_2xx
from math import sqrt
def even_2xx():
	if a > 4 :
		#list số chính phương
		lst2 = []
		for i in range(int(math.sqrt(a))+1):
			lst2.append(i**2)
			b = max(lst2)
			M -= b
	else:
		if i < 3 :
			hp = 0
			M = 0
		else:
			i = 0
			for i in range(len(lst)):
				if 200 <= lst[i] <= 299:
					continue
		

#event_3xx
M = currentM
hp = currenthp
def event_3xx():
	h1 = i % (100+R)
	h2 = lst[i] % (100+R)
	if ID != 1 :
		if h1 >= h2 :
			i = 0
			for i in range(len(lst)):
				if 300 <= lst[i] <= 399:
					continue
		else:
			dem = 0
	else:
		if isprime(h2) == True and h2 > M:
			dem = 0
		else:
			for i in range(len(lst)):
				if 200 <= lst[i] <= 299 or 500 <= lst[i] <= 599:
					continue
				if 100 <= lst[i] <= 199 or lst[i] == 666 or lst[i] == 777:
					event_1xx
					if M < currentM or hp < currenthp :
						M = current
						hp = currenthp

#event_5xx
def event_5xx():
	if ID != 2 and ID != 4 and uscln(xx,hp)!= 1:
		lst3 = []
		xx = lst[i] - 500
		for i in range(len(lst1)):
			if lst1[i] % xx == 0:
				lst3.append(lst1[i])
		Q = max(lst3)
		if len(lst3) == 0:
			Q = 1
		h1 = i % (100+R)
		h2 = lst[i] % (100+R)
		if ID != 1 :
			if h1 < h2:
				hp -= lst[i]
				if Q > 	M:
					M = 0
				else:
					M -= Q
		else:
			if isprime(h2) == True and h2 > M:
				hp -= lst[i]
				if Q > 	M:
					M = 0
				else:
					M -= Q
		print("hp = ",hp)
#event_666
def event_666():
	h1 = i % (100+R)
	h2 = lst[i] % (100+R)
	if ID != 1 :
		if h1 >= h2 :
			M += int(lst[i])
			if M > 999:	
				M = 999
		else:
			hp -= lst[i]
	else:
		if isprime(h2) == True and h2 > M:
			hp -= lst[i]
		else:
			M += lst[i]
			if M > 999:
				M = 999
	print("hp = ",hp)

#check stop
dem = 0
for i in range(n):
	if lst[i] == 0:
		dem += 1
	elif lst[i] == 1:
		event_1()
	elif 100 <= lst[i] <= 199:
		event_1xx()
	elif 200 <= lst[i] <= 299:
		event_2xx()
	elif 300 <= lst[i] <= 399:
		event_3xx()
	elif 500 <= lst[i] <= 599:
		event_5xx()
	elif lst[i] == 666:
		event_666()

print(result(hp,M))
