import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        with open(path) as file:
            products_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            data = list(products_reader)

        return SimpleReport.generate(data) if (
            type == "simples"
        ) else CompleteReport.generate(data)
