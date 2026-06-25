'''
#protected method:
class Instagram:
    def __init__(self):
        self._post = []
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
subha = Instagram()
print(subha.accesspost)
subha.accesspost = 'class and object'
print(subha.accesspost)

#single inheritance:
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

dinesh = whatsappv1()
print("v1-Dinesh")
dinesh.message()
Naresh = whatsappv2()
print("v1-Naresh")
dinesh.message()
Naresh.calls()

#Multiple Inheritance:
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2:
    def calls(self):
        print("You can do video/audio calls")
class whatsappv3:
    def media(self):
        print("You can share your photos and videos")
class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status


#multilevel inheritance:
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")
class whatsappv3(whatsappv2):
    def media(self):
        print("You can share your photos and videos")
class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()

#hierarchy inheritace:
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can do video/audio calls")
class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can share your photos and videos")
dinesh = whatsappv3()
print("v3-Dinesh")
dinesh.message()
dinesh.stickers()
dinesh = whatsappv2()
print("v2-Dinesh")
dinesh.emojis()
dinesh.message()


#hybrid inheritance:
class whatsappv1:
    def message(self):
        print("You can send messages to people")
class whatsappv2(whatsappv1):
    def gif(self):
        print("You can send messages with gif to people ")
class whatsappv3(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people ")
class whatsappv4(whatsappv2,whatsappv3):
    def stickers(self):
        print("You can send messages with emojis to people")

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.gif()
dinesh.emojis()
dinesh.stickers()

class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2(wpv1):
    def status(self):
        super().status()
        print("you can react and reply")
class wpv3(wpv2):
    def status(self):
        super().status()
        print("you can like and reshare")
sahith = wpv3()
sahith.status()
'''            

class wpv1:
    def status(self):
        print("You can upload images/videos")
class wpv2:
    def status(self):
        print("you can react and reply")
class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("you can like and reshare")
sahith = wpv3()
sahith.status()
