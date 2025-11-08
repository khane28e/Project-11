unit = input("is this temperature Celsius or Fahrenheit? (C/F):")

temp = float(input("enter the temperature:"))

if unit == "C":
  temp = round((temp * 9) / 5 + 32, 1)
  print(f"your temperature is {temp}°F")

elif unit == "F":
  temp = round((temp - 32) * 5 / 9, 1)
  print(f"your temperature is {temp}°C")

else:
  print(f"{unit} is Not invalid Unit!  ")