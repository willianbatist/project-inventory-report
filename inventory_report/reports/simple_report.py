from datetime import datetime


# test = [
#      {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-04",
#        "data_de_validade": "2023-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#      {
#        "id": 2,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2028-04-04",
#        "data_de_validade": "2025-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#      {
#        "id": 3,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2013-04-04",
#        "data_de_validade": "2014-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ]


class SimpleReport:
    @staticmethod
    def generate(productList):
        date = "3000-12-31"
        date_old = datetime.strptime(date, "%Y-%m-%d").date()
        date_validity = datetime.strptime(date, "%Y-%m-%d").date()
        repetition = {}
        for row in productList:
            date_fab = datetime.strptime(
                row["data_de_fabricacao"], "%Y-%m-%d"
            ).date()
            date_val = datetime.strptime(
                row["data_de_validade"], "%Y-%m-%d"
            ).date()
            if date_old > date_fab:
                date_old = date_fab
            if date_validity > date_val:
                date_validity = date_val
            if row["nome_da_empresa"] not in repetition:
                repetition[row["nome_da_empresa"]] = 0
            repetition[row["nome_da_empresa"]] += 1
            disruption_list_companies = [
                (value, key) for value, key in repetition.items()
            ]
        company = max(disruption_list_companies)[0]
        return (
            f"Data de fabricação mais antiga: {date_old}\n"
            f"Data de validade mais próxima: {date_val}\n"
            f"Empresa com mais produtos: {company}"
        )


# print(SimpleReport.generate(test))
