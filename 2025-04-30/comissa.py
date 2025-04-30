valor_venda = float(input('Digite o valor da venda: '))

percentual = float(input('Informe a porcentagem da comissão: '))


comissao = (valor_venda)*(percentual/100)

print(f' O valor da comissão ficou em: {comissao:.2f}' )