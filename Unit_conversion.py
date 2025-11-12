print("===============================")
print("Unit Conversion System")
print("===============================")
class UnitConverter:
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit.lower().strip()
        self.to_unit = to_unit.lower().strip()
    def convert_length(self, value):
        if self.from_unit == "meters" and self.to_unit == "feet":
            return value * 3.28084
        elif self.from_unit == "feet" and self.to_unit == "meters":
            return value / 3.28084
        elif self.from_unit == "kilometers" and self.to_unit == "miles":
            return value * 0.621371
        elif self.from_unit == "kilometers" and self.to_unit == "meters":
            return value * 1000
        elif self.from_unit == "meters" and self.to_unit == "kilometers":
            return value / 1000
        elif self.from_unit == "miles" and self.to_unit == "kilometers":
            return value / 0.621371
        elif self.from_unit == "centimeters" and self.to_unit == "inches":
            return value * 0.393701
        elif self.from_unit == "inches" and self.to_unit == "centimeters":
            return value / 0.393701
        
        else:
            return "Invalid length conversion units."
    def convert_weight(self, value):
        if self.from_unit == "kilograms" and self.to_unit == "pounds":
            return value * 2.20462
        elif self.from_unit == "pounds" and self.to_unit == "kilograms":
            return value / 2.20462
        elif self.from_unit == "grams" and self.to_unit == "ounces":
            return value * 0.035274
        elif self.from_unit == "ounces" and self.to_unit == "grams":
            return value / 0.035274
        elif self.from_unit == "tons" and self.to_unit == "kilograms":
            return value * 907.185
        elif self.from_unit == "kilograms" and self.to_unit == "tons":
            return value / 907.185
        elif self.from_unit == "grams" and self.to_unit == "kilograms":
            return value / 1000
        elif self.from_unit == "kilograms" and self.to_unit == "grams":
            return value * 1000
        elif self.from_unit == "pounds" and self.to_unit == "ounces":
            return value * 16
        elif self.from_unit == "ounces" and self.to_unit == "pounds":
            return value / 16   
        
        else:
            return "Invalid weight conversion units."
    def convert(self, value, measurement_type):
        if measurement_type.lower() == "length":
            return self.convert_length(value)
        elif measurement_type.lower() == "weight":
            return self.convert_weight(value)
        elif measurement_type.lower() == "temperature":
            return self.convert_temperature(value)
        elif measurement_type.lower() == "energy":
            return self.convert_energy(value)
        elif measurement_type.lower() == "time":
            return self.convert_time(value)
        elif measurement_type.lower() == "volume":
            return self.convert_volume(value)
        elif measurement_type.lower() == "area":
            return self.convert_area(value)
        elif measurement_type.lower() == "speed":
            return self.convert_speed(value)
        elif measurement_type.lower() == "pressure":
            return self.convert_pressure(value)
        elif measurement_type.lower() == "density":
            return self.convert_density(value)
        elif measurement_type.lower() == "power":
            return self.convert_power(value)
        elif measurement_type.lower() == "force":
            return self.convert_force(value)    
        elif measurement_type.lower() == "frequency":
            return self.convert_frequency(value)
        elif measurement_type.lower() == "voltage":
            return self.convert_voltage(value)
        elif measurement_type.lower() == "current":
            return self.convert_current(value)
        elif measurement_type.lower() == "data":
            return self.convert_data(value)
        else:
            return "Invalid measurement type."
    def convert_temperature(self, value):
        if self.from_unit == "celsius" and self.to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif self.from_unit == "fahrenheit" and self.to_unit == "celsius":
            return (value - 32) * 5/9
        elif self.from_unit == "celsius" and self.to_unit == "kelvin":
            return value + 273.15
        elif self.from_unit == "kelvin" and self.to_unit == "celsius":
            return value - 273.15
        elif self.from_unit == "fahrenheit" and self.to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif self.from_unit == "kelvin" and self.to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return "Invalid temperature conversion units."
    def convert_energy(self, value):
        if self.from_unit == "joules" and self.to_unit == "calories":
            return value * 0.239006
        elif self.from_unit == "calories" and self.to_unit == "joules":
            return value / 0.239006
        elif self.from_unit == "kilojoules" and self.to_unit == "calories":
            return value * 239.006
        elif self.from_unit == "calories" and self.to_unit == "kilojoules":
            return value / 239.006
        elif self.from_unit == "joules" and self.to_unit == "kilojoules":
            return value / 1000
        elif self.from_unit == "kilojoules" and self.to_unit == "joules":
            return value * 1000
        else:
            return "Invalid energy conversion units."
    def convert_time(self, value):
        if self.from_unit == "seconds" and self.to_unit == "minutes":
            return value / 60
        elif self.from_unit == "minutes" and self.to_unit == "seconds":
            return value * 60
        elif self.from_unit == "hours" and self.to_unit == "minutes":
            return value * 60
        elif self.from_unit == "minutes" and self.to_unit == "hours":
            return value / 60
        elif self.from_unit == "hours" and self.to_unit == "seconds":
            return value * 3600
        elif self.from_unit == "seconds" and self.to_unit == "hours":
            return value / 3600
        else:
            return "Invalid time conversion units."
    def convert_volume(self, value):
        if self.from_unit == "liters" and self.to_unit == "gallons":
            return value * 0.264172
        elif self.from_unit == "gallons" and self.to_unit == "liters":
            return value / 0.264172
        elif self.from_unit == "milliliters" and self.to_unit == "liters":
            return value / 1000
        elif self.from_unit == "liters" and self.to_unit == "milliliters":
            return value * 1000
        elif self.from_unit == "cups" and self.to_unit == "liters":
            return value * 0.24
        elif self.from_unit == "liters" and self.to_unit == "cups":
            return value / 0.24
        else:
            return "Invalid volume conversion units."
    def convert_area(self, value):
        if self.from_unit == "square meters" and self.to_unit == "square feet":
            return value * 10.7639
        elif self.from_unit == "square feet" and self.to_unit == "square meters":
            return value / 10.7639
        elif self.from_unit == "square kilometers" and self.to_unit == "square miles":
            return value * 0.386102
        elif self.from_unit == "square miles" and self.to_unit == "square kilometers":
            return value / 0.386102
        elif self.from_unit == "acres" and self.to_unit == "square meters":
            return value * 4046.86
        elif self.from_unit == "square meters" and self.to_unit == "acres":
            return value / 4046.86
        else:
            return "Invalid area conversion units."
    def convert_speed(self, value):
        if self.from_unit == "meters per second" and self.to_unit == "kilometers per hour":
            return value * 3.6
        elif self.from_unit == "kilometers per hour" and self.to_unit == "meters per second":
            return value / 3.6
        elif self.from_unit == "miles per hour" and self.to_unit == "kilometers per hour":
            return value * 1.60934
        elif self.from_unit == "kilometers per hour" and self.to_unit == "miles per hour":
            return value / 1.60934
        elif self.from_unit == "meters per second" and self.to_unit == "miles per hour":
            return value * 2.23694
        elif self.from_unit == "miles per hour" and self.to_unit == "meters per second":
            return value / 2.23694
        else:
            return "Invalid speed conversion units."
    def convert_pressure(self, value):
        if self.from_unit == "pascals" and self.to_unit == "bars":
            return value / 100000
        elif self.from_unit == "bars" and self.to_unit == "pascals":
            return value * 100000
        elif self.from_unit == "psi" and self.to_unit == "pascals":
            return value * 6894.76
        elif self.from_unit == "pascals" and self.to_unit == "psi":
            return value / 6894.76
        elif self.from_unit == "bars" and self.to_unit == "psi":
            return value * 14.5038
        elif self.from_unit == "psi" and self.to_unit == "bars":
            return value / 14.5038
        else:
            return "Invalid pressure conversion units."
    def convert_density(self, value):
        if self.from_unit == "kilograms per cubic meter" and self.to_unit == "grams per cubic centimeter":
            return value / 1000
        elif self.from_unit == "grams per cubic centimeter" and self.to_unit == "kilograms per cubic meter":
            return value * 1000
        elif self.from_unit == "pounds per cubic foot" and self.to_unit == "kilograms per cubic meter":
            return value * 16.0185
        elif self.from_unit == "kilograms per cubic meter" and self.to_unit == "pounds per cubic foot":
            return value / 16.0185
        else:
            return "Invalid density conversion units."
    def convert_power(self, value):
        if self.from_unit == "watts" and self.to_unit == "horsepower":
            return value / 745.7
        elif self.from_unit == "horsepower" and self.to_unit == "watts":
            return value * 745.7
        else:
            return "Invalid power conversion units."
    def convert_force(self, value):
        if self.from_unit == "newtons" and self.to_unit == "pounds-force":
            return value * 0.224809
        elif self.from_unit == "pounds-force" and self.to_unit == "newtons":
            return value / 0.224809
        else:
            return "Invalid force conversion units."
    def convert_frequency(self, value):
        if self.from_unit == "hertz" and self.to_unit == "kilohertz":
            return value / 1000
        elif self.from_unit == "kilohertz" and self.to_unit == "hertz":
            return value * 1000
        else:
            return "Invalid frequency conversion units."
    def convert_voltage(self, value):
        if self.from_unit == "volts" and self.to_unit == "millivolts":
            return value * 1000
        elif self.from_unit == "millivolts" and self.to_unit == "volts":
            return value / 1000
        else:
            return "Invalid voltage conversion units."
    def convert_current(self, value):
        if self.from_unit == "amperes" and self.to_unit == "milliamperes":
            return value * 1000
        elif self.from_unit == "milliamperes" and self.to_unit == "amperes":
            return value / 1000
        else:
            return "Invalid current conversion units."
    def convert_data(self, value):
        if self.from_unit == "bytes" and self.to_unit == "kilobytes":
            return value / 1024
        elif self.from_unit == "kilobytes" and self.to_unit == "bytes":
            return value * 1024
        elif self.from_unit == "megabytes" and self.to_unit == "kilobytes":
            return value * 1024
        elif self.from_unit == "kilobytes" and self.to_unit == "megabytes":
            return value / 1024
        elif self.from_unit == "gigabytes" and self.to_unit == "megabytes":
            return value * 1024
        elif self.from_unit == "megabytes" and self.to_unit == "gigabytes":
            return value / 1024
        else:
            return "Invalid data conversion units."
    def __str__(self):
        return f"Unit Converter from {self.from_unit} to {self.to_unit}"
# === Main Program ===
while True:
    try:
        print("Available conversion types: length, weight, temperature, energy, time, volume, area, speed, pressure, density, power, force, frequency, voltage, current, data")
        measurement_type = input("Enter the measurement type you want to convert: ")
        from_unit = input("Enter the unit you want to convert from: ")
        to_unit = input("Enter the unit you want to convert to: ")  
        value = float(input(f"Enter the value in {from_unit}: "))
        converter = UnitConverter(from_unit, to_unit)
        if measurement_type.lower() == "temperature":
            result = converter.convert_temperature(value)
        else:
            result = converter.convert(value, measurement_type)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    except ValueError:
        print("Enter a valid numeric value.Please try again. ")
    user_choice = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if user_choice == 'yes' or user_choice == 'y':
        continue
    elif user_choice == 'no' or user_choice == 'n':
        print("Thank you for using the Unit Conversion System. Goodbye!")
        break   
    else:
        print("Invalid choice. Exiting the program.")
        break

        
        