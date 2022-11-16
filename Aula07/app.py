# def big_mac():
#     print("Sanduiche Big Mac")

# print("Inicio")
# big_mac()
# print("Fim")

def fazer_big_mac(nome):
    print(f"Sanduiche Big Mac {nome}")

# fazer_big_mac("Lucas")
# fazer_big_mac("Hytally")
# fazer_big_mac("Baby")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo, tamanho):
    print(f"{tipo} {tamanho}")

# fazer_big_mac("Lucas")
# fazer_batata("Grande")
# preparar_refrigerante("Coca", "Média")

def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)


# fazer_combo_big_mac("Lucas", "Grande", "Coca", "Média")

def soma_numeros (num1, num2):
    return num1 + num2

# resultado = soma_numeros(15, 20)
# print(resultado)

def maior_numero(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_numero = lista_num[0]
    return maior_numero

resultado = maior_numero([321, 654, 899, 789, 2, 165, -1, 52, -46, 3652, 2, 7])
print(resultado)