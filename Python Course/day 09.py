
#ყოველი 5ის ჯერადი რიცხვი დავპრინტოთ 100ამდე range გამოყენებით 
 


#hardway
for i in range(1):
    print(i, "5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100")


#quickway
for i in range(0,100,5):
   print (i)









#შესაძლოა, მაგრამ იშვიათად
sqs = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

print(sqs[1::1])



