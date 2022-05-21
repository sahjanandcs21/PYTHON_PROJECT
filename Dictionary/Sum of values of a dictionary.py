# function
def Sum(dic):
 #sum variable
    sum=0
 #iterate through values
    for i in dic.values():
        sum=sum+i
    return sum

#initialisation
dic={ 'x':30, 'y':145, 'z':55 }

print("Dictionary: ", dic)

#print_sum
print("sum: ",Sum(dic))
