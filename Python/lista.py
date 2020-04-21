import csv

arquivo = open('barcodes.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha[1])