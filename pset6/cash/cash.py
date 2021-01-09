while True:
    change = input("Change owned: ")
    if change:
        if change.isalpha() == False:
            if float(change) >= 0:
                break
    
change = float(change)   
change = int(change * 100)

quarters = int(change / 25)

dimes = int((change % 25) / 10)

nickels = int(((change % 25) % 10) / 5)

pennies = int(((change % 25) % 10) % 5)

print(f"{int(quarters + dimes + nickels + pennies)}")
quit()