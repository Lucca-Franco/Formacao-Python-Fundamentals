texto = input("Informe um texto: ")
VOGAIS = "aeiouAEIOU"

conta_vogais = 0

for letra in texto:
    if letra in VOGAIS:
        conta_vogais += (1)

print(f"O número de vogais na string '{texto}' é: {conta_vogais}")
