from abc import abstractmethod
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @abstractmethod
    def generate(productList):
        simple_report = SimpleReport.generate(productList)
        result = simple_report + "\nProdutos estocados por empresa:\n"
        repetition = {}
        for row in productList:
            if row["nome_da_empresa"] not in repetition:
                repetition[row["nome_da_empresa"]] = 0
            repetition[row["nome_da_empresa"]] += 1
        for item in repetition.items():
            result = result + f"- {item[0]}: {item[1]}\n"
        return result
