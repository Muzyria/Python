

class HtmlTag:
    INDENT = 2
    depth = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.depth = type(self).depth
        self.inline = inline
        self.end_char = '' if inline else '\n'

