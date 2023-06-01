from abc import ABC, abstractmethod


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


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Processing debit payment type')
        print(f'Security code check: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order):
        print('Processing credit payment type')
        print(f'Security code check: {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print('Processing PayPal payment type')
        print(f'Security E-Mail: {self.email_address}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 2500)
order.add_item('SSD', 1, 7500)
order.add_item('USB', 2, 250)

print(order.total_price())
debit_processor = DebitPaymentProcessor('0372846')
debit_processor.pay(order)

credit_processor = CreditPaymentProcessor('0372846')
credit_processor.pay(order)

credit_processor = PaypalPaymentProcessor('some@mail.com')
credit_processor.pay(order)
