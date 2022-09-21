import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def render_files(path, str):
    reader = str(path).split(".")[-1]
    if reader == "csv":
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            *data, = reader
    return data


class Inventory:
    @staticmethod
    def import_data(path, str):
        dado = render_files(path, str)
        if type == "simples":
            return SimpleReport.generate(dado)
        if type == "completo":
            return CompleteReport.generate(dado)
