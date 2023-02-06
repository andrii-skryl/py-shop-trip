from math import sqrt
from app.customer import Customer
from app.shop import Shop


class Car:
    def __init__(self, brand: str, fuel_consumption: int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_trip_cost(
            self,
            fuel_price: float,
            customer: Customer,
            shop: Shop
    ) -> float:
        x_distance = (customer.location[0] - shop.location[0]) ** 2
        y_distance = (customer.location[1] - shop.location[1]) ** 2
        distance = sqrt(x_distance + y_distance)
        trip_cost = fuel_price * distance * self.fuel_consumption / 100 * 2
        return round(trip_cost, 2)

    def get_total_trip_cost(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> float:
        total_trip_cost = (
            shop.get_shopping_cost(customer)
            + self.get_trip_cost(fuel_price, customer, shop)
        )
        return total_trip_cost

    def get_shopping_options(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> None:
        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {self.get_total_trip_cost(customer, shop, fuel_price)}")

    def get_home(
            self,
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> None:
        total_cost = self.get_total_trip_cost(customer, shop, fuel_price)
        rest_on_balance = customer.money - total_cost
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {rest_on_balance} dollars\n")