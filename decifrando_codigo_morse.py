#.-  .- ..- .-.. .-  -.. .-  -.-. .- .-. --- .-.. .. -. .-  ..  -- .- .-. .- ...- .. .-.. .... --- ... .-
import os
from datetime import datetime

# Função para carregar o dicionário Morse
def load_morse_code():
    morse_code ={".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F","--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L","--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R","...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X","-.--": "Y", "--..": "Z", "-----": 0, ".----": 1, "..---": 2, "...--": 3,"....-": 4, ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9}
    return morse_code

# Função para decodificar a mensagem
def decode_morse(message, morse_dict):
    words = message.split('  ')  # Separar palavras
    decoded_message = []

    for word in words:
        letters = word.split(' ')  # Separar letras
        decoded_word = ''.join([morse_dict.get(letter, ' ') for letter in letters])
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

# Função para salvar a mensagem em um arquivo
def save_message(decoded_message, file_path):
    with open(file_path, 'a') as file:
        file.write(f"Data e Hora: {datetime.now()} | Mensagem: {decoded_message}\n")

# Função principal para executar a decodificação
def main():
    morse_dict = load_morse_code()
    message = input("Digite a mensagem em código Morse: ")
    decoded_message = decode_morse(message, morse_dict)
    
    # Definir caminho do arquivo
    file_path = os.path.join(os.getcwd(), 'decoded_messages.txt')
    
    save_message(decoded_message, file_path)
    print(f"Mensagem decodificada: {decoded_message}")
    print(f"Mensagem salva em: {file_path}")

if __name__ == "__main__":
    main()

#Mensagem01:.- .--. .-. . -. -.. . -. -.. ---   .-   -.. . -.-. .. ..-. .-. .- .-.   ..- --   -.-. --- -.. .. --. ---   -- --- .-. ... .   . --   .--. -.-- - .... --- -.
#Mensagem02:--. .-. ..- .--. ---     .-.. .- .-. .. ... ... .-   .-.. . - .. -.-. .. .-   .- .-.. .-.. .. ... --- -.   --. .-. .- ... -.-- . .-.. ..   .   . -.. .. .-.. ... --- -.
#Mensagem03: -- -... .-   -.. .- - .-   ... -.-. .. . -. -.-. .     .- -.. ...- .- -. -.-. . -..   .- -. .- .-.. -.-- - .. -.-. ...     -.. ... .-