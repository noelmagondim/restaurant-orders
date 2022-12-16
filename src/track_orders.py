from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        client_orders = [
            order[1]
            for order in self.orders
            if order[0] == customer
        ]

        return Counter(client_orders).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        plates = set(
            order[1]
            for order in self.orders
        )

        client_orders = set(
            order[1]
            for order in self.orders
            if order[0] == customer
        )

        return plates - client_orders

    def get_days_never_visited_per_customer(self, customer):
        days = set(
            order[2]
            for order in self.orders
        )

        client_days = set(
            order[2]
            for order in self.orders
            if order[0] == customer
        )

        return days - client_days

    def get_busiest_day(self):
        days = set(
            day[2]
            for day in self.orders
        )

        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = [
            day[2]
            for day in self.orders
        ]

        return Counter(days).most_common()[-1][0]
