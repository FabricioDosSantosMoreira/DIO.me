from interface.interface import Interface


class Main():

    def __init__(self) -> None:
        self.is_running: bool = True

        self.on_init()

    
    def on_init(self) -> None:
        self.interface = Interface(self)
        
    
    def run(self) -> None:
        while self.is_running:

            self.interface.run()


    def quit(self) -> None:
        self.is_running = False
        quit("\nAVISO - - -> Saindo do sistema...")


if __name__ == "__main__":
    app = Main()
    app.run()
