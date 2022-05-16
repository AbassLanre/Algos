               
def get_prime_numbers(start, stop) :
    prime_numbers=[]
    for i in range(start,stop):
        if i == 2 or i == 3 or i == 5 or i == 7:
            prime_numbers.append(i)
        elif i > 1:
            if i%2 ==0 or i%3 ==0 or i%5 ==0 or i%7 ==0 :
                continue
            else:
                prime_numbers.append(i)
    return prime_numbers
print(get_prime_numbers(10,50))