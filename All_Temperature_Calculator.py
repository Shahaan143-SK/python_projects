print("===============================")
print("   All Temperature Calculator   ")
print("===============================")
class TempCal:
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit.lower()
        self.to_unit = to_unit.lower()
    def celsius_to_fahrenheit(self,c):
        return (c * 9/5) + 32   
    def fahrenheit_to_celsius(self,f):
        return (f - 32) * 5/9   
    def celsius_to_kelvin(self,c):
        return c + 273.15   
    def kelvin_to_celsius(self,k):   
        return k - 273.15
    def fahrenheit_to_kelvin(self,f):
        return (f - 32) * 5/9 + 273.15  
    def kelvin_to_fahrenheit(self,k):
        return (k - 273.15) * 9/5 + 32
    def convert(self, temp):
        if self.from_unit in ["celsius","c"] and self.to_unit in ["fahrenheit","f"]:
            return self.celsius_to_fahrenheit(temp)
        elif self.from_unit in ["fahrenheit","f"] and self.to_unit in ["celsius","c"]:
            return self.fahrenheit_to_celsius(temp)
        elif self.from_unit in ["celsius","c"] and self.to_unit in ["kelvin","k"]:
            return self.celsius_to_kelvin(temp)
        elif self.from_unit in ["kelvin","k"] and self.to_unit in ["celsius","c"]:
            return self.kelvin_to_celsius(temp)
        elif self.from_unit in ["fahrenheit","f"] and self.to_unit in ["kelvin","k"]:
            return self.fahrenheit_to_kelvin(temp)
        elif self.from_unit in ["kelvin","k"] and self.to_unit in ["fahrenheit","f"]:
            return self.kelvin_to_fahrenheit(temp)
        elif self.from_unit == self.to_unit:
            return temp
        else:
            return "Invalid conversion units."  
    def __str__(self):
        return f"Temperature Converter from {self.from_unit} to {self.to_unit}"
# === Main Program ===  
while True:

    from_unit = input("Enter the unit you want to convert from (Celsius/C/c, Fahrenheit/F/f, Kelvin/K/k): ").strip()
    to_unit = input("Enter the unit you want to convert to (Celsius/C/ck, Fahrenheit/F/f, Kelvin/K/k): ").strip()
    try:
        temp = float(input(f"Enter the temperature in {from_unit}: "))  
        converter = TempCal(from_unit, to_unit)
        result = converter.convert(temp)    
        print(f"{temp} {from_unit} is equal to {result} {to_unit}.")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
    user_choice = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if user_choice == 'yes' or user_choice == 'y':
        continue
    elif user_choice == 'no' or user_choice == 'n':
        print("Thank you for using the All Temperature Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Exiting the program.")
        break
    




