class UI:
    def __init__(self, menu_items):
        self.menu_items = menu_items

    @staticmethod
    def line(text=""):
        if text == "":
            return "-" * 55
        else:
            return "|" + text.center(53, " ") + "|"

    def create_menu(self):
        text = self.line()
        text += f"\n{self.line('Menu')}\n"
        text += self.line()
        for element in self.menu_items:
            text += f"\n{self.line(element)}"
        text += "\n" + self.line()
        print(text)
        option = input(f"Please enter your choice [1-{len(self.menu_items)}]: ")
        return option


