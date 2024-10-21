# Extrator de Dados de Texto em Python

Este é um simples extrator de e-mails e URLs que permite a extração a partir de um texto fornecido pelo usuário. Este projeto foi desenvolvido durante meus estudos de Python e regex.

## Pré-requisitos

- Python 3 ou superior

## Instrução de Uso

### 1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   ```
   
### 2. Navegue até o diretório do projeto:
   ```bash
   cd seurepositorio
   ```
   
### 3. Execute o script:
```bash
python extrator.py
```
O script solicitará que você insira o texto a ser analisado e, em seguida, irá exibir e salvar os e-mails e URLs encontrados no arquivo `resultados.txt`.

## Exemplo de uso
Insira o texto a ser analisado: 
```
Exemplo de texto com e-mail teste@email.com e site https://exemplo.com
```

Saída no terminal:
```
E-mails encontrados: ['teste@email.com']
URLs encontradas: ['https://exemplo.com']
```

