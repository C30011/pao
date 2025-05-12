nome_do_reservista = (input("Digite seu nome:"))
if nome_do_reservista == "":
    quit()
dia_checkin = int(input("Digite o dia do check-in:"))
mes_checkin = int(input("Digite o mes do check-in:"))
ano_checkin = int(input("Digite o ano do check-in:"))

dia_checkout = int(input("Digite o dia do check-out:"))
mes_checkout = int(input("Digite o mes do check-out:"))
ano_checkout = int(input("Digite o ano do check-out:"))

tipo_de_quarto = input("Tipo de quarto:(Standard,Premium,Luxo):")

if ano_checkout < ano_checkin or \
    (ano_checkin == ano_checkout and mes_checkout < mes_checkin) or \
    (ano_checkin == ano_checkout and mes_checkin == mes_checkout and dia_checkout <= dia_checkin):
    print("A data de checkout deve ser posterior da data de checkin")

if mes_checkin > 12:
    print("não exite esse mes")

