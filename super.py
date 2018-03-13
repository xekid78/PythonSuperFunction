class Greeting(object):
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def __init__(self):
        super(Hello, self).__init__()

    def wahaha(self):
        print("WA HA HA HA")

hello = Hello()
hello.say_hello()
hello.wahaha()
