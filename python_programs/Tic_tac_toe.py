class TicTacToe:
    def __init__(self, cells):        
        self.lst = [list(cells[i:i+3]) for i in range(0,9,3)]
    
    def output(self):
        print('---------')
        for i in range(3):
            print("| ",end = "")
            for j in range(3):
                print(" " if self.lst[i][j] == '_' else self.lst[i][j], end = " ")
            print("|")
        print('---------')
    def start(self):
        self.output()
        while True:
            new_val = list(input("Enter the coordinates: ").split())
            if len(new_val) == 2 and (len(new_val[0]) == len(new_val[1]) == 1):
                if 47< ord(new_val[0]) <58 and 47< ord(new_val[1]) < 58:
                    if 48< ord(new_val[0]) < 52 and 48< ord(new_val[1]) < 52:
                        x, y = int(new_val[0]), int(new_val[1])
                        if self.lst[-y][x-1] == 'X' or self.lst[-y][x-1] == 'O':
                            print("This cell is occupied! Choose another one!")
                        else:
                            self.lst[-y][x-1] = 'X'
                            self.output()
                            break
                    else:
                        print("Coordinates should be from 1 to 3!")
                else:
                    print('You should enter numbers!')
            else:   
                print('You should enter numbers!')


game = TicTacToe(input('Enter cells: ')).start()