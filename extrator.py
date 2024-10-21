import re

def extrair_dados(texto):
    padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    padrao_url = r'https?://[^\s]+'

    emails = re.findall(padrao_email, texto)
    urls = re.findall(padrao_url, texto)

    return emails, urls

def salvar_resultados(emails, urls):
    with open('resultados.txt', 'w') as f:
        f.write("E-mails encontrados:\n")
        for email in emails:
            f.write(f"{email}\n")
        f.write("\nURLs encontradas:\n")
        for url in urls:
            f.write(f"{url}\n")

if __name__ == "__main__":
    texto = input("Insira o texto a ser analisado: ")
    
    emails, urls = extrair_dados(texto)
    
    print("E-mails encontrados:", emails)
    print("URLs encontradas:", urls)

    salvar_resultados(emails, urls)
    print("Resultados salvos em 'resultados.txt'.")
