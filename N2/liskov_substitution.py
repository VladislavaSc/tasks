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
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, order, payment_type, security_code):
        print('Processing debit payment type')
        print(f'Security code check: {security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, payment_type, security_code):
        print('Processing credit payment type')
        print(f'Security code check: {security_code}')
        order.status = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):

    def pay(self, order, payment_type, security_code):
        print('Processing PayPal payment type')
        print(f'Security E-Mail: {security_code}')
        order.status = 'paid'


order = Order()
order.add_item('Keyboard', 1, 2500)
order.add_item('SSD', 1, 7500)
order.add_item('USB', 2, 250)

print(order.total_price())
debit_processor = DebitPaymentProcessor
debit_processor.pay_debit(order, '0372846')

credit_processor = CreditPaymentProcessor
credit_processor.pay_debit(order, '0372846')

credit_processor = PaypalPaymentProcessor
credit_processor.pay_debit(order, 'some@mail.com')