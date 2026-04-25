print("Welcome to the Temperature Converter!")

celsius_input = float(input("Enter temperature in Celsius: "))

degree_f = (celsius_input * 9/5) + 32
degree_k = celsius_input + 273.15

print(f"The temperature you have entered is {celsius_input} degree Celsius.")
print("Converted Temperatures:")
print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.")
print("Thank you for using the Temperature Converter!")