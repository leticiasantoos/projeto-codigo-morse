morse_code ={".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F","--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L","--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R","...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X","-.--": "Y", "--..": "Z", "-----": 0, ".----": 1, "..---": 2, "...--": 3,"....-": 4, ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9}    
# Passo 1: Receber a entrada
frase = input("Digite a frase para converter em código Morse: ")

# Passo 3: Processar a frase
morse_result = []

for char in frase:
    if char.upper() in morse_code.values():
        morse_result.append(list(morse_code.keys())[list(morse_code.values()).index(char.upper())])
        morse_result.append(" ")  # Adiciona um espaço entre as letras
    elif char == " ":
        morse_result.append("  ")  # Adiciona dois espaços entre as palavras

# Passo 5: Exibir o resultado
morse_final = "".join(morse_result).strip()
print("Código Morse:", morse_final)
