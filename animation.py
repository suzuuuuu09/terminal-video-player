from time import sleep

class Animation:
    def loading_animation(self, duration: float):
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        while duration > 0:
            for symbol in symbols:
                print(f"\r{symbol}", end="")
                sleep(0.1)
                duration -= 0.1
        print("\r", end="")