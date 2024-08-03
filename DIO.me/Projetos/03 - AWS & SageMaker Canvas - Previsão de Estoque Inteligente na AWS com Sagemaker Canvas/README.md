# 📊 Previsão do Tempo Estimado Usando [Amazon SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

No desafio de projeto "Previsão do Tempo Estimado Usando Amazon SageMaker Canvas" a ideia é treinar um modelo baseado em Machine Learning para criar previsões sobre o tempo estimado de uma remessa em dias.


## 🎯 Objetivos do Desafio de Projeto

![image](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque/assets/730492/72f5c21f-5562-491e-aa42-2885a3184650)

- Selecionar o Dataset que será usado no modelo
- Modelar/Preparar os dados antes de treinar o modelo
- Treinar o modelo de Machine Learning
- Analisar o modelo treinado


## 🚀 Passo a Passo

### 1. Selecionar o Dataset

Primeiramente, selecionei o dataset 'canvas-sample-shipping-logs.csv' disponível por padrão no SageMaker Canvas. Este dataset contém informações completas relacionadas ao envio de produtos, incluindo tempo estimado, prioridade de envio, origem, entre outros. O dataset possui aprox. 10000 linhas e 12 colunas e está organizado da seguinte maneira:

| Nome da Coluna           | Descrição da Coluna                                                                            |
|--------------------------|------------------------------------------------------------------------------------------------|
| ExpectedShippingDays     | Dias esperados para a remessa -                                                                |
| ActualShippingDays       | Número de dias que levou para entregar a remessa                                               |
| Carrier                  | Transportadora utilizada para a remessa                                                        |
| YShippingDistance        | Distância da remessa no eixo Y                                                                 |
| XShippingDistance        | Distância da remessa no eixo X                                                                 |
| InBulkOrder              | É um pedido em massa                                                                           |
| ShippingOrigin           | Origem da remessa                                                                              |
| OrderDate                | Data em que o pedido foi feito                                                                 |
| OrderID                  | ID do pedido                                                                                   |
| ShippingPriority         | Prioridade da remessa                                                                          |
| OnTimeDelivery           | Indica se a remessa foi entregue no prazo                                                      |
| ProductId                | ID do produto                                                                                  |


### 2. Modelar/Preparar os dados

A modelagem e preparação dos dados é necessária para garantir a precisão do modelo que será treinado. Como o SageMaker Canvas fornece uma interface no-code, essa etapa é simplificada via 'Model Recipe', que é um histórico das alterações feitas sobre os dados antes do treinamento. Passos para transformar os dados:

- Remover colunas irrelevantes: As colunas 'OrderID' e 'ProductID' não serão necessárias para a previsão, logo foram removidas.
- Criar coluna de distância total: Calcular a distância total usando a fórmula 'Pow(Pow(XShippingDistance, 2) + Pow(YShippingDistance, 2), 1/2)' e criar uma coluna chamada 'Distance'.
- Remover colunas irrelevantes: Com a coluna 'Distance' criada, remova as colunas 'YShippingDistance' e 'XShippingDistance'
- Extrair infromações: A coluna 'OrderDate' deve ser converitida para datetime e extrair 'quarter', 'week of year' e 'month'


### 3. Construir/Treinar

Após modelar e preparar os dados é necessário treinar o modelo de Machine Learning, para isso construi com o 'Model type' sendo 'Numeric model type' e treinei usando a Standard Build. Deve demorar cerca de 1-2 horas até o modelo ser treinado.


### 4. Analisar

Status do modelo treinado: 

![Status do Modelo](./examples/util/01%20-%20Model%20Status.png)
