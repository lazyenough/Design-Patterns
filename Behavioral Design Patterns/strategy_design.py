# The Strategy Design Pattern is a behavioral pattern that defines a group of related algorithms, encapsulates each one in a separate class, and makes them interchangeable. It allows the algorithm to vary independently from the client that uses it, enabling behavior changes at runtime without altering existing code.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float | int):
        pass
    

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} from Credit Card."

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} from Pay Pal."

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} from Bitcoin."
    

class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def pay(self, amount):
        return self.strategy.pay(amount)
    

if __name__ == "__main__":
    payment_service = PaymentService(CreditCardPayment())
    print(payment_service.pay(1000))
    
    payment_service.set_strategy(PayPalPayment())
    print(payment_service.pay(2000))
    
    payment_service.set_strategy(BitcoinPayment())
    print(payment_service.pay(3000))