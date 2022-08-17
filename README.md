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

# 2. Premissas de Negócios.

O time de vendas já utiliza o Google Sheets como ferramenta corporativa. É preciso que o ranking de propensão de compra seja incorporado nele.

# 3. Planejamento da solução
## Qual a Solução?
Desenvolver uma solução que classifique os clientes com maior propensão de adquirir seguro de automóvel.

## Como Será a solução?
Será disponibilizado uma API que o cliente pode acessar através de aplicativo, site ou outra ferramenta.

## Hospedagem
Hospedagem será feita na plataforma Heroku, disponibilizado no link: https://health-insurance-ranking-cs.herokuapp.com/
- Para consultar o status basta fazer requisição /status
- Para fazer a classificação a requisição do tipo POST na rota /predict

## Método de entrega
Conforme levantado a maneira mais rápida é através de uma funcionalidade dentro da ferramenta Google Sheets, que para quaisquer novos clientes inclusos na planilha, vai informar na coluna Score a por propensão de compra.
Esta solução pode gerar o score para novo cliente ou os 76 mil clientes da base.

Disponibilizado no link: https://docs.google.com/spreadsheets/d/1RDqk3xsWjkq25O6RqTeURAtFN7fsZNiU9me7N_db_Fg/edit#gid=0

# 3. Estratégia de Solução

A minha estratégia para resolver este desafio foi:

**Etapa 01. Descrição dos dados:**
- Coletar dados em um banco de dados AWS.
- Nesta etapa meu objetivo é entender as dimensões dos dados, atributos, analisar distribuição dos dados de uma forma sucinta para se necessário questionar time de negócio.
- Fazer análise descritiva.

Os dados disponíveis tem 381109 linhas e 12 colunas com as seguintes informações:

| **Feature** | **Descrição** |
| -- | -- |
| Id | identificador único do cliente. |
| Gender | gênero do cliente. |
| Age | idade do cliente. |
| Driving License | 0, o cliente não tem permissão para dirigir e 1, o cliente tem para dirigir ( CNH – Carteira Nacional de Habilitação ) |
| Region Code | código da região do cliente. |
| Previously Insured | 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel. |
| Vehicle Age | idade do veículo. |
| Vehicle Damage | 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado. |
| Anual Premium | quantidade que o cliente pagou à empresa pelo seguro de saúde anual. |
| Policy sales channel | código anônimo para o canal de contato com o cliente. |
| Vintage | número de dias que o cliente se associou à empresa através da compra do seguro de saúde. |
| Response | 0, o cliente não tem interesse e 1, o cliente tem interesse. |

![](/img/descricao_dados.jpg)

**Etapa 02. Feature Engineering:**
- Criação mindmap de hipóteses.
- Derivar a partir dos dados originais novos atributos que consigam modelar melhor o fonômeno.

**Etapa 03. Filtragem de dados:**
- Filtrar atributos e linhas que não tenham informações relevantes para modelar o fonômeno.

**Etapa 04. Análise Exploratória de Dados:**
- Fazer análise univariada no sweetviz, avaliando detalhes de cada atributo
- Análise bivariada para encontrar insights e validar hipóteses.
- Entender o impacto das variávais na aprendizagem do modelo.

**Etapa 05. Preparação de Dados:**
- Padronizar atributos numéricos com distribuição normal.
- Reescalar atributos numéricos com distribuição não normal.
- Codificar atributos categóricos em atributos numéricos.
- Aplicas as transformações acima aos dados de teste.
- Para scaling:
    - RobustScaler (Quando havia muitos outliers)
    - MinMaxScaler
- Encoding:
    - Label Encoding
    - TargetEncoder
    - OneHotEncoder

**Etapa 06. Feature Selection:**
- Separar dados de treino e validação.
- Executar algoritmos que mostra relevância das features. (boruta, RFE)
- Unir features do algoritmo com as que foram identificadas na EDA.
- Selecionar apenas os melhores atributos para treinar os modelos de machine learning.

**Etapa 07. Modelagem de machine learning:**
- Executado algoritmos: KNN classifier, Logistic regression, ExtraTrees classifier, Randon Forest e XGBboost classifier.
- Plotar gráficos curva de ganho cumulativo.
- Plotar gráficos curva lift.
- Criar tabela de performance comparando precison@k/recall@k de cada modelo.

**Etapa 08. Ajuste fino de hiperparâmetros:**
- Fazer um ajuste fino de hiperparâmetros em cada modelo, identificando o melhor conjunto de parâmetros para maximizar suas capacidades de aprendizagem.
- Aplicar validação cruzada em cada modelo, reduzindo o viés de seleção (teoria da amostragem), por utilizar várias amostras diferentes dos dados.
- Plotar curvas de ganho cumulativo, lift e precison@k/recall@k comparando os 4 modelos.

**Etapa 09. Converter o desempenho do modelo em valores de negócios:**
- Comparar resultados da lista aleatória com a lista ordenada por propensão de compra.
- Traduzir as métricas do algoritmo para ganho no negócio.

**Etapa 10. Implantar o Modelo em Produção:**
- Criar classes para publicação em produção.
- Testar as classes localmente.
- Publicar modelo no Heroku Cloud.
- Criar App Script em Google Sheets para consultar o modelo em produção.
- Implementar botão que consulta a propensão de compra dos clientes no Google Sheets, e testar a solução.

# 4. Os principais insights de dados

... Em Desenvolvimento

<!-- **Hipótese 01:**

**Verdadeiro/falso.**

**Hipótese 02:**

**Verdadeiro/falso.**

**Hipótese 03:**

**Verdadeiro/falso.** -->

# 5. Modelo de aprendizado de máquina aplicado

# 6. Desempenho do Modelo de Aprendizado de Máquina

# 7. Resultados de Negócios

# 8. Conclusões

# 9. Lições aprendidas

# 10. Próximos passos para melhorar (proximos ciclos do CRISPI)
- Derivar novas features.
- Aplicar mais métodos de seleção de features (RFECV).
- Fazer hyperparameter fine tunning usando o optuna ou GridSearchCV.

<!-- ## Referências
**Métricas de Ranqueamento**
- https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples
- https://stats.stackexchange.com/questions/159657/metrics-for-evaluating-ranking-algorithms
- https://archive.siam.org/meetings/sdm10/tutorial1.pdf
- https://brianmcfee.net/papers/mlr.pdf
- https://towardsdatascience.com/meaningful-metrics-cumulative-gains-and-lyft-charts-7aac02fc5c14
- https://towardsdatascience.com/20-popular-machine-learning-metrics-part-2-ranking-statistical-metrics-22c3e5a937b6

**Outras**
- https://stats.stackexchange.com/questions/262794/why-does-a-decision-tree-have-low-bias-high-variance

**Debug**
- https://towardsdatascience.com/how-to-debug-flask-applications-in-vs-code-c65c9bdbef21
- https://medium.com/trainingcenter/flask-restplus-ea942ec30555 -->

