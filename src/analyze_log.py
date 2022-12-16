import csv
from collections import Counter


def most_requested_product(orders, client):
    client_orders = [
        order[1]
        for order in orders
        if order[0] == client
    ]

    return Counter(client_orders).most_common(1)[0][0]


def client_count_ordered(orders, client, dish):
    client_dishes = [
        order[1]
        for order in orders
        if order[0] == client and order[1] == dish
    ]

    return len(client_dishes)


def never_ordered(orders, client):
    plates = set(
        order[1]
        for order in orders
    )

    client_plates = set(
        order[1]
        for order in orders
        if order[0] == client
    )

    return plates - client_plates


def never_visited_days(orders, client):
    days = set(
        order[2]
        for order in orders
    )

    client_days = set(
        order[2]
        for order in orders
        if order[0] == client
    )

    return days - client_days


def read_file_function(path_to_file):
    if (".csv") not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            return list(
                csv.reader(file)
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def analyze_log(path_to_file):
    orders = read_file_function(path_to_file)
    maria_most_ordered = most_requested_product(orders, "maria")
    arnaldo_ordered = client_count_ordered(orders, "arnaldo", "hamburguer")
    joao_never_ordered = never_ordered(orders, "joao")
    joao_never_visited = never_visited_days(orders, "joao")
    with open("data/mkt_campaign.txt", mode="w", encoding="utf-8") as file:
        file.write(
            f"{maria_most_ordered}\n"
            f"{arnaldo_ordered}\n"
            f"{joao_never_ordered}\n"
            f"{joao_never_visited}\n"
        )
