def selction_sort(arr):
      n=len(arr)
      for i in range(n):
            min_idx=i
            for j in range(i+1,n):
                  if arr[j]<arr[min_idx]:
                        min_idx=j
            arr[i],arr[min_idx]=arr[min_idx],arr[i]
            
def bubble_sort(arr):
      n=len(arr)
      for i in range(n):
            for j in range(n-i-1):
                  if arr[j]>arr[j+1]:
                        arr[j],arr[j+1]=arr[j+1],arr[j]
                        
percentages=[]

n=int(input("Enter number of studentss:-"))
print("Enter marks of students:-")
for i in range(n):

      p=float(input())
      percentages.append(p)

sel=percentages.copy()
selction_sort(sel)
print("initial sorting of students:-",sel)
print("Top 5 scorers:-",sel[-5:][::-1])

bub=percentages.copy()
bubble_sort(bub)
print("initial sorting of students:-",bub)
print("Top 5 scorers:-",bub[-5:][::-1])