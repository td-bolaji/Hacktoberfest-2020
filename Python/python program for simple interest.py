''' Example:
Input : P = 10000
		R = 5
		T = 5
Output : 2500

we need to find simple interest on 10,000 at the rate of 5% for 5 years of time.
'''

P = 10000
R = 5
T = 5

#CalCulate Simple Interest

P = int(input("Input The Principle Number: "))
R = int(input("Input The Rate: "))
T = int(input("Input The Time: "))

SI =(P * R * T)/100

print("Simple Interest Is {}".format(SI))
