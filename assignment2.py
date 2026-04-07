

# y =[1200,1500,1100,1800,2000,1700,1600]
# total_sales = sum(y)
# print("Total weekly sales:",total_sales)
# output :10900

# average = sum(y)/len(y)
# print("Average sales:",average)
# output :1557.1428

# highest_sale = max(y)
# lowest_sale = min(y)
# print("highest sale day:",highest_sale)
# print("lowest sale day:",lowest_sale)
# output :2000,1100)

# average = sum(y)/len(y)
# count = sum(1 for sale in y if sale > average)
# print("Days above average:",count)
# output :4

sales = [1200,1500,1100,1800,2000,1700,1600]
average = sum(sales) / len(sales)

if average > 1700:
    print("Excellent")
elif 1400 <= average <= 1700:
    print("Good")
elif average <1400:
    print("Average")

