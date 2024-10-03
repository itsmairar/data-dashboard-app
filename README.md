# Data Dashboard App

Esta é uma aplicação que fornece dados de mercado para diferentes tickers financeiros utilizando a API do Yahoo Finance. A aplicação está estruturada utilizando o padrão de projeto **Facade** para simplificar a interface de uso dos serviços de mercado.

## Padrão de Projeto

### Facade

O padrão Facade foi utilizado para fornecer uma interface simplificada para o sistema de acesso aos dados de mercado. Isso permite que o front-end interaja com a aplicação sem precisar se preocupar com os detalhes da implementação dos serviços de mercado.

### Estrutura do Projeto

A estrutura do projeto é a seguinte:

├── main.py ├── models/ │ └── market_data_model.py ├── routers/ │ └── market_data_router.py └── services/ └── market_data_service.py

 - **main.py**: Ponto de entrada da aplicação, onde o FastAPI é iniciado e os roteadores são incluídos.
- **models/**: Contém as definições de modelos de dados.
 - **market_data_model.py**: Define o modelo para os dados de mercado.
- **routers/**: Contém as definições de rotas da API.
 - **market_data_router.py**: Define as rotas para acessar os dados de mercado.
- **services/**: Contém a lógica de negócio para acessar dados de mercado.
 - **market_data_service.py**: Implementa a lógica para buscar dados do Yahoo Finance.

## Pré-requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes pré-requisitos instalados:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/data-dashboard-app.git
   cd data-dashboard-app` 
   
2.**Instale as dependências:**

Utilize o `pip` para instalar as dependências necessárias. O arquivo `requirements.txt` deve conter as bibliotecas necessárias para a aplicação.


`pip install -r requirements.txt`

## Execução

Para executar a aplicação, utilize o seguinte comando:

`uvicorn main:app --reload` 

O servidor será iniciado e estará disponível em `http://127.0.0.1:8000`.

## Rotas da API


#### 1. Definição do Endpoint

-   **Rota**: `/market-data/`
-   **Método**: `GET`
-   **Parâmetros de Query**:
    -   `period`: Um string que indica o intervalo de tempo desejado. Exemplos de valores válidos incluem:
        -   `1d` (1 dia)
        -   `5d` (5 dias)
        -   `1mo` (1 mês)
        -   `3mo` (3 meses)

#### 2. Exemplo de Requisição

Aqui está um exemplo de como você pode fazer uma requisição para obter dados de mercado para os últimos 5 dias:

**Requisição HTTP**:


`GET http://127.0.0.1:8001/market-data/?period=5d` 

#### 3. Resposta

A resposta do servidor incluirá os dados do mercado para os tickers especificados (como `BTC-USD`, `ETH-USD`, etc.) para o período solicitado. A resposta deve ter a seguinte estrutura:

`{
  "BTC-USD": {
    "price": 60360.44,
    "change": -0.0087,
    "previous_price": 60365.69
  },
  "ETH-USD": {
    "price": 2331.24,
    "change": -0.0722,
    "previous_price": 2332.93
  },
  "PETR4.SA": {
    "price": 37.74,
    "change": 0.0,
    "previous_price": 37.74
  }
}`