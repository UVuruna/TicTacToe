from Model import Model
from View import View
from Controller import Controller


if __name__=='__main__':
    game = Model()
    screen = View()
    controller = Controller()

    screen.mainloop()