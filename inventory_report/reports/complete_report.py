from abc import abstractmethod
from datetime import datetime
from inventory_report.reports.simple_report import SimpleReport


def render_report(repetition, date_old, date_validity):
    disruption_list_companies = [
        (value, key) for value, key in repetition.items()
    ]
    company = max(disruption_list_companies)[0]
    result = (
        f"Data de fabricação mais antiga: {date_old}\n"
        f"Data de validade mais próxima: {date_validity}\n"
        f"Empresa com mais produtos: {company}\n"
        f"Produtos estocados por empresa:\n"
    )
    for item in repetition.items():
        result = result + f"- {item[0]}: {item[1]}\n"
    return result


class CompleteReport(SimpleReport):
    @abstractmethod
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
        response = render_report(repetition, date_old, date_validity)
        return response
