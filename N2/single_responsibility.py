class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantities * prices for quantities, prices in zip(self.quantities,))

    def pay(self, payment_type, security_code):
        if payment_type == 'debit':
            print('Processing debit payment type')
            print(f'Security code check: {security_code}')
            self.status = 'paid'
        elif payment_type == 'credit':
            print('Processing credit payment type')
            print(f'Security code check: {security_code}')
            self.status = 'paid'


class PaymentProcessor:

    def pay_debit(self, order, payment_type, security_code):
        print('Processing debit payment type')
        print(f'Security code check: {security_code}')
        order.status = 'paid'

    def pay_credit(self, order, payment_type, security_code):
        print('Processing credit payment type')
        print(f'Security code check: {security_code}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 2500)
order.add_item('SSD', 1, 7500)
order.add_item('USB', 2, 250)

print(order.total_price())
processor = PaymentProcessor
processor.pay_debit(order, '0372846')
processor.pay_credit(order, '7383903')
