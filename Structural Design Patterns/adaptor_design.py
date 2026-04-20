# It allows incompatible interfaces to work together. It acts as a bridge between two unrelated components by translating one interface into another that the client expects.

class EuropeanSocket:
    def plug_in(self):
        return "220V power"

class USPlugAdapter:
    def __init__(self, european_socket: EuropeanSocket):
        self.socket = european_socket
    
    def connect(self):
        return f"Adapter converts -> {self.socket.plug_in()} from european socket to 110V."

if __name__ == "__main__":
    european_socket = EuropeanSocket()

    adapter = USPlugAdapter(european_socket)

    print(adapter.connect())