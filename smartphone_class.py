# smartphone_class.py

class Smartphone:
    def __init__(self, brand, model, storage):
        # Attributes
        self.brand = brand
        self.model = model
        self.__storage = storage  # 🔒 Encapsulated attribute (private)

    def call(self, contact):
        print(f"📞 Calling {contact} from {self.model}...")

    def install_app(self, app_name):
        print(f"📲 Installing {app_name} on {self.model}...")

    def show_info(self):
        print(f"📱 {self.brand} {self.model} with {self.__storage}GB storage")

    def get_storage(self):  # 🔓 Controlled access to private attribute
        return self.__storage


# Child class demonstrating inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # Inherit parent init
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"🎮 Playing {game_name} on {self.model} with GPU {self.gpu}!")


# 🧪 Testing
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S23", 256)
    phone1.show_info()
    phone1.call("Alice")
    phone1.install_app("Instagram")

    print("Storage:", phone1.get_storage())  # Access private data safely

    print("\n--- Gaming Phone ---")
    gamer = GamingPhone("Asus", "ROG 7", 512, "Adreno 740")
    gamer.show_info()
    gamer.play_game("Call of Duty")
