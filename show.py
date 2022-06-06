import sys
import pygame as pg
from funnumbers import Numbers,Decimals,Hund,Thousands, DecimalThousands

pg.init()
pg.font.init()
pg.display.set_caption("Funy Numbers")
size = width, height = 1000,100
screen = pg.display.set_mode(size)
color = 255,255,255
font = pg.font.SysFont('Comic Sans MS', 25)


def main(user_input):
    print(len(user_input))
    try:
        if int(user_input) <= 19:
            NN = Numbers(int(user_input))
            print(NN.__str__())
            return NN.__str__()
    except ValueError as VE:
        print("Error")
    try:
        if int(user_input) >= 19 and len(str(user_input)) == 2 :
            DD = Decimals(user_input)
            print(DD.__str__())
            return DD.__str__()
    except ValueError as VE:
        print("Error")
    try:
        if int(user_input) >= 100 and len(str(user_input)) <= 3:
            HH = Hund(user_input)
            print(HH.__str__())
            return HH.__str__()
    except ValueError as VE:
        print("Error")
    try:
        if int(user_input) >= 1000 and len(str(user_input)) == 4:
            TT = Thousands(user_input)
            print(TT.__str__())
            return TT.__str__()
    except ValueError as VE:
        print("Error")
    try:
        if len(str(user_input)) == 5:
            TS = DecimalThousands(user_input)
            print(TS.__str__())
            return TS.__str__()
    except ValueError as VE:
        print("Error")
symbols = []


def starting():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_0:
                    symbols.append(0)
                    print("pressed - 0")
                if event.key == pg.K_1:
                    symbols.append(1)
                    print("pressed - 1")
                if event.key == pg.K_2:
                    symbols.append(2)
                    print("pressed - 2")
                if event.key == pg.K_3:
                    symbols.append(3)
                    print("pressed - 3")
                if event.key == pg.K_4:
                    symbols.append(4)
                    print("pressed - 4")
                if event.key == pg.K_5:
                    symbols.append(5)
                    print("pressed - 5")
                if event.key == pg.K_6:
                    symbols.append(6)
                    print("pressed - 6")
                if event.key == pg.K_7:
                    symbols.append(7)
                    print("pressed - 7")
                if event.key == pg.K_8:
                    symbols.append(8)
                    print("pressed - 8")
                if event.key == pg.K_9:
                    symbols.append(9)
                    print("pressed - 9")
                if event.key == pg.K_DELETE:
                    print("deleted")
                    symbols.append("clear")
                if "clear" in symbols:
                    print("deleted")
                    symbols.clear()
                    screen.fill(color)
                    pg.display.update()
        symbols_ready = "".join(map(str, symbols))
        #print(symbols_ready)

        if len(symbols_ready) >= 1:
            textsurface = font.render(main(symbols_ready),False,(0,0,0))
            screen.fill(color)
            screen.blit(textsurface, (30, 0))
            user_input_render = font.render(symbols_ready, False, (0, 0, 0))
            screen.blit(user_input_render, (30, 50))
            pg.display.flip()
        if len(symbols_ready) == 0:
            symbols.clear()
            screen.fill(color)
            textsurface = font.render("Start Typing (to clean screen press 'DELETE')", False, (0, 0, 0))
            user_input_render = font.render(symbols_ready, False, (0, 0, 0))
            screen.blit(user_input_render, (30, 50))
            screen.blit(textsurface, (30, 0))
        pg.display.update()


if __name__ == '__main__':
    starting()