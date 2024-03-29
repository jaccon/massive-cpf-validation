# Relatório de Validação de CPF

Este é um projeto simples que valida CPFs (Cadastro de Pessoas Físicas) utilizando Python. O projeto inclui um script que lê um arquivo CSV contendo CPFs e gera um relatório CSV indicando se cada CPF é válido ou inválido.

## Como Funciona

O script Python lê um arquivo CSV de entrada contendo uma lista de CPFs. Em seguida, ele valida cada CPF utilizando o algoritmo de validação de CPF e gera um relatório CSV de saída indicando o CPF e seu status de validade.

## Detalhes de Implementação

O script contém duas funções principais:

### `validar_cpf(cpf)`

Esta função recebe um CPF como entrada e retorna se o CPF é válido ou inválido. O algoritmo de validação utilizado verifica se o CPF tem 11 dígitos, se não consiste em uma sequência de dígitos repetidos e, em seguida, calcula os dígitos verificadores de acordo com o algoritmo específico para CPFs.

### `gerar_relatorio(input_file, output_file)`

Esta função recebe o caminho para um arquivo CSV de entrada e o caminho para um arquivo CSV de saída. Ele lê o arquivo de entrada, valida cada CPF encontrado no arquivo e escreve um relatório CSV de saída contendo o CPF e seu status de validade.

## Uso

Para utilizar o script, você precisa fornecer um arquivo CSV contendo uma lista de CPFs. O script então gera um relatório CSV indicando o status de validade de cada CPF.

```python
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

