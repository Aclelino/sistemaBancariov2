from datetime import datetime as dt


def menu():

	menu_ = """

#### System Bancking ####

---#---#---

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usúario
[5] Listar Conta
[6] Nova Conta
[Q] Sair

---#---#---

=> """

	return menu_

def novo_usuario(nome,data_nascimento,endereco,cpf):

	nome = nome
	data_nascimento = data_nascimento
	endereco = endereco
	cpf = cpf

	return nome,cpf
def nova_conta(agencia,conta,usuario):

	if usuario:
	
		return {'Agencia':agencia,'Conta':conta,'Usúario':usuario}
	
def pesquisa_cpf(usuario,cpf):
	for i in usuario:
		if cpf in i.values():
			return i['nome']
	
	
def filtra_usuario(usuario ,cpf):
  
  if usuario:
  	return usuario[0]['cpf'] == cpf
  else:
    return False
  
def main():
	AGENCIA = '0001'
	CONTA = 0

	saldo = 0
	limit_day = 3
	limit = 500
	extrato = ""
	usuario = []
	conta_corrente = []


	while True:
		
		opcao = str(input(menu()))
		if opcao == "1":

			print("MENU > DEPOSITAR")
			valor = float(input("Digite o valor: "))
			saldo = saldo + valor
			print("Desposito realizado com sucesso!")
			extrato +=  "Depositado: R$ {:.2f}\n".format(valor)

		elif opcao == "2":

			print("MENU > SAQUE")
			valor = float(input("Digite o valor: "))
			if valor <= saldo:
				limit_day -= 1
				if limit_day >= 0 and valor <= limit :
					limit -= valor
					saldo = saldo - valor
					print("Saque realizado com sucesso!")
					extrato += " Saque: R$ {:.2f}\n".format(valor)
				else:
					print("Limite de saque esgotado!")
			else:
				print("Saldo Insulficiente")

		elif opcao == "3":
			print("MENU > Extrato")
			print(extrato, "\n\nSaldo disponivel: {:.2f}".format(saldo))

		elif opcao == '4':

			print("MENU > Novo Usúario")
			nome = input("Nome: ")
			data_nascimento = input("Data de Nascimento: ")
			endereco = input("Endereco: ")
			cpf = input("Cpf: ")

			if not filtra_usuario(usuario,cpf) == True:
				usuario.append({'nome':nome,'data_nascimento':data_nascimento,'endereco':endereco,'cpf':cpf})
				print('Usúario criado com sucesso!')
			else:
				print('Usuario Já Existe')
				
		elif opcao =='5':

			print('MENU > Lista Conta')

			for i in conta_corrente:
				print(i)

		elif opcao =='6':

			print('MENU > Nova Conta')
			cpf = input('Digite o seu Cpf: ')

			if usuario:
				CONTA +=1
				nome = pesquisa_cpf(usuario,cpf)
				conta_corrente.append(nova_conta(AGENCIA,CONTA,nome))
				print('Nova conta Salvo com Sucesso')
			else:
				print('Conta de Usuario não existe!')
			
			print(conta_corrente)
			

		elif opcao.lower() == "q":
			print("Tchau")
			break


main()