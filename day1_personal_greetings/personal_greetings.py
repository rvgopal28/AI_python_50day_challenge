# Step 1: Ask user for name
name = input("Enter your name: ")

# Step 2: Ask for the recipient's name
recipient = input("Enter the recipient's name: ")

# Step 3: Create the message
message = f"""
Hi {recipient},

Hope you're doing well! Just wanted to drop a quick message and say that you're awesome 😊

Warm regards,  
{name}
"""

# Step 4: Print the message
print("\nYour personalized message:\n")
print(message)
