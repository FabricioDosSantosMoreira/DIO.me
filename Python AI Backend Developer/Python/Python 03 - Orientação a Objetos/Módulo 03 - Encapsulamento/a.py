
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


foo = Foo()
foo.hello()


bar = Bar()
bar.hello()