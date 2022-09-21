import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def render_files(path, type: str):
    reader = str(path).split(".")[-1]
    if reader == "csv":
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            *data, = reader
    if reader == "json":
        with open(path) as file:
            data = json.load(file)
    if reader == "xml":
        with open(path) as file:
            data = xmltodict.parse(file.read())["dataset"]["record"]
    return data


class Inventory:
    @staticmethod
    def import_data(path, type: str):
        dado = render_files(path, type)
        if type == "simples":
            return SimpleReport.generate(dado)
        if type == "completo":
            return CompleteReport.generate(dado)
