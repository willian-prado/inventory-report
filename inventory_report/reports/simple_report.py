from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(stock):
        creation_datetimes = [
            product["data_de_fabricacao"] for product in stock
        ]
        expiration_datetimes = [
            product["data_de_validade"] for product in stock
        ]

        sorted_list = sorted(
            expiration_datetimes,
            key=lambda t: datetime.strptime(t, "%Y-%m-%d"),
        )

        companies = [product["nome_da_empresa"] for product in stock]
        count_companies = Counter(companies)

        oldest_date = min(creation_datetimes)
        closest_date = [
            date for date in sorted_list
            if datetime.strptime(date, "%Y-%m-%d") > datetime.now()
        ][0]
        largest_inventory = count_companies.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com maior quantidade de produtos estocados: \
{largest_inventory}\n"
        )
