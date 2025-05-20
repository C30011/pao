# Entrada de dados
nome_responsavel = input("Nome do responsável pela reserva: ")
if not nome_responsavel:
    print("Erro: O nome do responsável não pode estar vazio.")
    exit()

dia_checkin = int(input("Dia do check-in: "))
mes_checkin = int(input("Mês do check-in: "))
ano_checkin = int(input("Ano do check-in: "))

dia_checkout = int(input("Dia do check-out: "))
mes_checkout = int(input("Mês do check-out: "))
ano_checkout = int(input("Ano do check-out: "))

tipo_quarto = input("Tipo de quarto (Standard, Premium, Luxo): ")

# Validações
if ano_checkout < ano_checkin or \
   (ano_checkout == ano_checkin and mes_checkout < mes_checkin) or \
   (ano_checkout == ano_checkin and mes_checkout == mes_checkin and dia_checkout <= dia_checkin): se
    print("Erro: A data de check-out deve ser posterior à data de check-in.")
    exit()

if tipo_quarto not in ["Standard", "Premium", "Luxo"]:
    print("Erro: Tipo de quarto inválido.")
    exit()

# Cálculo do valor total da reserva
if tipo_quarto == "Standard":
    valor_diaria = 100
elif tipo_quarto == "Premium":
    valor_diaria = 180
else:  # tipo_quarto == "Luxo"
    valor_diaria = 250

# Considerando que a diferença entre as datas é em dias (simplificação)
total_dias = (ano_checkout - ano_checkin) * 365 + (mes_checkout - mes_checkin) * 30 + (dia_checkout - dia_checkin)  # Aproximação para fins do projeto
valor_total = valor_diaria * total_dias

# Saída de dados
print("\nDados da Reserva:")
print(f"Responsável: {nome_responsavel}")
print(f"Check-in: {dia_checkin}/{mes_checkin}/{ano_checkin}")
print(f"Check-out: {dia_checkout}/{mes_checkout}/{ano_checkout}")
print(f"Tipo de Quarto: {tipo_quarto}")
print(f"Valor Total: R$ {valor_total:.2f}")
