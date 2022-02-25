from inventory_report.importer.importer import Importer
from inventory_report.inventory.read_file import ReadFile


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        data = ReadFile.read_json_file(path)
        return data
