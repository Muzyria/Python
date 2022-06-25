class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass


print(PizzaMaker.__dict__.keys())

maker = PizzaMaker()
maker._make_barbecue()
#maker.__make_pepperoni()