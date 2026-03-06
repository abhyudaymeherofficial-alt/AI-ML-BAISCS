from tkinter.font import names

print("hello")
s="Programming in python"
print(s)
print(s[0:3])
print(s[::-1])
print(len(s))
z=21+2.3j
y=3+4.2j
print(z.imag)
print((y+z).imag)
print(y.conjugate())
q="Iceland is the best country."
print(q*2)
print(q[-20:-1])

m=4
n=3
sta=f"{m} times {n} is {n*m}"
print(sta)
print(type(n))
print(type(sta))

flag=bool(1)
print(flag)
print(type(flag))

stringnumber1=str(12456)
print(stringnumber1)
print(type(stringnumber1))

x=5%2
print(x)

s="Pyhton"
if "y" in s or "P" not in s:
    print("yes")
else:
    print("no")

'''import math as iceland'''
from math import sqrt as iceland,pi as norway

print(iceland(16))
print(2*norway*1)

count=0
while count<=9:
    print(count)
    count=count+1
print("Good bye!!")

l1=list(range(2,30))
print(l1)

fruits=["pomme","mure","banane","orange","raisan"]
for i in fruits:
    print(i)
print("--------------------")
for i in range(len(fruits)):
    print("\ncurrent fruit:",fruits[i],end="@@@")
print("\n")
l2=list(range(-22,30,3))
print(l2)

s="Iceland"
f=0
while True:
    if s[f]=="a":
        break
    print(s[f])
    f=f+1


'''----------------------
cou=0
no1=int(input("Emter a number:"))
for i in range(1,no1):
    if no1%i==0:
        cou=cou+1
print(cou)
if(cou>1):
    print("Its not a prime number")
else:
    print("Its a prime number")

-----------------------'''

fruits1=["pomme","mure","banane","orange","raisan"]
print(fruits1[1:4])
fruits1.remove(fruits1[2])
print(fruits1)

l4=[1.2,3.4,8.9,58.5,1,8.9,8.8]
print(max(l4))
print(min(l4))
l4.extend("car")
print(l4)
print(l4.pop())
print(l4.pop(2))
print(l4.count(8))

d={1:"Python",2:"Cpp",3:"JAVA","con1":"Iceland","con2":"Greenland"}
print(d[1])
print(d["con2"])
print(len(d))
print(str(d))
print(type(d))
d1=d.copy()
print(d1)
lq1=["a","b","c","d","e"]
d2=dict.fromkeys(lq1,"asx")
print(d2)
print(d.get("con1"))
print(d.items())
print(d.keys())
print(d.values())
print(d.update({"con3":"Norway"}))
print(d)
for i in d:
    print(i)
print("-----------------")
for i in d.values():
    print(i)
print("------------------")
for i in d.items():
    print(i)
    print(i[0],":",i[1])

'''ZIP METHOD'''

names1=["John","Charles","Miki"]
age=[23,56,21]
zip_list=list(zip(names1,age))
print(zip_list)


'''SETS'''

s={1,2,3,4,"Python",("x",1)}
x=set("Iceland")
y2=set(["Pearl","Python","Java"])
print(s)
print(x)
print(y2)

s.add(8)
print(s)

s.discard(8)
print(s)

print(s.intersection(y2))

q=s.difference(y2)
print(q)

'''STRINGS'''

s="Pyhton"
p="!!!!"
print(s.join(p))
print("$_a".join((s," ",p)))
print("#_b".join((s[0:3],p,s[3:])))

s="Iceland&Sweden"
s=s.replace('e','E',2)
print(s)

s="Iceland is the most beautiful country."
s=s.split(" ")
print(s)

v="This tour offers a unique kayaking adventure on the pristine waters of the Jökulsárlón Glacier Lagoon in Vatnajökull National Park.\nHighlights include gliding safely past floating icebergs with panoramic views of surrounding majestic glaciers and rugged mountains.\nThe adventure uses highly stable, beginner-friendly SIT-ON-TOP kayaks and emphasizes eco-conscious travel within this breathtaking natural environment."
print(v)
v=v.splitlines()
print(v)
print("-------------------------------")
d="""This unique kayaking tour provides an intimate,
 eco-friendly adventure on the serene waters of the Jökulsárlón Glacier Lagoon,
  located in Southeast Iceland. This tour requires you to meet the guide directly
   at the Jökulsárlón parking lot base camp."""
print(d.splitlines())

s="Iceland is the most beautiful country."
s=s.rsplit(" ",2)
print(s)

s="*********Iceland is the most beautiful country.***********"
s=s.strip("*")
print(s)

s="2112Iceland is the most beautiful country.12312"
s=s.strip("13.y2rIc")
print(s)

print('''------RegEx------''')

import re

result=re.match(r"NG","NGSwetha NG Swetha NG")
print(result)
print(result.group())
print(result.string)
print(result.span())
print(result.start())
print(result.end())
print("--------------")

result1=re.match(r"NG","Swehta NG Swetha")
print(result1)
print("---------------------")

result=re.search(r"NG","Swetha NG Swetha")
print(result)
print(result.group())
print(result.string)
print(result.span())
print(result.start())
print(result.end())
print("---------------------")

result=re.findall(r"NG","Swetha NG Swngetha rgsrg nGfr qrty NG nucrty",re.I)
print(result)
print("---------------------")

result=re.split(r"NG","Swetha NG Swngetha rgsrg nGfr qrty NG nucrty",1)
print(result)
print("---------------------")

a="Python"
b="C"
c="Python is easy"
result=re.sub(a,b,c)
print(c)
print(result)
print("---------------------")

p1=re.compile("NGS")
p2=re.compile("!!!")
s="NGS is a faculty in VITNGS!!!. NGS is handling python !!!"
result=p1.findall(s)
print(result)

result=p2.findall(s)
print(result)
print("-------------------")

result=re.findall(r"P","Pyhton is easy!!!")
print(result)
result=re.findall(r"\w","Python is easy!!!")
print(result)
result=re.findall(r"\W","Python is easy!!!")
print(result)
result=re.findall(r"\s","Python is easy!!!")
print(result)
result=re.findall(r"\S","Python is easy!!!")
print(result)
print("-------------------")

s="""
Iceland
is the 
best
country!!!"""

result=re.findall(r'\n',s)
print(result)

result=re.findall(r'\d',"Python11 is22 easy 333 !!!")
print(result)
result=re.findall(r'\D',"Python11 is22 easy 333 !!!")
print(result)
result=re.findall(r'^\d',"111Python11 is22 easy 333 !!!")
print(result)
result=re.findall(r'\d$',"Python11 is22 easy 333 !!!44")
print(result)
print("-------------------")

result=re.findall(r".","Pyhton is easy!!!")
print(result)
result=re.findall(r".?","Python is easy!!!")
print(result)
result=re.findall(r".+","Python \nis easy!!!")
print(result)
result=re.findall(r".*","Python \nis easy!!!")
print(result)
result=re.findall(r"[a-z]","Python is easy!!!")
print(result)
result=re.findall(r"[a-z]?","Python is easy!!!")
print(result)
result=re.findall(r"[a-z]+","Python is easy!!!")
print(result)
result=re.findall(r"[a-z]*","Python is easy!!!")
print(result)
result=re.findall(r"[^a-z]*","Python is easy!!!")
print(result)
result=re.findall(r"[A-Za-z]{2}","Python is easyz!!!")
print(result)
print("----------------")

