from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(productList):
        date = "9999-12-31"
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
        company = max(repetition, key=repetition.get)
        return (
            f"Data de fabricação mais antiga: {date_old}\n"
            f"Data de validade mais próxima: {date_validity}\n"
            f"Empresa com mais produtos: {company}"
        )
