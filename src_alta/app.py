def calcular_rentabilidade(custo, venda):
    if custo <= 0:
        raise ValueError("Custo deve ser maior que zero")

    return ((venda - custo) / custo) * 100

def calcular_preco_venda(custo, markup):
    if custo <= 0:
        raise ValueError("Custo deve ser maior que zero")

    if markup < 0:
        raise ValueError("Markup não pode ser negativo")

    return custo * (1 + markup / 100)