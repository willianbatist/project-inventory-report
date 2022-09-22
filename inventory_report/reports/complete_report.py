from abc import abstractmethod
from inventory_report.reports.simple_report import SimpleReport


def render_report(repetition, test):
    for item in repetition.items():
        result = test + f"- {item[0]}: {item[1]}\n"
    return result


class CompleteReport(SimpleReport):
    @abstractmethod
    def generate(productList):
        test = SimpleReport.generate(productList)
        result = test + "\nProdutos estocados por empresa:\n"
        repetition = {}
        for row in productList:
            if row["nome_da_empresa"] not in repetition:
                repetition[row["nome_da_empresa"]] = 0
            repetition[row["nome_da_empresa"]] += 1
        for item in repetition.items():
            result = result + f"- {item[0]}: {item[1]}\n"
        return result
