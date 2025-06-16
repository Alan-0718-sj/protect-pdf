# Protect PDF File

Este repositório contém um script em Python que permite criptografar arquivos PDF existentes, protegendo-os com senha.

---

## Índice

1. [Descrição](#descrição)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Como funciona](#como-funciona)
6. [Estrutura de Arquivos](#estrutura-de-arquivos)
7. [Exemplos](#exemplos)
8. [Contribuição](#contribuição)
9. [Licença](#licença)

---

## Descrição

O script `protect_pdf.py` utiliza a biblioteca [PyPDF2](https://pypi.org/project/PyPDF2/) para ler um arquivo PDF existente, iterar sobre suas páginas e gerar uma nova cópia criptografada com senha. Ao executar o programa, o usuário será solicitado a inserir a senha desejada, e o PDF de saída será salvo como `new-file-protected.pdf`.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca PyPDF2

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/protect-pdf.git
   cd protect-pdf
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install PyPDF2
   ```

## Uso

1. Coloque o arquivo PDF que deseja proteger no mesmo diretório do script e renomeie-o para `github-git-cheat-sheet.pdf`, ou ajuste o nome no código.

2. Execute o script:

   ```bash
   python protect_pdf.py
   ```

3. Insira a senha quando solicitado.

4. O arquivo protegido será gerado como `new-file-protected.pdf`.

## Como funciona

O script segue as etapas abaixo:

1. Limpa a tela (compatível com Windows e Unix).
2. Exibe um título centralizado.
3. Lê o PDF original usando `PdfReader`.
4. Adiciona todas as páginas ao objeto `PdfWriter`.
5. Solicita ao usuário que digite a senha (utilizando `getpass` para ocultar a entrada).
6. Criptografa o PDF com a senha informada.
7. Gera o novo arquivo `new-file-protected.pdf`.
8. Informa sucesso ao usuário.

## Estrutura de Arquivos

```
protect-pdf/
├── protect_pdf.py   # Script principal
├── github-git-cheat-sheet.pdf   # PDF de exemplo (substitua pelo seu arquivo)
└── new-file-protected.pdf       # PDF gerado após execução
```

## Exemplos

```bash
$ python protect_pdf.py
######################################################################
#                           PROTECT PDF FILE                          #
######################################################################

Digite a senha: ********

PDF protegido com sucesso!
```
## Vídeo

- YouTube: [Alan Silva](https://youtu.be/R2n0G7xqJFg)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

