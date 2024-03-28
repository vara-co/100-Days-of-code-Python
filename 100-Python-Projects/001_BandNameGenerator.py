#1. Create a greeting for your program.
print("Hello future rockstar!\n")
print('This is a "Band Name" generator!\nTo generate a cool name for your band, just follow the instructions below.\n')
print('Instructions: Answer the questions and check out your new "Band Name"!\n')

#2. Ask the user for the city that they grew up in.
# Add the \n at the end of your string, so that the input goes to the next line.
cityName = input("What city did you grow up in?\n")

#3. Ask the user for the name of a pet.
# Add the \n at the end of your string, so that the input goes to the next line.
petName = input("What would be a cool pet name?\n")

#4. Combine the name of their city and pet and show them their band name.
print(f"The name for your awesome new band would be {cityName + " " + petName}! Nicely done!\n")

#5. Make sure the input cursor shows on a new line:
# This was done by using \n at the end of the text before closing the string.
