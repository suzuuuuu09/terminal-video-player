from time import sleep
from random import uniform

class Animation:
    # ロードのアニメーション
    def loading_animation_dot(self, duration: float):
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        while duration > 0:
            for symbol in symbols:
                print(f"\r{symbol}", end="")
                sleep(0.1)
                duration -= 0.1
        print("\r", end="")

    def loading_animation_spinner(self, duration: float):
        symbols = ['|', '/', '-', '\\']
        while duration > 0:
            for symbol in symbols:
                print(f"\r{symbol}", end="")
                sleep(0.1)
                duration -= 0.1
        print("\r", end="")

    def loading_animation_bar(self, duration: float, length: int):
        speed = duration / length
        for i in range(length + 1):
            sleep_time = uniform(speed - (speed / 1.1), speed + (speed / 1.1))
            percent = round(i / length * 100, 3)
            print(f"\r{percent:.1f}% [{'█' * i}{' ' * (length - i)}]", end="", flush=True)
            sleep(sleep_time)
            duration -= sleep_time
        print("\r", end="")

animation = Animation()
animation.loading_animation_bar(5.0, 50)