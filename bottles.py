# This program will print 99 bottles of beer on the wall all the way till there are no more bottles left

count = 99
while count >= 1:
    if count == 2:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer\nTake one down, pass it around")
        count = count - 1
        print(f"{count} bottle of beer on the wall!\n")
    elif count == 1:
        print(f"{count} bottle of beer on the wall")
        print(f"{count} bottle of beer\nTake one down, pass it around")
        count = count - 1
        print(f"{count} bottles of beer on the wall!\n")
    else:
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer\nTake one down, pass it around")
        count = count - 1
        print(f"{count} bottles of beer on the wall!\n")
