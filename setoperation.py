def dup(d):
    list1=[]
    for i in d:
        if i not in list1:
            list1.append(i)
    return list1

def intersection(list1,list2):
    list3=[]
    for a in list1:
        if a in list2:
            list3.append(a)
    return list3

def union(list1,list2):
    list3=list1.copy()
    for a in list2:
        if a not in list3:
            list3.append(a)
    return list3

def difference(list1,list2):
    list3=[]
    for a in list1:
        if a not in list2:
            list3.append(a)
    return list3

def symmetric_difference(list1,list2):
    list3=[]
    d1=difference(list1,list2)
    d2=difference(list2,list1)
    list3=union(d1,d2)
    return list3

def func1(list1,list2):
    list3=intersection(list1,list2)
    print("The number of students who play both cricket and badminton are:-",len(list3))
    
def func2(list1,list2):
    list3=symmetric_difference(list1,list2)
    print("The number of students who either cricket or badminton:-",len(list3))
    
def func3(list1,list2):
    list3=intersection(list1,list2)
    list4=[]
    result=len(SE)-len(list1)-len(list2)+len(list3)
    print("Students who play neither cricket nor badminton are:",result)
    
def func4(list1,list2,list3):
    list4=difference(intersection(list1,list2),list3)
    print("The students who play both cricket and football but not badminton:-",len(list4))

SE=[]
n=int(input("Enter number of students:-"))
for i in range(0,n):
    name=input("Enter names")
    SE.append(name)
print("List of student in SE comp dept:-",str(SE))

Cricket=[]
n=int(input("Enter number of students who play cricket:-"))
for i in range(0,n):
    name=input("Enter names:-")
    Cricket.append(name)
dCricket=dup(Cricket)
print("List of students who play cricket",str(dCricket))

Football=[]
n=int(input("Enter number of students who play football:-"))
for i in range(0,n):
    name=input("Enter names:-")
    Football.append(name)
dFootball=dup(Football)
print("Lis of Students who play football:-",str(dFootball))

Badminton=[]
n=int(input("Enter number of students who play Badminton:-"))
for i in range(0,n):
    name=input("Enter names:-")
    Badminton.append(name)
dBadminton=dup(Badminton)
print("List of Students who play badminton:-",str(dBadminton))

while(True):
    print("Choose an option")
    print("1.List of students who play both cricket and badminton")
    print("2.List of students who play either cricket or badminton")
    print("3.List of students who play neither cricket nor badminton")
    print("4.Number of students who play both cricket and football but not badminton")
    print("5.Exit")
    ch=int(input("Enter your choice"))
    if(ch==1):
        func1(Cricket,Badminton)
    if(ch==2):
        func2(Cricket,Badminton)
    if(ch==3):
        func3(Cricket,Badminton)
    if(ch==4):
        func4(Cricket,Football,Badminton)
    if(ch==5):
        exit()
    next=input("Do you want to countinue Yes(Y) or No(N)")
    Y=1
    N=2
    if(next=='N'):
        break
    if(next=='Y'):
        continue
    