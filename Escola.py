import math

print("==== BEM VINDO A ESCOLA ====")

tip = str(input("Informe o tipo de acesso ALUNO ou PROFESSOR: "))

if tip == "aluno":
    print("==== REALIZE O SEU CADASTRO ====")

    nome = str(input("Informe o nome do aluno: "))
    sn = str(input("Informe o sobrenome do aluno: "))
    datan = int(input("Informe o ano de nascimento do aluno: "))
    s = (2023 - datan)
    print("Atualmento o aluno {} tem {} anos de idade ! ".format(nome, s))
    doc = float(input("informe o documento que gostaria de informar 1)RG e 2)CPF : "))

    if doc == 1:
        input("Informe o numero do seu RG: ")
    elif doc == 2:
        input("Informe o numero do seu CPF: ")

    b = str(input("Informe o bairro onde o aluno reside: "))
    muni = str(input("Informe o municipio onde o aluno reside: "))
    rua = str(input("Informe o nome da rua do aluno: "))

    mod = str(input("sr{}, Informe em qual modalidade (Primaria / Fundamental / Medio / Tecnico / Graduação)"
                    " o senhor se encontra: ".format(nome)))

    if mod == 'Primaria':
        p = int(input("sr{} , Informe em qual ANO do ensino {} o sr se encontra: ".format(nome, mod)))

    if mod == 'Fundamental':
        p = int(input("sr{} , Informe em qual SERIE do ensino {} o sr se encontra: ".format(nome, mod)))

    if mod == 'Médio':
        p = int(input("sr{} , Informe em qual ANO do ensino {} o sr se encontra: ".format(nome, mod)))

    if mod == 'Tecnico':
        p = int(input("sr{} , Informe em qual ANO do ensino {} o sr se encontra: ".format(nome, mod)))

    if mod == 'graduação':
        fac = str(input("Informe em que area é a sua graduação: "))
        p = int(input("sr{} , Informe em qual periodo da Graduação de {} o sr se encontra: ".format(nome, fac)))

    tur = str(input("sr {}, escolha entre as turmas (J1,J2,J3,J4,J5) em que turma gostaria de entrar: ".format(nome)))
    print("sr {}, o senhor será da turma {} nesse periodo na modalidade {} no periodo {}.".format(nome, tur, mod, p))
    print("== CADASTRO FINALIZADO == ',' \n == OBRIGADO == ','\n == SEJA BEM VINDO SR(A) {} =)".format(nome))

elif tip == 'professor':
    proname = str(input("Seja bem Vindo professor(a), informe o seu nome: "))
    sh = int(input("professor(a): {}, por favor Informe a sua senha: ".format(proname)))
    while sh != 123456:
        print("A senha informada esta errada !!")
        break

    if sh == 123456:
        mat = str(input("Informe a materia em que lesiona: "))
        con = str(input("sr {} informe agora o aluno(a) que gostaria de analisar: ".format(proname)))
        print("Estamos iniciando a consulta e lançamento das notas do aluno(a) {}".format(con))

        n1 = float(input("Diga a primeira nota do(a) {} :".format(con)))
        n2 = float(input("Diga a segunda nota do(a) {} :".format(con)))
        n3 = float(input("Diga a terceira nota do(a) {}".format(con)))

        media = (n1 + n2 + n3) / 3

        if media < 10.0:
            print('O aluno {} ficou com a media {:.1f} e esta REPROVADO.'.format(con, media))
        elif media >= 11.0 and media < 18.0:
            print('O aluno {} ficou com a media {:.1f} e esta de RECUPERAÇÃO.'.format(con, media))
        elif media >= 18.0:
            print('O aluno {} ficou com a media {:.1f} e foi APROVADO.'.format(con, media))
    print("professor {} a sua consulta foi finalizada !!\n volte sempre! OBRIGADO :)".format(proname))

else:
    print("A OPÇÃO ESCOLHIDA É INVALIDA :(")
