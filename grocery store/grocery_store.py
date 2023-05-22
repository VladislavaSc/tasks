class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.__count = count

    def sale(self, sale_count):
        self.__count -= sale_count

    def fill(self, fill_count):
        self.__count += fill_count


    @property
    def count(self):
        return self.__count


if __name__ == '__main__':
    product = Product('Chair', 1500, 10)


# TestCase#1 Initialization
    assert product.name == 'Chair'
    assert product.price == 1500
    assert product.count == 10

# TestCase#2 Sale
    product.sale(1)
    assert product.count == 9

#TestCase#3 Replenish the warehouse
    product.fill(1)
    assert product.count == 10