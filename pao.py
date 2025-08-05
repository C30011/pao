from datetime import datetime

disponivel = {"Standard": 10, "Premium": 5, "Luxo": 3}
total_reservas = soma_valores = maior_valor = maior_dias = 0
resp_maior_valor = resp_maior_duracao = ""

while True:
    nome = input("\nNome do responsável: ")
    if not nome or nome[0].isdigit():
        print("Erro: Nome inválido.")
        break

    while True:
        try:
            ci = datetime.strptime(input("Check-in (dd/mm/aaaa): "), "%d/%m/%Y")
            co = datetime.strptime(input("Check-out (dd/mm/aaaa): "), "%d/%m/%Y")
            if co <= ci: print("Erro: Check-out inválido."); break
        except: print("Erro: Data inválida."); break

        tipo = input("Tipo de quarto (Standard, Premium, Luxo): ")
        if tipo not in disponivel: print("Erro: Tipo inválido."); break

        try:
            qtd = int(input("Quantidade de quartos: "))
            if qtd <= 0 or qtd > disponivel[tipo]:
                print("Erro: Quantidade inválida ou indisponível."); break
        except: print("Erro: Valor inválido."); break

        dias = (co - ci).days
        diaria = {"Standard": 100, "Premium": 180, "Luxo": 250}[tipo]
        total = diaria * dias * qtd

        # Atualizações
        total_reservas += 1
        soma_valores += total
        if total > maior_valor: maior_valor, resp_maior_valor = total, nome
        if dias > maior_dias: maior_dias, resp_maior_duracao = dias, nome
        disponivel[tipo] -= qtd

        # Saída
        print(f"\n✅ Reserva de {nome}")
        print(f"Check-in: {ci.strftime('%d/%m/%Y')} | Check-out: {co.strftime('%d/%m/%Y')}")
        print(f"Dias: {dias} | Tipo: {tipo} | Quartos: {qtd} | Total: R$ {total:.2f}")

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