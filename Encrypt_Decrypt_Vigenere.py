alfabeto = 'abcdefghijklmnopqrstuvwxyz'

letras_especiais = 'ÁáÂâÀàÅåÃãÄäÉéÊêÈèËëÍíÎîÌìÏïÓóÔôÒòÕõÖöÚúÛûÙùÜüÇç'
letra_a = letras_especiais[0:12]
letra_e = letras_especiais[12:20]
letra_i = letras_especiais[20:28]
letra_o = letras_especiais[28:38]
letra_u = letras_especiais[38:46]
letra_c_cedilha = letras_especiais[46:]

iniciador = 0
finalizador = 999999999999

def creditos(crdt):
    print()
    print('*'*120)
    print('Projeto de Criptografia e Descriptografia de Mensagens')
    print()
    print('Criador: SavioSayke')
    print('*'*120)
    print()
    print('Retornar ao Menu - R')
    ex = input('Digite a opção correspondente: ')
    if ex == 'R' or ex == 'r':
        return ex
    else:
        print('Retornar ao Menu Inicial - R')
        return creditos_loop(ex)


def creditos_loop(ex):
    exi = input()
    if exi == 'R' or exi == 'r':
        return exi
    else:
        print('Retornar ao Menu Inicial - R')
        return creditos_loop(exi)


def criptografar(mensagem):
    mensagem_criptografada = ''
    cont = 0
    for letra in mensagem:
        letra = letra.lower()
        if letra == ' ':
            mensagem_criptografada = (mensagem_criptografada + letra)
        elif letra not in alfabeto:
            mensagem_criptografada = (mensagem_criptografada + letra)
        else:
            posicao_letra_mensagem = alfabeto.find(letra)
            posicao_letra_chave = alfabeto.find(chave_formatada[cont%len(chave_formatada)])
            cifrar_letra = (posicao_letra_mensagem + posicao_letra_chave)
            mod = int(cifrar_letra) % len(alfabeto)
            mensagem_criptografada = (mensagem_criptografada + str(alfabeto[mod]))
            cont = (cont + 1)
    return mensagem_criptografada


def descriptografar(mensagem):
    mensagem_descriptografada = ''
    cont = 0
    for letra in mensagem:
        letra = letra.lower()
        if letra == ' ':
            mensagem_descriptografada = (mensagem_descriptografada + letra)
        elif letra not in alfabeto:
            mensagem_descriptografada = (mensagem_descriptografada + letra)
        else:
            posicao_letra_mensagem = alfabeto.find(letra)
            posicao_letra_chave = alfabeto.find(chave_formatada[cont%len(chave_formatada)])
            decifrar_letra = (posicao_letra_mensagem - posicao_letra_chave + 26)
            mod = int(decifrar_letra) % len(alfabeto)
            mensagem_descriptografada = (mensagem_descriptografada + str(alfabeto[mod]))
            cont = (cont + 1)
    return mensagem_descriptografada


def verificar_chave(c):
    chave = ''
    for letra in c:
        if letra not in alfabeto and letra not in letras_especiais:
            return chave_loop(c)
        else:
            chave = (chave + letra)
    return chave


def chave_loop(c):
    print('.'*120)
    print('ERRO...Digite uma chave sem utilizar caracteres especiais, simbolos ou numeros, apenas letras do alfabeto brasileiro!')
    chave = input('Digite uma chave para criptografar sua mensagem: ')
    return verificar_chave(chave)


def formatacao_c(e):
    if e == '1':
        print()
        print('='*120)
        x = c_final.upper()
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    elif e == '2':
        print()
        print('='*120)
        x = c_final.lower()
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    elif e == '3':
        print()
        print('='*120)
        x = c_final.upper().replace(' ', '')
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    elif e == '4':
        print()
        print('='*120)
        x = c_final.lower().replace(' ', '')
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    else:
        x = formatacao_c_loop(e)


def formatacao_d(e):
    if e == '1':
        print()
        print('='*120)
        x = d_final.upper()
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    elif e == '2':
        print()
        print('='*120)
        x = d_final.lower()
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    elif e == '3':
        print()
        print('='*120)
        x = d_final.upper().replace(' ', '')
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    elif e == '4':
        print()
        print('='*120)
        x = d_final.lower().replace(' ', '')
        print('Mensagem Criptografada: {}'.format(x))
        print('='*120)
    else:
        x = formatacao_d_loop(e)


def formatacao_m(m,e):
    if e == '1':
        print()
        print('='*120)
        x = m.upper()
        print('Mensagem Formatada: {}'.format(x))
        print('='*120)
    elif e == '2':
        print()
        print('='*120)
        x = m.lower()
        print('Mensagem Formatada: {}'.format(x))
        print('='*120)
    elif e == '3':
        print()
        print('='*120)
        x = m.upper().replace(' ', '')
        print('Mensagem Formatada: {}'.format(x))
        print('='*120)
    elif e == '4':
        print()
        print('='*120)
        x = m.lower().replace(' ', '')
        print('Mensagem Formatada: {}'.format(x))
        print('='*120)
    else:
        x = formatacao_m_loop(e)


def formatacao_c_loop(f):
    print()
    print('-'*120)
    print('ERRO...Digite uma opcao valida!')
    print('-'*120)
    print()
    escolha = input('Digite a opcao correspondente: ')
    if escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4':
        return formatacao_c_loop(escolha)
    else:
        return formatacao_c(escolha)


def formatacao_d_loop(f):
    print()
    print('-'*120)
    print('ERRO...Digite uma opcao valida!')
    print('-'*120)
    print()
    escolha = input('Digite a opcao correspondente: ')
    if escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4':
        return formatacao_d_loop(escolha)
    else:
        return formatacao_d(escolha)


def formatacao_m_loop(f):
    print()
    print('-'*120)
    print('ERRO...Digite uma opcao valida!')
    print('-'*120)
    print()
    escolha = input('Digite a opcao correspondente: ')
    if escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4':
        return formatacao_m_loop(escolha)
    else:
        return formatacao_m(mensagem,escolha)


mensagem_inicio = '        Criptografia e Descriptografia de Mensagens          '

for i in range(1):
    print()
    print('-'*(len(mensagem_inicio)))
    print(mensagem_inicio)
    print('-'*(len(mensagem_inicio)))
    print()
    print('Bem-vindo! Para acessar as opcoes deste programa, digite o numero correspondente e aperte Enter.')
    print()

while iniciador < finalizador:
    print('Criptografar ou Descriptografar mensagens - Digite 1')
    print('Formatacao de mensagem - Digite 2')
    print('Informacoes importantes - Digite 3')
    print('Creditos - Digite 4')
    print('Sair - Digite 5')
    print()
    comando = input('Digite em qual opcao deseja navegar: ')
    if comando == '1':
        print()
        print('-'*120)
        print('Bem-vindo ao Menu Principal, aqui você pode escolher se deseja Criptografar ou Descriptografar sua mensagem!')
        print()
        print('Criptografar - Digite C')
        print('Descriptografar - Digite D')
        print()
        cript_ou_descript = input('Selecione se deseja Criptografar ou Descriptografar a sua mensagem: ')
        print('-'*120)
        if cript_ou_descript == 'C' or cript_ou_descript == 'c':
            print()
            print('.'*120)
            mensagem_original = input('Digite a mensagem na qual deseja criptografar: ')
            mensagem_formatada = ''
            for letra_mensagem in mensagem_original:
                if letra_mensagem in letra_a:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'A'
                    else:
                        letra_mensagem = 'a'
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
                elif letra_mensagem in letra_e:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'E'
                    else:
                        letra_mensagem = 'e'
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
                elif letra_mensagem in letra_i:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'I'
                    else:
                        letra_mensagem = 'i'
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
                elif letra_mensagem in letra_o:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'O'
                    else:
                        letra_mensagem = 'o'
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
                elif letra_mensagem in letra_u:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'U'
                    else:
                        letra_mensagem = 'u'
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
                elif letra_mensagem in letra_c_cedilha:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'C'
                    else:
                        letra_mensagem = 'c'
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
                else:
                    mensagem_formatada = (mensagem_formatada + letra_mensagem)
            chave_original = input('Digite uma chave para criptografar sua mensagem: ').lower()
            chave_f = ''
            for letra_chave in chave_original:
                if letra_chave in letra_a:
                    letra_chave = 'a'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_e:
                    letra_chave = 'e'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_i:
                    letra_chave = 'i'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_o:
                    letra_chave = 'o'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_u:
                    letra_chave = 'u'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_c_cedilha:
                    letra_chave = 'c'
                    chave_f = (chave_f + letra_chave)
                else:
                    chave_f = (chave_f + letra_chave)
            chave_formatada = verificar_chave(chave_f)
            print('.'*120)
            print()
            c = criptografar(mensagem_formatada)
            c_final = ''
            for i in range (len(mensagem_formatada)):
                if mensagem_formatada[i] == mensagem_formatada[i].upper():
                    c_final = (c_final + c[i].upper())
                else:
                    c_final = (c_final + c[i].lower())
            print('='*120)
            print('Mensagem Criptografada: {}'.format(c_final))
            print('='*120)
            print()
            print('-'*120)
            print('Bem-vindo as opcoes de formatacao de mensagem criptografada!')
            print()
            print('Deseja formatar a sua mensagem criptografada?')
            print()
            print('Sim - Digite S')
            print('Não - Digite qualquer outra letra, número ou caractere especial')
            print()
            escolha_formatacao = input('Digite a opcao correspondente: ')
            print('-'*120)
            if escolha_formatacao == 'S' or escolha_formatacao == 's':
                print()
                print('Qual das formatações deseja utilizar?')
                print()
                print('Mensagem original maiuscula - 1')
                print('Mensagem original minuscula - 2')
                print('Mensagem original maiuscula sem espaços - 3')
                print('Mensagem original minuscula sem espaços - 4')
                print()
                escolha_opcao = input('Digite a opcao correspondente: ')
                resultado_escolha = formatacao_c(escolha_opcao)
                print()
                print('-'*120)
                print('Deseja retornar ao Menu Inicial?')
                print('Sim - Digite S')
                print('Não - Digite qualquer letra, numero ou caractere especial')
                print()
                retornar_ou_n = input('Digite a opcao correspondente: ')
                print('-'*120)
                print()
                if retornar_ou_n == 'S' or retornar_ou_n == 's':
                    iniciador = (iniciador + 1)
                else:
                    print()
                    print('*'*120)
                    print('Obrigado por usar este programa, espero ter ajudado!')
                    print('*'*120)
                    break
            else:
                print()
                print('Deseja retornar ao Menu Inicial?')
                print('Sim - Digite S')
                print('Não - Digite qualquer letra, numero ou caractere especial')
                print()
                retornar_ou_n = input('Digite a opcao correspondente: ')
                print('-'*120)
                print()
                if retornar_ou_n == 'S' or retornar_ou_n == 's':
                    iniciador = (iniciador + 1)
                else:
                    print()
                    print('*'*120)
                    print('Obrigado por usar este programa, espero ter ajudado!')
                    print('*'*120)
                    break
        elif cript_ou_descript == 'D' or cript_ou_descript == 'd':
            print()
            print('.'*120)
            mensagem_original_cript = input('Digite a mensagem na qual foi criptografada para descriptografar: ')
            mensagem_formatada_cript = ''
            for letra_mensagem in mensagem_original_cript:
                if letra_mensagem in letra_a:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'A'
                    else:
                        letra_mensagem = 'a'
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
                elif letra_mensagem in letra_e:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'E'
                    else:
                        letra_mensagem = 'e'
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
                elif letra_mensagem in letra_i:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'I'
                    else:
                        letra_mensagem = 'i'
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
                elif letra_mensagem in letra_o:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'O'
                    else:
                        letra_mensagem = 'o'
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
                elif letra_mensagem in letra_u:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'U'
                    else:
                        letra_mensagem = 'u'
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
                elif letra_mensagem in letra_c_cedilha:
                    if letra_mensagem.isupper() == True:
                        letra_mensagem = 'C'
                    else:
                        letra_mensagem = 'c'
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
                else:
                    mensagem_formatada_cript = (mensagem_formatada_cript + letra_mensagem)
            chave_original = input('Digite a chave utilizada para criptografar sua mensagem: ').lower()
            chave_f = ''
            for letra_chave in chave_original:
                if letra_chave in letra_a:
                    letra_chave = 'a'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_e:
                    letra_chave = 'e'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_i:
                    letra_chave = 'i'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_o:
                    letra_chave = 'o'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_u:
                    letra_chave = 'u'
                    chave_f = (chave_f + letra_chave)
                elif letra_chave in letra_c_cedilha:
                    letra_chave = 'c'
                    chave_f = (chave_f + letra_chave)
                else:
                    chave_f = (chave_f + letra_chave)
            chave_formatada = verificar_chave(chave_f)
            print('.'*120)
            print()
            d = descriptografar(mensagem_original_cript)
            d_final = ''
            for i in range(len(mensagem_formatada_cript)):
                if mensagem_formatada_cript[i] == mensagem_formatada_cript[i].upper():
                    d_final = (d_final + d[i].upper())
                else:
                    d_final = (d_final + d[i].lower())
            print('='*120)
            print('Mensagem Criptografada: {}'.format(d_final))
            print('='*120)
            print()
            print('-'*120)
            print('Bem-vindo as opcoes de formatação de mensagem descriptografada!')
            print()
            print('Deseja formatar a sua mensagem descriptografada?')
            print()
            print('Sim - Digite S')
            print('Não - Digite qualquer outra letra, numero ou caractere especial')
            print()
            escolha_formatacao = input('Digite a opção correspondente: ')
            print('-'*120)
            if escolha_formatacao == 'S' or escolha_formatacao == 's':
                print()
                print('Qual das formatações deseja utilizar?')
                print()
                print('Mensagem original maiuscula - 1')
                print('Mensagem original minuscula - 2')
                print('Mensagem original maiuscula sem espaços - 3')
                print('Mensagem original minuscula sem espaços - 4')
                print()
                escolha_opcao = input('Digite a opcao correspondente: ')
                resultado_escolha = formatacao_d(escolha_opcao)
                print()
                print('-'*120)
                print('Deseja retornar ao Menu Inicial?')
                print('Sim - Digite S')
                print('Não - Digite qualquer letra, numero ou caractere especial')
                print()
                retornar_ou_n = input('Digite a opcao correspondente: ')
                print('-'*120)
                print()
                if retornar_ou_n == 'S' or retornar_ou_n == 's':
                    iniciador = (iniciador + 1)
                else:
                    print()
                    print('*'*120)
                    print('Obrigado por usar este programa, espero ter ajudado!')
                    print('*'*120)
                    break
            else:
                print()
                print('Deseja retornar ao Menu Inicial?')
                print('Sim - Digite S')
                print('Não - Digite qualquer letra, numero ou caractere especial')
                print()
                retornar_ou_n = input('Digite a opcao correspondente: ')
                print('-'*120)
                print()
                if retornar_ou_n == 'S' or retornar_ou_n == 's':
                    iniciador = (iniciador + 1)
                else:
                    print()
                    print('*'*120)
                    print('Obrigado por usar este programa, espero ter ajudado!')
                    print('*'*120)
                    break
    elif comando == '2':
        print()
        print('Bem-vindo as opcoes de formatação de mensagem!')
        print()
        print('-'*120)
        mensagem = input('Digite sua mensagem: ')
        print('-'*120)
        print()
        print('Qual das formatações deseja utilizar?')
        print()
        print('Mensagem original maiuscula - 1')
        print('Mensagem original minuscula - 2')
        print('Mensagem original maiuscula sem espaços - 3')
        print('Mensagem original minuscula sem espaços - 4')
        print()
        escolha_opcao = input('Digite a opcao correspondente: ')
        resultado = formatacao_m(mensagem,escolha_opcao)
        print()
        print('-'*120)
        print('Deseja retornar ao Menu Inicial?')
        print('Sim - Digite S')
        print('Não - Digite qualquer letra, numero ou caractere especial')
        print()
        retornar_ou_n = input('Digite a opcao correspondente: ')
        print('-'*120)
        print()
        if retornar_ou_n == 'S' or retornar_ou_n == 's':
            iniciador = (iniciador + 1)
        else:
            print()
            print('*'*120)
            print('Obrigado por usar este programa, espero ter ajudado!')
            print('*'*120)
            break
    elif comando == '3':
        print()
        print('<>'*155)
        print()
        print('Olá! Este programa tem por funcionalidade criptografar e descriptografar mensagens utilizando um chave informada pelo usuario, essa chave sera como uma senha e, a menos que o usuario não conheça e/ou não repasse essa chave ao destinatario, não sera possivel descriptografar a mensagem utilizando este programa!')
        print()
        print('Informação 1 - Este programa ira criptografar e descriptografar mensagem utilizando a Cifra de Vigenere.')
        print('Mais informações sobre essa Cifra basta acessar: https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re ')
        print()
        print('Informação 2 - Caso a mensagem originalmente possua alguma letra com acentuacao, ao descriptografar, o programa nao exibira a mensagem com sua acentuacao antes de ser criptografada!')
        print()
        print('Informação 3 - Este programa ira criptografar apenas as letras que estiverem contidas na mensagem e que facam parte do alfabeto brasileiro, quaisquer outros caracteres serao mantidos na mensagem!')
        print()
        print('Informação 4 - Caso alguma letra da mensagem esteja com acentuacao, o programa ira converter essa letra para a mesma letra sem o acento!')
        print()
        print('<>'*155)
        print()
    elif comando == '4':
        x = creditos(comando)
    elif comando == '5':
        print()
        print('*'*120)
        print('Obrigado por usar este programa, espero ter ajudado!')
        print('*'*120)
        break
    else:
        print()
        print('-'*120)
        print('ERRO...Selecione uma opcao valida!')
        print('-'*120)
        print()