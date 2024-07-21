
class handler():
    def __init__(self):
        self.red = "\033[1;31m"
        self.white = "\033[1;37m"
        self.normal = "\033[0;0m"
        self.blue = "\033[1;34m"

    def exception(self, exception):
        print(f"{self.red}[{self.white}Error{self.red}]{self.white} {str(exception)} {self.normal}")

    def info(self, message):
        print(f"{self.blue}[{self.white}INFO{self.blue}]{self.white} {str(message)} {self.normal}")