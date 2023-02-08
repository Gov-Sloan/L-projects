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
def Discount():
    while True:
        bill = input('Please input amount(press enter key to exit): ')
        if bill == '':
            print('Closing calculator,Goodbye user.')
            time.sleep(3)
            break
        if bill.isdigit():
            bill = float(bill)
            Dis = input("Please input the discount: ")
            if Dis.isdigit():
                Dis = float(Dis)
                disc = Dis / 100
                multi = bill * disc
                sub = bill - multi
                print(f"\n\tThe items' discounted price is {sub}")


            else:
                print("Please input a valid no.")
        else:
            print("input a valid no.")


Discount()