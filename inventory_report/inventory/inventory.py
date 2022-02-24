import csv
import json
import xml.etree.ElementTree as ET
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

        elif path.endswith(".xml"):
            tree = ET.parse(path)
            root = tree.getroot()
            data = []

            for record in root.iter('record'):
                product = {}
                for entries in record:
                    product[entries.tag] = entries.text
                data.append(product)

        return (
            SimpleReport.generate(data)
            if (type == "simples")
            else CompleteReport.generate(data)
        )


path = "inventory_report/data/inventory.xml"
my_report = Inventory.import_data(path, "simples")
