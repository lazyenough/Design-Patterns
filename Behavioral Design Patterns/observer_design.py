# Observer Design Pattern is a behavioral pattern that creates a one-to-many relationship between a subject and its observers. When the subject's state changes, all dependent observers are notified and updated automatically, ensuring synchronized communication.

# Enables automatic updates to multiple objects when one object changes.
# Promotes loose coupling between the subject and its observers.
# Useful for implementing event-driven or publish-subscribe systems.

from abc import abstractmethod, ABC

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temparature = None
    
    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def set_temparature(self, temparature):
        self._temparature = temparature
        self.notify()
    
    def notify(self):
        for obs in self._observers:
            obs.update(self._temparature)


class Observer(ABC):
    @abstractmethod
    def update(self, temparature):
        pass

class PhoneDisplay(Observer):
    def update(self, temparature):
        print(f"Phone Display: Temparature is {temparature}.")

class TVDisplay(Observer):
    def update(self, temparature):
        print(f"TV Display: Temparature is {temparature}.")

class SmartSpeaker(Observer):
    def update(self, temparature):
        print(f"Smart Speaker: Temparature is {temparature}.")


if __name__ == "__main__":
    subject = WeatherStation()

    phone = PhoneDisplay()
    tv = TVDisplay()
    speaker = SmartSpeaker()

    subject.subscribe(phone)
    subject.subscribe(tv)
    subject.subscribe(speaker)

    subject.set_temparature(25)

    subject.unsubscribe(tv)

    subject.set_temparature(30)