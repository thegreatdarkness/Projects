#  Create an application which manages an inventory of products.
#  Create a product class which has a price, id, and
#  quantity on hand. Then create an inventory class which keeps track
#  of various products and can sum up the inventory value.


class Product:
    def __init__(self, prod_id, price, quantity):
        self.prod_id = prod_id
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.prod_id}"

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
        else:
            print("Error. Enter value greater than zero.")

    def update_quantity(self, new_quantity, isIncrement):
        if isIncrement is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print("Error. Cannot reduce further.")

    def get_quantity(self):
        return self.quantity

    def view_product(self):
        print("Product ID: " +
              str(self.prod_id) +
              ", Price: " + str(self.price) +
              ", Quantity: " +
              str(self.quantity))


class Inventory:
    list_prod = None
    action = None

    def __init__(self, initial_inventory=[]):
        self.list_prod = initial_inventory

    def __repr__(self):
        return f"{self.list_prod}"

    def add_product(self):
        name = str(input("Input product name: "))
        price = float(input("Input price: "))
        quantity = int(input("Input quantity in stock: "))

        self_list_prod.append(
                                {
                                    "Name": name,
                                    "Price": price,
                                    "Quantity": quantity
                                }
                            )
        print(self.list_prod)

    def remove_prod(self):
        rmv_product_name = str(input("Name of product to remove: "))

        for product in self.list_prod:
            if product['Name'] == rmv_product_name:
                product_to_remove = product
                break
        else:
            print("Error. Product not in the inventory.")
            return

        self.list_prod.remove(product_to_remove)


    def view_inventory(self):
        for prod in self.list_prod:
            print(prod)


def interactive_manage(inv_instance):
    while True:
        action = input("Options: 1 - Add product,"
                       "2 - Delete product, "
                       "3 - View inventory, "
                       "4 - Exit: ")
        if action == '1':
            inv_instance.add_product()
        elif action == '2':
            inv_instance.remove_prod()
        elif action == '3':
            inv_instance.view_inventory()
        elif action == '4':
            break
        else:
            print('Option invalid')


def main():
    initial_inventory = [{
                            'Name': 'sandau',
                            'Price': 10,
                            'Quantity': 3
                        },
                        {
                            'Name': 'kozak',
                            'Price': 20,
                            'Quantity': 4
                        }]

    shoe_inventory = Inventory(initial_inventory)
    interactive_manage(shoe_inventory)


if __name__ == '__main__':
    main()
