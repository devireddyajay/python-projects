def rectangle(l, w, h):
    # Calculate volume
    volume = l * w * h

    print("Volume of the rectangle:", volume)


l = int(input("Enter a number for length: "))
w = int(input("Enter a number for width: "))
h = int(input("Enter a number for height: "))

# Calling the function with the provided variables l, w, and h
rectangle(l, w, h)
