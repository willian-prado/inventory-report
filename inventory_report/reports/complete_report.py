from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(stock):
        simple = SimpleReport.generate(stock)
        companies = [product["nome_da_empresa"] for product in stock]
        count_companies = Counter(companies)
        report_companies = [
            f"- {key}: {value}" for key, value in count_companies.items()
        ]
        complete_report = (
            simple
            + "\nProdutos estocados por empresa: \n"
            + "\n".join(report_companies)
            + "\n"
        )

        return complete_report
