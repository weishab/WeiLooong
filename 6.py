n1 = 1010
n2 = 0b1010
n3 = 0o1010
n4 = 0x1010
print(n1,"\n",n2,"\n",n3,"\n",n4,"\n",n1+n2+n3+n4)
print("\n")



orbit_height = 3.84e5 
moon_diameter = 3476.2

result = 2 * orbit_height - moon_diameter

print(result)
print("{:.2e}".format(result))
print("\n")



l1 = [215.8,198.5,230.2,189.9,225.6]
print(max(l1),min(l1))
print(round(sum(l1)/5,1))
print("\n")



initial = 100
initial += 50
print(initial)
initial *= 2
print(initial)
initial //=3
print(initial)
initial%=7
print(initial)
initial**=2
print(initial)
print("\n")


aa=divmod(897,24)
print(aa)
bb=aa[1]
cc=bb**3%9
print(cc)
print("\n")



aaa=0.1
bbb=0.3
print(0.1*3==0.3)
ccc=(0.1*3)-0.3
print(ccc)
print(round(ccc,6))
print("\n")



is_true = True
is_false = False
print(int(is_true),int(is_false))
print(is_true + 5,is_false * 10)
print((is_true + 5) > (is_false * 10))
print("\n")



user_score = None
print(type(user_score))
print(user_score is None)
user_score = 89
print(user_score is None)
print("\n")



age = 22
has_ticket = True
has_fever = False
can = age >= 18 and has_ticket and not has_fever
print(can)
print("\n")




zz = 5 + 12j
print(zz.real, zz.imag)
yy = 3-4j
dd=zz-yy
print(dd)
print(abs(zz))
print("\n")
