# Conversor de Moedas

Uma aplicação web para conversão de moedas em tempo real, desenvolvida com Python Flask e uma interface web moderna.

## 🚀 Funcionalidades

- Conversão em tempo real entre diferentes moedas
- Interface web responsiva e amigável
- Botão de inversão rápida entre moedas
- Suporte para várias moedas principais (USD, EUR, BRL, GBP, JPY, CNY)
- Exibição da taxa de câmbio atual
- Tratamento de erros e feedback ao usuário

## 🛠 Tecnologias Utilizadas

- **Backend:**
  - Python 3
  - Flask (Framework web)
  - Requests (Para chamadas à API de câmbio)

- **Frontend:**
  - HTML5
  - CSS3 (com Bootstrap 5)
  - JavaScript (Vanilla)

- **API Externa:**
  - [ExchangeRate-API](https://open.er-api.com) para taxas de câmbio em tempo real

## 📋 Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luizhferraz/conversao-cambio.git
cd conversao-cambio
```

2. Crie um ambiente virtual e ative-o:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. Com o ambiente virtual ativado, execute:
```bash
python app.py
```

2. Abra seu navegador e acesse:
```
http://127.0.0.1:5000
```

## 💻 Como Usar

1. Selecione a moeda de origem no campo "De:"
2. Selecione a moeda de destino no campo "Para:"
3. Digite o valor que deseja converter
4. Clique em "Converter" ou use o botão de inversão (⇄) para trocar as moedas rapidamente

## 🏗 Estrutura do Projeto

```
conversao-cambio/
├── app.py                 # Aplicação Flask principal
├── currency_converter.py  # Lógica de conversão de moedas
├── requirements.txt      # Dependências do projeto
└── templates/
    └── index.html        # Interface web
```

## 📦 Componentes Principais

- **app.py**: Servidor Flask que gerencia as rotas e a comunicação entre frontend e backend
- **currency_converter.py**: Módulo responsável pela lógica de conversão e comunicação com a API externa
- **index.html**: Interface do usuário com layout responsivo e interações dinâmicas

## ⚙️ Funcionalidades Técnicas

- Requisições assíncronas para melhor experiência do usuário
- Tratamento de erros robusto (API indisponível, moeda inválida, etc.)
- Interface responsiva que funciona em diferentes dispositivos
- Validação de entrada para evitar valores negativos ou inválidos

## 🤝 Como Contribuir

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Luiz Ferraz
- GitHub: [@luizhferraz](https://github.com/luizhferraz)