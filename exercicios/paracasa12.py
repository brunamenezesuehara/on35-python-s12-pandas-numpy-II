import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configurando a seed para reprodutibilidade
np.random.seed(42)

# Gerando dados falsos
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Brinquedos']
datas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
num_registros = len(datas)

# Criando DataFrame
data = {
    'Data': np.random.choice(datas, num_registros),
    'Categoria': np.random.choice(categorias, num_registros),
    'Quantidade_Vendida': np.random.randint(1, 100, num_registros),
    'Preco_Unitario': np.round(np.random.uniform(10, 500, num_registros), 2)
}
df = pd.DataFrame(data)
df['Valor_Total'] = df['Quantidade_Vendida'] * df['Preco_Unitario']

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados_vendas.csv', index=False)

print("Conjunto de dados gerado e salvo como 'dados_vendas.csv'.")

df = pd.read_csv('dados_vendas.csv')

# Pergunta 1 
print(f"O DataFrame tem {df.shape[0]} linhas e {df.shape[1]} colunas.")
# Pergunta 2
print(df.dtypes)
print(df.head())
# Pergunta 3
categorias_unicas = df['Categoria'].unique()
print(f"Categorias únicas: {categorias_unicas}")
eletronicos = df[df['Categoria'] == 'Eletrônicos']
print(eletronicos)
# Pergunta 4
media_valor_total = eletronicos['Valor_Total'].mean()
print(f"Média do valor total das vendas de Eletrônicos: R$ {media_valor_total:.2f}")
vendas_acima_1000 = df[df['Valor_Total'] > 1000]
print(vendas_acima_1000)
#Pergunta 5
print(f"Quantidade de vendas acima de R$ 1000: {len(vendas_acima_1000)}")
total_por_categoria = df.groupby('Categoria')['Valor_Total'].sum().reset_index()
print(total_por_categoria)
# Pergunta 6
categoria_maior_venda = total_por_categoria.loc[total_por_categoria['Valor_Total'].idxmax()]
print(f"Categoria com maior valor de vendas: {categoria_maior_venda['Categoria']}")
media_quantidade_categoria = df.groupby('Categoria')['Quantidade_Vendida'].mean().reset_index()
print(media_quantidade_categoria)
# Pergunta 7
categoria_maior_media = media_quantidade_categoria.loc[media_quantidade_categoria['Quantidade_Vendida'].idxmax()]
print(f"Categoria com maior quantidade média vendida: {categoria_maior_media['Categoria']}")

plt.figure(figsize=(10, 6))
plt.bar(total_por_categoria['Categoria'], total_por_categoria['Valor_Total'], color='skyblue')
plt.xlabel('Categoria')
plt.ylabel('Valor Total de Vendas (R$)')
plt.title('Total de Vendas por Categoria')
plt.show()

# Pergunta 8
vendas_diarias = eletronicos.groupby('Data')['Valor_Total'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(vendas_diarias['Data'], vendas_diarias['Valor_Total'], color='purple')
plt.xlabel('Data')
plt.ylabel('Valor Total de Vendas (R$)')
plt.title('Variação Diária das Vendas de Eletrônicos')
plt.xticks(rotation=45)
plt.show()

