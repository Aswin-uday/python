
#filter A

customers=['Rahul','Antony','Salman','Arun','Kiran']
A_customers=[customer for customer in customers if 'A' in customer]
print(A_customers)

##list 

I=[1,2,3,4,5]
x=list(map(lambda n:n*2,I))
print(dict(zip(I,x)))

##

words=['apple','banana','apple','orange','banana','apple']
words_count={word:words.count(word) for word in set(words)}
print(words_count)

##salary

employees={'Antony':55000,'susan':45000,'kiran':60000}
categorized_employees={name:'High' if salary > 50000 else 'low' for name, salary in employees.items()}
print(categorized_employees)

#price of items

prices=[15,25,10,30,50]
price_below_20=[price for price in prices if price < 20]
print(price_below_20)















