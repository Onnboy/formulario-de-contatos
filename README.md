# Formulário de Cadastro

Este é um simples formulário de cadastro desenvolvido com [Flet](https://flet.dev/), que permite ao usuário inserir informações como nome, e-mail e uma mensagem. O projeto valida os campos e exibe mensagens de confirmação ou erro com base nos dados fornecidos.

---

## 💻 Demonstração

O formulário contém:
- **Campo de Nome**: Entrada para o nome do usuário.
- **Campo de E-mail**: Entrada para o e-mail do usuário.
- **Campo de Mensagem**: Entrada para mensagens longas com suporte a várias linhas.
- **Botão Enviar**: Valida os campos e exibe mensagens de confirmação ou erro.

---

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flet**: Framework para criar interfaces gráficas multiplataforma.

---

## 🎯 Funcionalidades

1. **Formulário Simples**:
   - Insira nome, e-mail e mensagem.
2. **Validação de Campos**:
   - Exibe mensagem de erro caso algum campo esteja vazio.
3. **Confirmação de Envio**:
   - Exibe mensagem de sucesso ao enviar o formulário.
4. **Reset Automático**:
   - Limpa os campos após o envio bem-sucedido.

---

## 🛠️ Requisitos

- Python 3.10 ou superior.
- Biblioteca `flet` instalada.

---

## ⚙️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/formulario-cadastro.git
   cd formulario-cadastro
4. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
5. Instale as dependências:
    ```bash
   pip install flet
6. Execute o projeto:
    ```bash
   python3 formulario.py

📖 Melhorias Futuras:
. Adicionar validação de formato de e-mail.
. Implementar envio real dos dados para um servidor ou API.
. Melhorar o design com estilos personalizados.



📂 Estrutura do Projeto até então:
formulario-cadastro/
│
├── main.py           # Código principal do formulário
├── requirements.txt  # Arquivos ignorados pelo Git
└── README.md         # Documentação do projeto
