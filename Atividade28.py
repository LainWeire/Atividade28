# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

pro = []
e = []
z = []

for p in range(5):
    por2 = input(F"Digite o {p+1} produto:")

    q = int(input(F"Digite a quantidade do {p+1} produto:"))

    pro.append(por2)

    e.append(q)
    



    
for p in range(5):
    if e[p]==0:
        z.append(pro[p])
if z:
    print(f"Este(s) itens esta(o) com estoque zerado:   {', '.join(z)}")
else:
    print("Todos estão no estoque!")