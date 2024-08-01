def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Digite a temperatura em Grau Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)

print(f"{celsius}°C é igual a {fahrenheit}°F")