from datetime import datetime
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None


spy = Spy('Pandey', 'Mr.', 21, 4.9)

f1 = Spy('Deepti', 'Ms.', 16,4.7)
f2 = Spy('Kapish', 'Mr.', 21,4.8)
f3 = Spy('Aastha', 'Ms.', 26,4.5)

friends = [f1, f2, f3]

class chat_message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
