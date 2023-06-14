class HtmlTag:
    INDENT = 2
    depth = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.depth = type(self).depth
        self.inline = inline
        self.end_char = '' if inline else '\n'

    def __enter__(self):
        print(' ' * type(self).INDENT * self.depth + f'<{self.tag}>', end=self.end_char)
        type(self).depth += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline:
            print(f'</{self.tag}>')
        else:
            print(' ' * type(self).INDENT * self.depth + f'</{self.tag}>')
        type(self).depth -= 1

    def print(self, txt):
        if self.inline:
            print(txt, end=self.end_char)
        else:
            print(' ' * type(self).INDENT * (self.depth + 1) + txt, end=self.end_char)
