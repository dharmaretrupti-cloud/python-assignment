

# x = [200,150,300,400,100,250,350]
# Expense = sum(x)
# print("Expense=", Expense)
# output :1750

# x = [200,150,300,400,100,250,350]
# Average = sum(x)/len(x)
# print("Average=",Average)
# output :250.0

# x= [200,150,300,400,100,250,350]
# highest = max(x)
# lowest =min(x)
# print("Highest expense=",highest)
# print("Lowest expense=",lowest)
# output :highest expense = 400
# output :lowest expense = 100

# expenses = [200, 150, 300, 400, 100, 250, 350]
# average = sum(expenses) / len(expenses)
# count = sum(1 for expense in expenses if expense > average)
# print("Days above average:", count)
# output= 4


x = [200,150,300,400,100,250,350]
if sum(x) > 1500:
    print("Saving Needed")
else:
    print("No")