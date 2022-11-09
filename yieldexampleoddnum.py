def filter_odd(numbers):

   for number in range(numbers):

       if(number%2!=0):

           yield number 

odd_numbers = filter_odd(50)

print(list(odd_numbers))