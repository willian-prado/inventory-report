import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        if path.endswith(".csv"):
            with open(path) as file:
                products_reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                data = list(products_reader)
        elif path.endswith(".json"):
            with open(path) as file:
                data = json.load(file)

        return (
            SimpleReport.generate(data)
            if (type == "simples")
            else CompleteReport.generate(data)
        )
