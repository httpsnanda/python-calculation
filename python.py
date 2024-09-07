def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Exemplo de uso
num = int(input("Informe um número: "))
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
    faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())

percentual = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

for estado, perc in percentual.items():
    print(f"{estado}: {perc:.2f}%")
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Exemplo de uso
string = input("Informe uma string: ")
print("String invertida:", inverter_string(string))
