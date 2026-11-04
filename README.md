# BaseLab — Conversor de bases numéricas

Aplicação acadêmica desenvolvida com Python e Flask para converter números inteiros entre as bases binária, decimal, octal e hexadecimal.

## Requisitos
- Python 3.13 ou compatível
- pip
- Navegador web

## Como executar no Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:5000.

## Estrutura

- `app.py`: rotas Flask e algoritmo de conversão
- `templates/`: páginas Início, Conversor e Equipe
- `static/style.css`: estilos responsivos
- `static/app.js`: comportamento do modal e cópia do resultado
- `requirements.txt`: dependências Python

## Sobre o algoritmo

A conversão é implementada manualmente. O programa interpreta cada dígito e acumula o valor decimal com `resultado = resultado * base + digito`. Em seguida, gera a representação de destino por divisões sucessivas e coleta dos restos. Não utiliza `int(texto, base)`, `bin()`, `oct()`, `hex()` nem bibliotecas de conversão de bases.

