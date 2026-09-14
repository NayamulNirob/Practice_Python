class Phone:
    def call(self):
        print('It can call')

    def massage(self):
        print("It can massage")


class Samsung(Phone):
    def takePhoto(self):
        print("It can take photo")

a10=Samsung()
a10.call()
a10.massage()
a10.takePhoto()
