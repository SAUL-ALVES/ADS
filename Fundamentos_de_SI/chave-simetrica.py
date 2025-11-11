import random


def converteEmBinEinverteAleatorio(texto):
    
    binarios = ""
    for letra in texto:
        cod = ord(letra)
        binario = bin(cod)[2:].zfill(8)
        binarios += binario

    
    chave = "".join(random.choice("01") for _ in range(len(binarios)))

    
    xor_resultado = ""
    for b_texto, b_chave in zip(binarios, chave):
        xor_resultado += "1" if b_texto != b_chave else "0"

    
    invertido = ""
    for bit in xor_resultado:
        invertido += "1" if bit == "0" else "0"

    
    return invertido, chave



def decifrarAleatorio(texto_invertido, chave):
    
    original_xor = ""
    for bit in texto_invertido:
        original_xor += "1" if bit == "0" else "0"

    
    bin_original = ""
    for b_texto, b_chave in zip(original_xor, chave):
        bin_original += "1" if b_texto != b_chave else "0"

    
    texto_original = ""
    for i in range(0, len(bin_original), 8):
        byte = bin_original[i:i+8]
        numero = int(byte, 2)
        caractere = chr(numero)
        texto_original += caractere

    return texto_original



texto = input("Digite um texto para cifrar: ")

cifrado, chave = converteEmBinEinverteAleatorio(texto)
print("\nTexto cifrado:", cifrado)
print("Chave gerada: ", chave)

decifrado = decifrarAleatorio(cifrado, chave)
print("\nTexto decifrado:", decifrado)
