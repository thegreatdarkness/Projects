#  Create an application which manages an inventory of products. Create a product class which has a price, id, and
#  quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory
#  value.

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
        print("Product ID: " + str(self.prod_id) + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity))


class Inventory:

    list_prod = None

    def __init__(self):
        self.list_prod = {"Name": [], "Price": [], "Quantity": []}
        self.action = input("Options: 1 - Add product, 2 - Delete product, 3 - View inventory, 4 - Exit: ")

    def __repr__(self):
        return f"{self.list_prod}"

    def __eq__(self, other):
        return True if self.list_prod["Name"] == other.prod_id else False

    def add_product(self):
        name = str(input("Input product name: "))
        price = float(input("Input price: "))
        quantity = int(input("Input quantity in stock: "))
        self.list_prod["Name"].append(name)
        self.list_prod["Price"].append(price)
        self.list_prod["Quantity"].append(quantity)
        print(self.list_prod)

    def remove_prod(self):
        rmv_prod_id = str(input("Which product should be removed?: "))

        def get_position():
            return self.list_prod["Name"].index(rmv_prod_id)

        if rmv_prod_id in self.list_prod["Name"]:
            position = get_position()
            name = self.list_prod["Name"]
            price = self.list_prod["Price"]
            quantity = self.list_prod["Quantity"]
            self.list_prod["Name"].remove(name[position])
            self.list_prod["Price"].remove(price[position])
            self.list_prod["Quantity"].remove(quantity[position])

        else:
            print("Error. Product not in the inventory.")

    def view_inventory(self):
        print(self.list_prod)

    # if __name__ == '__main__':

    def __call__(self, *args, **kwargs):
        x = int(self.action)
        if True:
            if x == 1:
                self.add_product()
                self.__init__()
                self.__call__()
            if x == 2:
                self.remove_prod()
                self.__init__()
                self.__call__()
            if x == 3:
                self.view_inventory()
                self.__init__()
                self.__call__()
            while self.action == 4:
                break


invent1 = Inventory()
invent1()
