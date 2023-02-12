import time
CurrentTime = time.ctime()
time_parts = time.strptime(CurrentTime)

day = time_parts.tm_mday
month = time_parts.tm_mon
year = time_parts.tm_year
hour = time_parts.tm_hour
minute = time_parts.tm_min
second = time_parts.tm_sec

print("Current time:", hour, ":", minute, ":", second)
print("Current date:", day, "/", month, "/", year)


#Discount Calculator anti-error code
print('\nDiscount calculator')
while True:
     try:
        bill = input('\nPlease input price(q to exit); ').strip()
        if bill == '':
            print('Shuting down, goodbye user.')
            time.sleep(3)
            break
        bill = float(bill)
        dis = input('Input discount; ')
        dis = float(dis)

        dis = dis / 100
        multi = bill * dis
        sub = bill - multi
        print(f"\nThe items' discounted price is {sub}")


     except:
            print('Enter a number')

