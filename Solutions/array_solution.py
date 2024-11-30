# Exercise:

l= [2200,2350,2600,2130,2190] # Given list

# 1 .-->

print(f"The money spent extra is ${l[1]-l[0]}")

# 2.-->


a= l[:3]
b= sum(a)

print(f"The expense is ${b}")

# 3.-->

for expense in l:
  if expense==2000:
    print("Yes, You spent exactly $2000 in a moth")
    break
    
  else:
    f= False

if f==False:
  print("No,You didn't")

# 4.-->

l.append(1980)
  
# 5.-->

l[2]=1830

