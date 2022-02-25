from inventory_report.importer.importer import Importer
from inventory_report.inventory.read_file import ReadFile


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        data = ReadFile.read_csv_file(path)
        return data
