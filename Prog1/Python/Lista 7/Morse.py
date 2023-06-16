def decodificador(cod_morse):
    resposta = ""
    letras = cod_morse.split("...")
    for letra in letras:
        resposta += tabela_morse[letra.replace(".", ",").replace("===", "-").replace("=", ".").replace(",", "")]
    return resposta


tabela_morse = dict({'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
                     '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                     '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                     '-.--': 'y', '--..': 'z'})


casos_teste = int(input())
for i in range(casos_teste):
    conj_resp_final = []
    frase_cod = input().split(".....")
    for palavra in frase_cod:
        conj_resp_final.append(decodificador(palavra))
    print(" ".join(conj_resp_final))