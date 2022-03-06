import 谷歌登录 as bing
class Person:
    name='a'
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def greet(self):
        print("hi! ervery one ! I'm {}".format(self.name))


def main():
    Alan=Person()
    Alan.set_name("Alan")
    Alan.greet()
    bing.main()

if __name__ == '__main__':
    main()