from inventory_report.inventory.product import Product


def mock_products():
    return Product(
        id=1,
        nome_do_produto="Nicotine Polacrilex",
        nome_da_empresa="Target Corporation",
        data_de_fabricacao="2021-02-18",
        data_de_validade="2023-09-17",
        numero_de_serie="CR25 1551 4467 2549 4402 1",
        instrucoes_de_armazenamento="instrucao 1",
    )


def test_relatorio_produto():
    product = mock_products()
    assert (
        product.__repr__()
        == (
            f"O produto {product.nome_do_produto}"
            f" fabricado em {product.data_de_fabricacao}"
            f" por {product.nome_da_empresa} com validade"
            f" até {product.data_de_validade}"
            f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
        )
    )
