import math 


sation_name = 'Kathmandu Weather Station'
temperatures = [18.4,22.1,15.7,29.3,11.8,25.6,19.2]

def get_average(temps):
    sum = math.fsum(temps)
    count = len(temps)
    return sum/count

# mean = get_average(temps)
def get_deviation(temps):
    mean = get_average(temps)
    sum = 0.0
    n = len(temps)
    for i in range(len(temps)):
        sum = sum + math.pow(2,(temps[i]-mean))
    result = (sum/n)
    return math.sqrt(result)

def get_summary(temps):
    mean = get_average(temps)
    deviation = get_deviation(temps)
    minimum = min(temps)
    maximum = max(temps)

    print(f'Station: {sation_name}')
    print(f"The minimum temperature is {minimum}")
    print(f'The maximum temperature is {maximum}')
    print(f'The average temperature is {mean}')
    print(f'The standard deviation of the temperature is {deviation}')

get_summary(temperatures)
# Trying to call mean here causing a Nameerror because 'mean' is a local variable inside
# get deviation it only exits in that function's scope and is destroyed once the function finishes
# print(mean)