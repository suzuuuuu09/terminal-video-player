from msvcrt import getch

class ChoiceSelector:
    def __init__(self, options, start_row):
        self.options = options
        self.selected_index = 0
        self.start_row = start_row

    def display_menu(self):
        for i, option in enumerate(self.options):
            if i == self.selected_index:
                print(f"\033[{self.start_row};{i*10 + 5}H\033[32m> {option}\033[0m", end='', flush=True)
            else:
                print(f"\033[{self.start_row};{i*10 + 5}H  {option}", end='', flush=True)

    def run(self):
        self.display_menu()
        while True:
            key = ord(getch())
            if key == 75:  # Left arrow key
                if self.selected_index > 0:
                    self.selected_index -= 1
                    self.display_menu()
            elif key == 77:  # Right arrow key
                if self.selected_index < len(self.options) - 1:
                    self.selected_index += 1
                    self.display_menu()
            elif key == 13:  # Enter key
                break
        print("\n")
        return self.options[self.selected_index]