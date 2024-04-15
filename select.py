import random

# Prompt the user to enter the total number of customers
total_customers = int(input("Enter the total number of customers: "))

# Initialize an empty dictionary to store customer IDs and names
customers = {}

# Prompt the user to enter the customer names
for i in range(1, total_customers + 1):
    while True:
        name = input(f"Enter the name of customer {i}: ")

        # Check if the name is at least 4 characters long and at most 24 characters long
        if len(name) < 4 or len(name) > 24:
            print("Name must be between 4 and 24 characters long.")
            continue

        # Check if the name is already in the dictionary (case sensitive)
        if name in customers.values():
            print("Name must be unique.")
            continue

        # Add the name to the dictionary with the customer ID as the key
        customers[i] = name
        break

# Prompt the user to enter the number of random customers to select
num_random_customers = int(input("Enter the number of random customers to select: "))

# Selecting random customers
random_customers = random.sample(list(customers.keys()), num_random_customers)

# Print the randomly selected customers and their names
print("Randomly selected customers:")
for customer_id in random_customers:
    print(f"Customer ID: {customer_id}, Name: {customers[customer_id]}")
