gpa=float(input("enter gpa"))
instapp=input("student going to same inistitution")
if gpa >3.75:
    if instapp=="yes":
        print("loan approved")
    else:
        print("application does not qualify")
else:
    print("loan rejected")
