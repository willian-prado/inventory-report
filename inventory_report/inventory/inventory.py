from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.read_file import ReadFile


class Inventory:
    def import_data(path, type):
        if path.endswith(".csv"):
            data = ReadFile.read_csv_file(path)

        elif path.endswith(".json"):
            data = ReadFile.read_json_file(path)

        elif path.endswith(".xml"):
            data = ReadFile.read_xml_file(path)

        return (
            SimpleReport.generate(data)
            if (type == "simples")
            else CompleteReport.generate(data)
        )
