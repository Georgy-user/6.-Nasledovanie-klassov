class Horse:
    x_distance = 0
    def __init__(self):
        self.sound = 'Frrr'
        # Далее: super(): обращение к self другого класса (класса Eagle)
        # при создании нового объекта класса Pegasus.
        super().__init__()
    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    def __init__(self):
        self.sound = 'I train, eat, sleep and repeat'
        self.tutu = 5
    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)
    def voice(self): # Подача голоса.
        print(self.sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


