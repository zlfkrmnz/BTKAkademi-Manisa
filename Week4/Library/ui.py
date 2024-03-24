class UI:
    def __init__(self, menu_items: list):
        self.menu_items = menu_items

    @staticmethod
    def line(text=""):
        if text == "":
            return "-" * 50
        else:
            return "|" + text.center(48, " ") + "|"

    def create_menu(self):
        text = self.line()
        text += f"\n{self.line('Menü')}\n"
        text += self.line()
        no = 0
        for element in self.menu_items:
            no += 1
            element = f"{no}..{element}"
            text += f"\n{self.line(element)}"
        text += "\n" + self.line()
        print(text)
        option = input(f"Lütfen tercihinizi giriniz. [1-{len(self.menu_items)}]: ")
        return option


