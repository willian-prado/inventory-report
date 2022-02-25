import csv
import json
import xml.etree.ElementTree as ET


class ReadFile:
    def read_csv_file(path):
        with open(path) as file:
            products_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            data = list(products_reader)

            return data

    def read_json_file(path):
        with open(path) as file:
            data = json.load(file)

            return data

    def read_xml_file(path):
        tree = ET.parse(path)
        root = tree.getroot()
        data = []

        for record in root.iter("record"):
            product = {}
            for entries in record:
                product[entries.tag] = entries.text
            data.append(product)

        return data
