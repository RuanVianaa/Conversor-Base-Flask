from flask import Flask, render_template, request

app = Flask(__name__)

BASES = {
    "decimal": {"label": "Decimal", "base": 10, "prefix": "DEC"},
    "binario": {"label": "Binário", "base": 2, "prefix": "BIN"},
    "octal": {"label": "Octal", "base": 8, "prefix": "OCT"},
    "hexadecimal": {"label": "Hexadecimal", "base": 16, "prefix": "HEX"},
}


class ConversionError(ValueError):
    """Erro para entradas inválidas ou bases não suportadas."""


def caractere_para_valor(caractere):
    """Converte um único dígito em seu valor, sem funções prontas de conversão de base."""
    if "0" <= caractere <= "9":
        return ord(caractere) - ord("0")

    caractere = caractere.upper()
    if "A" <= caractere <= "F":
        return ord(caractere) - ord("A") + 10

    raise ConversionError(f"O caractere '{caractere}' não é um dígito válido.")


def valor_para_caractere(valor):
    """Converte um valor entre 0 e 15 no caractere que o representa."""
    if 0 <= valor <= 9:
        return chr(ord("0") + valor)
    if 10 <= valor <= 15:
        return chr(ord("A") + valor - 10)
    raise ConversionError("Valor interno inválido durante a conversão.")


def texto_para_decimal(texto, base_origem):
    """Lê o número dígito por dígito e calcula seu valor decimal."""
    texto = texto.strip().upper()
    if not texto:
        raise ConversionError("Digite um número para converter.")

    sinal = 1
    if texto[0] == "-":
        sinal = -1
        texto = texto[1:]
    elif texto[0] == "+":
        texto = texto[1:]

    if not texto:
        raise ConversionError("Digite os algarismos do número.")

    resultado = 0
    for caractere in texto:
        valor = caractere_para_valor(caractere)
        if valor >= base_origem:
            raise ConversionError(
                f"O dígito '{caractere}' não é válido para a base {base_origem}."
            )
        resultado = resultado * base_origem + valor

    return resultado * sinal


def decimal_para_texto(numero, base_destino):
    """Gera a representação em outra base usando divisões sucessivas."""
    if numero == 0:
        return "0"

    sinal = "-" if numero < 0 else ""
    numero = abs(numero)
    digitos = []

    while numero > 0:
        resto = numero % base_destino
        digitos.append(valor_para_caractere(resto))
        numero //= base_destino

    digitos.reverse()
    return sinal + "".join(digitos)


def converter(texto, origem, destino):
    if origem not in BASES or destino not in BASES:
        raise ConversionError("Selecione bases válidas.")

    valor_decimal = texto_para_decimal(texto, BASES[origem]["base"])
    return decimal_para_texto(valor_decimal, BASES[destino]["base"])


@app.route("/")
def inicio():
    return render_template("index.html", pagina="inicio")


@app.route("/equipe")
def equipe():
    # Substituam os exemplos pelos integrantes reais e suas contribuições.
    integrantes = [
        {"nome": "Nome do integrante 1", "contribuicao": "Implementação do algoritmo de conversão."},
        {"nome": "Nome do integrante 2", "contribuicao": "Desenvolvimento das páginas e do layout."},
        {"nome": "Nome do integrante 3", "contribuicao": "Testes, validação e documentação."},
    ]
    return render_template("equipe.html", pagina="equipe", integrantes=integrantes)


@app.route("/conversor", methods=["GET", "POST"])
def conversor():
    resultado = None
    erro = None
    valor = ""
    origem = "decimal"
    destino = "binario"
    origem_label = ""
    destino_label = ""

    if request.method == "POST":
        valor = request.form.get("valor", "")
        origem = request.form.get("origem", "decimal")
        destino = request.form.get("destino", "binario")

        if origem in BASES:
            origem_label = BASES[origem]["label"]
        if destino in BASES:
            destino_label = BASES[destino]["label"]

        try:
            resultado = converter(valor, origem, destino)
        except ConversionError as exc:
            erro = str(exc)

    return render_template(
        "conversor.html",
        pagina="conversor",
        bases=BASES,
        resultado=resultado,
        erro=erro,
        valor=valor,
        origem=origem,
        destino=destino,
        origem_label=origem_label,
        destino_label=destino_label,
    )


if __name__ == "__main__":
    app.run(debug=True)
