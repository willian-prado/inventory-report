from inventory_report.importer.importer import Importer
from inventory_report.inventory.read_file import ReadFile


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        data = ReadFile.read_xml_file(path)
        return data
