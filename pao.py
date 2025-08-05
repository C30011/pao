
from datetime import datetime

disponivel = {"Standard": 10, "Premium": 5, "Luxo": 3}
total_reservas = soma_valores = maior_valor = maior_dias = 0
resp_maior_valor = resp_maior_duracao = ""

while True:
    nome = input("\nNome do responsável: ")
    if not nome:
        print("Nome inválido.")
        break

    while True:
        try:
            Checkin = datetime.strptime(input("Check-in (dd/mm/aaaa): "), "%d/%m/%Y")
            Checkout = datetime.strptime(input("Check-out (dd/mm/aaaa): "), "%d/%m/%Y")
            if Checkout <= Checkin: print("Check-out inválido."); break
        except: print("Data inválida."); break

        tipo_de_Quarto = input("Tipo de quarto (Standard, Premium, Luxo): ")
        if tipo_de_Quarto not in disponivel: print("Tipo de Quarto inválido."); break

        try:
            quantidade_de_Quartos = int(input("Quantidade de quartos: "))
            if quantidade_de_Quartos <= 0 or quantidade_de_Quartos > disponivel[tipo_de_Quarto]:
                print("Quantidade inválida ou indisponível."); break
        except: print("Valor inválido."); break

        dias = (Checkout - Checkin).days
        diaria = {"Standard": 100, "Premium": 180, "Luxo": 250}[tipo_de_Quarto]
        total = diaria * dias * quantidade_de_Quartos

        # Atualizações
        total_reservas += 1
        soma_valores += total
        if total > maior_valor: maior_valor, resp_maior_valor = total, nome
        if dias > maior_dias: maior_dias, resp_maior_duracao = dias, nome
        disponivel[tipo_de_Quarto] -= quantidade_de_Quartos

        # Saída
        print(f"\n✅ Reserva de {nome}")
        print(f"Check-in: {Checkin.strftime('%d/%m/%Y')} | Check-out: {Checkout.strftime('%d/%m/%Y')}")
        print(f"Dias: {dias} | Tipo: {tipo_de_Quarto} | Quartos: {quantidade_de_Quartos} | Total: R$ {total:.2f}")

        # Menu final
        op = input("\n[1] Encerrar programa  [2] Novo cliente  [3] Nova reserva\nOpção: ")
        if op == "1": break
        elif op == "2": break
        elif op == "3": continue
        else: print("Opção inválida. Encerrando."); break
    if op == "1": break

# Estatísticas
if total_reservas:
    media = soma_valores / total_reservas
    print(f"\n📊 Estatísticas:")
    print(f"Total reservas: {total_reservas}")
    print(f"Total arrecadado: R$ {soma_valores:.2f}")
    print(f"Valor médio: R$ {media:.2f}")
    print(f"Reserva mais cara: {resp_maior_valor} - R$ {maior_valor:.2f}")
    print(f"Reserva mais longa: {resp_maior_duracao} - {maior_dias} dias")
else:
    print("\nNenhuma reserva registrada.")
