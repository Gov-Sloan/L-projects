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

import sys

# The usd and php can be adjusted manually below, just numbers, no others.
#Also ps. put date
Usd = 0.018
Php = 55.53

def UsdToPhp():
    print('\nUsd To Php')
    while True:
        try:
            baseUsd = input('Please input Usd (press enter to exit): ').strip()
            if baseUsd == '':
                return
            baseUsd = float(baseUsd)
            multip = baseUsd * Php
            print(f"The exchange of {baseUsd} Usd will be {multip} Php")
            
        except:
            print('There is an error in the inputted data, please try again')


def PhpToUsd():
    print('\nPhp to Usd')
    while True:
        try:
            basePhp = input('Please input Php (press enter to exit): ').strip()
            if basePhp == '':
                return
            basePhp = float(basePhp)
            multi = basePhp * Usd
            print(f'The exchange of {basePhp} Php to Usd will be {multi} Usd')
            
        except:
            print('There is an error in the inputted data, please try again')


print("\nWelcome to the Php to Usd vice versa converter")

def main():
    while True:
        call = input("\nPress 1 for UsdToPhp, press 2 for PhpToUsd, or press enter to exit: ").strip()
        if call == '':
            sys.exit()
        elif call == '1':
            UsdToPhp()
        elif call == '2':
            PhpToUsd()
        else:
            print('Invalid input, please try again.')

main()