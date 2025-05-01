def linear(arr,x):
      for i in range(len(arr)):
            if arr[i]==x:
                  return True
      return False

def sentinel(arr,x):
      n=len(arr)
      last=arr[-1]
      arr[-1]=x
      
      i=0
      while arr[i]!=x:
            i+=1
            
      arr[-1]=last
      
      if i<n-1 or arr[-1]==x:
            return True
      return False

roll=[]
n=int(input("Enter number of students:-"))
print("Enter roll number of students:-")
for _ in range(n):
      r=int(input())
      roll.append(r)
key=int(input("Enter roll number to search:-"))
if(linear(roll,key)):
      print("Student attended(Linear)")
else:
      print("Student not attended(Linear)")
if(sentinel(roll,key)):
      print("Student attended(Sentinel)")
else:
      print("Student not attended(Sentinel)")