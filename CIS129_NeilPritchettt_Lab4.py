# CIS129 Lab 5 - Bottle Return Program
# Name: Neil Pritchett
# Date: March 4 2025
# Description: This program calculates the number of bottles collected over a week and the total payout.

totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0.0
keepGoing = "y"

NBR_OF_DAYS = 7
PAYOUT_PER_BOTTLE = 0.10

while keepGoing == "y":
    totalBottles = 0  
    counter = 1

    while counter <= NBR_OF_DAYS:
        print("Enter number of bottles returned for day #", counter, ":")
        todayBottles = int(input())
        totalBottles = totalBottles + todayBottles
        counter = counter + 1

    totalPayout = totalBottles * PAYOUT_PER_BOTTLE

    print("Total number of bottles collected: ", totalBottles)
    print("Total amount paid out: $", totalPayout)

    print("\nDo you want to enter another week's worth of data?")
    keepGoing = input("Enter y or n: ")