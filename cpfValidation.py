import csv

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return "valid"
    else:
        return "invalid"

def gerar_relatorio(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as output_csv:
        reader = csv.reader(csvfile)
        writer = csv.writer(output_csv)
        writer.writerow(['CPF', 'Status']) 

        for row in reader:
            cpf = row[0]  
            status = validar_cpf(cpf)
            writer.writerow([cpf, status])

input_file = 'data.csv'
output_file = 'relatorio.csv'
gerar_relatorio(input_file, output_file)
print("Relatório gerado com sucesso.")
