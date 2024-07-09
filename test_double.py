class TestDoubleInput:
    """test double for input"""
    def __init__(self, input):
        """stores input"""
        self.inputs = iter(input)

    def read(self):
        """Reads through lines"""
        try:
            return next(self.input)
        except StopIteration:
            return ''

    def close(self):
        """Ends it"""
        pass


class TestDoubleOutput:
    """Test double output"""
    def __init__(self):
        """stores output in a list"""
        self.list = []

    def add_text(self, text):
        """writes the tect"""
        self.list.append(text)

    def output(self):
        """Connects for output"""
        return ''.join(self.list)

    def close(self):
        """Ends it"""
        pass
