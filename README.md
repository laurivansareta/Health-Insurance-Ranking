![](/img/car-insurance.jpg)

# Sistema de Recomendação para Cross-selling de Seguros

**Disclaimer: O Contexto a seguir, é completamente fictício, a empresa, o contexto, o CEO, as perguntas de negócio existem somente na minha imaginação.**

## ****Contexto de negócio****

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.


## ****Dados****

O conjunto de dados está disponível na plataforma do Kaggle, através desse link: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction 

Cada linha representa um cliente e cada coluna contém alguns atributos que descrevem esse cliente, além da sua resposta à pesquisa, na qual ela mencionou interesse ou não ao novo produto de seguros. 

O conjunto de dados inclui as seguintes informações:
- Id: identificador único do cliente.
- Gender: gênero do cliente.
- Age: idade do cliente.
- Driving License: 0, o cliente não tem permissão para dirigir e 1, o cliente tem para dirigir ( CNH – Carteira Nacional de Habilitação )
- Region Code: código da região do cliente.
- Previously Insured: 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel.
- Vehicle Age: idade do veículo.
- Vehicle Damage: 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado.
- Anual Premium: quantidade que o cliente pagou à empresa pelo seguro de saúde anual.
- Policy sales channel: código anônimo para o canal de contato com o cliente.
- Vintage: número de dias que o cliente se associou à empresa através da compra do seguro de saúde.
- Response: 0, o cliente não tem interesse e 1, o cliente tem interesse.

# 2. Premissas de Negócios.

O time de vendas já utiliza o Google Sheets como ferramenta corporativa. É preciso que o ranking de propensão de compra seja incorporado nele.

# 3. Planejamento da solução

O que será entregue efetivamente?

Uma funcionalidade dentro da ferramenta Google Sheets, que ordena os 76 mil clientes (ou quaisquer novos clientes inclusos na planilha) por propensão de compra.

# 3. Estratégia de Solução

... Em Desenvolvimento

A minha estratégia para resolver este desafio foi:

**Etapa 01. Descrição dos dados:**

**Etapa 02. Feature Engineering:**

**Etapa 03. Filtragem de dados:**

**Etapa 04. Análise Exploratória de Dados:**

**Etapa 05. Preparação de Dados:**

**Etapa 06. Feature Selection:**

**Etapa 07. Modelagem de machine learning:**

**Etapa 08. Ajuste fino de hiperparâmetros:**

**Etapa 09. Converter o desempenho do modelo em valores de negócios:**

**Etapa 10. Implantar o Modelo em Produção:**

# 4. Os 3 principais insights de dados

... Em Desenvolvimento

<!-- **Hipótese 01:**

**Verdadeiro/falso.**

**Hipótese 02:**

**Verdadeiro/falso.**

**Hipótese 03:**

**Verdadeiro/falso.**

# 5. Modelo de aprendizado de máquina aplicado

# 6. Desempenho do Modelo de Aprendizado de Máquina

# 7. Resultados de Negócios

# 8. Conclusões

# 9. Lições aprendidas

# 10. Próximos passos para melhorar -->


## Referências
**Métricas de Ranqueamento**
- https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples
- https://stats.stackexchange.com/questions/159657/metrics-for-evaluating-ranking-algorithms
- https://archive.siam.org/meetings/sdm10/tutorial1.pdf
- https://brianmcfee.net/papers/mlr.pdf
- https://towardsdatascience.com/meaningful-metrics-cumulative-gains-and-lyft-charts-7aac02fc5c14
- https://towardsdatascience.com/20-popular-machine-learning-metrics-part-2-ranking-statistical-metrics-22c3e5a937b6

**Outras**
- https://stats.stackexchange.com/questions/262794/why-does-a-decision-tree-have-low-bias-high-variance

