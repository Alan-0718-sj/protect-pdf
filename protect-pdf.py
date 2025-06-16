from PyPDF2 import PdfWriter, PdfReader  # Classes atualizadas
import os
import getpass

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def title():
    print(" Protect PDF file ".upper().center(70, "#"))
    print()

def process():
    # Cria um objeto para escrever no PDF
    pdfwriter = PdfWriter()

    # Lê o arquivo PDF original
    pdf = PdfReader("github-git-cheat-sheet.pdf")

    # Itera por todas as páginas do PDF e adiciona ao novo PDF
    for page in pdf.pages:
        pdfwriter.add_page(page)

    # Solicita ao usuário que insira uma senha
    password = getpass.getpass(prompt="Digite a senha: ")

    # Criptografa o PDF com a senha fornecida
    pdfwriter.encrypt(password)

    # Salva o PDF criptografado em um novo arquivo
    with open("new-file-protected.pdf", "wb") as file:
        pdfwriter.write(file)

    print("\nPDF protegido com sucesso!")

def main():
    clear()
    title()
    process()

if __name__ == "__main__":
    main()

  