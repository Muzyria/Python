class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ("ul", "ol") else "ul"

    def __call__(self, *args, **kwargs):
        s = ''.join([f"<li>{i}</li>\n" for i in args[0]])
        return f"<{self.type_list}>\n{s}</{self.type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ul")
html = render(lst)
print(html)
