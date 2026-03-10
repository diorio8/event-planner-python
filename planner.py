#identificação
print ("configuração do evento")
nome_do_evento = input ("Qual o nome do evento?")
local_do_evento = input("Onde vai ser o evento?")

#pessoas
convidados = input ("Quem são as pessoas confirmadas?(separe por virgula):")

#valores
valor_total = float(input ("Qual o valor total que vai ser ou que foi gasto? R$"))
quantidade_pessoas = int(input("Quantas pessoas vão dividir a conta?"))

#resultado
valor_por_pessoa = valor_total / quantidade_pessoas

print("\n" + "="*30)
print(f"resumo do evento: {nome_do_evento}")
print(f"local{local_do_evento}")
print(f"convidados: {convidados}")
print(f"cada um vai pagar: R$ {valor_por_pessoa:.2f}")
print("="*30)