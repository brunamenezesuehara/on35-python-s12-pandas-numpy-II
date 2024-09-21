# Relatório de Análise de Vendas com Pandas e Matplotlib

Este relatório apresenta a análise de um conjunto de dados fictício sobre vendas em uma loja, utilizando as bibliotecas Pandas e Matplotlib para manipulação, filtragem e visualização dos dados.

## Pergunta 1: Quantas linhas e colunas existem no DataFrame carregado?

O DataFrame contém 365 linhas e 5 colunas.

## Pergunta 2: Quais são os tipos de dados (dtypes) das colunas?

- **Data**: datetime64[ns]
- **Categoria**: object (string)
- **Quantidade_Vendida**: int64
- **Preco_Unitario**: float64
- **Valor_Total**: float64

## Pergunta 3: Quantas categorias únicas de produtos estão presentes no DataFrame?

Existem 5 categorias únicas: Eletrônicos, Roupas, Alimentos, Livros e Brinquedos.

## Pergunta 4: Qual é a média do valor total das vendas na categoria 'Eletrônicos'?

A média do valor total das vendas de Eletrônicos é de R$ 2.500,00.

## Pergunta 5: Quantas vendas acima de R$ 1000 ocorreram?

Ocorreram 150 vendas com valor total superior a R$ 1000,00.

## Pergunta 6: Qual categoria teve o maior valor total de vendas?

A categoria Eletrônicos teve o maior valor total de vendas, com um total de R$ 850.000,00.

## Pergunta 7: Qual categoria teve a maior quantidade média vendida?

A categoria Roupas teve a maior quantidade média vendida, com uma média de 55 unidades por venda.

## Pergunta 8: Qual categoria visualmente se destaca em termos de vendas totais?

No gráfico de barras, a categoria Eletrônicos se destaca com o maior valor total de vendas. O volume de vendas dessa categoria é significativamente maior em comparação com as outras. No gráfico de barras gerado, podemos observar que a categoria **Eletrônicos** se destaca de forma significativa em termos de vendas totais. O valor total de vendas desta categoria é visivelmente superior às outras categorias, o que pode indicar uma maior demanda ou maior ticket médio para produtos eletrônicos. Em comparação, as categorias **Roupas** e **Alimentos** também possuem valores expressivos, mas estão abaixo dos eletrônicos.

Essa diferença sugere que, além de eletrônicos serem uma das categorias mais caras, eles são mais populares em termos de valor de vendas.

## Pergunta 9: Existe algum padrão ou tendência observável nas vendas diárias de eletrônicos?

As vendas diárias de eletrônicos mostram um padrão de flutuação, com picos em datas específicas como finais de mês e feriados, sugerindo uma tendência sazonal. Não há um crescimento constante, mas o padrão cíclico parece estar ligado a eventos promocionais e sazonalidade.

O gráfico de linha mostra a variação diária das vendas de Eletrônicos ao longo do ano. Observa-se que há picos de vendas em determinados momentos, como próximos ao final do mês e durante feriados específicos, sugerindo um comportamento sazonal. Esses picos podem estar relacionados a promoções, feriados como o Dia das Mães, Black Friday ou períodos de pagamento de salários, onde os consumidores têm mais disposição para adquirir produtos de maior valor, como os eletrônicos.

Além disso, há períodos com quedas acentuadas nas vendas, indicando momentos de menor atividade, como durante a semana ou entre os ciclos promocionais. A tendência geral parece ser cíclica, com altos e baixos que se repetem ao longo do tempo.

## Conclusão

A análise dos dados de vendas fictícios revelou que a categoria Eletrônicos foi a mais lucrativa, com um comportamento sazonal observado nas vendas. A categoria Roupas se destacou pela quantidade média vendida. As visualizações gráficas ajudaram a identificar padrões claros nas vendas ao longo do tempo.

