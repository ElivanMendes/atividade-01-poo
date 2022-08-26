salary = float(input("Informe o Salario: "))
installment_value = float(input("Informe o Valor da Prestação: "))

if installment_value / salary > 0.2:
    print("Emprestimo Não Concedido!")
else:
    print("Emprestimo Concedido!")
