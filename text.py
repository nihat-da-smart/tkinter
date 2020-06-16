from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_Input.set("")


cal = Tk()
cal.title('speller')
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=1,
                   bg="light yellow", justify='center').grid(columnspan=400)

btna = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="a", command=lambda: btnClick('a')).grid(row=1, column=0)

btnb = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="b", command=lambda: btnClick('b')).grid(row=1, column=1)

btnc = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="c", command=lambda: btnClick('c')).grid(row=1, column=2)

btnd = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="d", command=lambda: btnClick('d')).grid(row=1, column=3)

btne = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="e", command=lambda: btnClick('e')).grid(row=1, column=4)

btnf = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="f", command=lambda: btnClick('f')).grid(row=1, column=5)

btng = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="g", command=lambda: btnClick('g')).grid(row=1, column=6)

btnh = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="h", command=lambda: btnClick('h')).grid(row=1, column=7)

btni = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="i", bg="orange", command=lambda: btnClick('i')).grid(row=1, column=8)

btnj = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="j", bg="orange", command=lambda: btnClick('j')).grid(row=1, column=9)

btnk = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="k", bg="orange", command=lambda: btnClick('k')).grid(row=1, column=10)

btnl = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="l", bg="orange", command=lambda: btnClick('l')).grid(row=2, column=0)

btnm = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="m", command=lambda: btnClick('m')).grid(row=2, column=1)

btnn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="n", command=lambda: btnClick('n')).grid(row=2, column=2)

btno = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="o", command=lambda: btnClick('o')).grid(row=2, column=3)

btnp = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="p", command=lambda: btnClick('p')).grid(row=2, column=4)

btnq = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="q", command=lambda: btnClick('q')).grid(row=2, column=5)

btnr = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="r", command=lambda: btnClick('r')).grid(row=2, column=6)

btns = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="s", command=lambda: btnClick('s')).grid(row=2, column=7)

btnt = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="t", command=lambda: btnClick('t')).grid(row=2, column=8)

btnu = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="u", command=lambda: btnClick('u')).grid(row=2, column=9)

btnv = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="v", command=lambda: btnClick('v')).grid(row=2, column=10)

btnw = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="w", command=lambda: btnClick('w')).grid(row=3, column=0)

btnx = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="x", command=lambda: btnClick('x')).grid(row=3, column=1)

btny = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="y", command=lambda: btnClick('y')).grid(row=3, column=2)

btnz = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="z", command=lambda: btnClick('z')).grid(row=3, column=3)

btnclear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="clear", command=btnClear).grid(row=3, column=4)

btnspace = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="space", command=lambda: btnClick(' ')).grid(row=3, column=5)

btndot = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text=".", command=lambda: btnClick('.')).grid(row=3, column=6)

btncapsa = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="A", command=lambda: btnClick('A')).grid(row=3, column=7)

btncapsb = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="B", command=lambda: btnClick('B')).grid(row=3, column=8)

btncapsc = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="C", command=lambda: btnClick('C')).grid(row=3, column=9)

btncapsd = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="D", command=lambda: btnClick('D')).grid(row=3, column=10)

btncapse = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="E", command=lambda: btnClick('E')).grid(row=4, column=0)

btncapsf = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="F", command=lambda: btnClick('F')).grid(row=4, column=1)

btncapsg = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="G", command=lambda: btnClick('G')).grid(row=4, column=2)

btncapsh = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="H", command=lambda: btnClick('H')).grid(row=4, column=3)

btncapsi = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="I", command=lambda: btnClick('I')).grid(row=4, column=4)

btncapsj = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="J", command=lambda: btnClick('J')).grid(row=4, column=5)

btncapsk = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="K", command=lambda: btnClick('K')).grid(row=4, column=6)

btncapsl = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="L", command=lambda: btnClick('L')).grid(row=4, column=7)

btncapsm = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="M", command=lambda: btnClick('M')).grid(row=4, column=8)

btncapsn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="N", command=lambda: btnClick('N')).grid(row=4, column=9)

btncapso = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="O", command=lambda: btnClick('O')).grid(row=4, column=10)

btncapsp = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="P", command=lambda: btnClick('P')).grid(row=5, column=0)

btncapsq = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="Q", command=lambda: btnClick('Q')).grid(row=5, column=1)

btncapsr = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="R", command=lambda: btnClick('R')).grid(row=5, column=2)

btncapss = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="S", command=lambda: btnClick('S')).grid(row=5, column=3)

btncapst = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="T", command=lambda: btnClick('T')).grid(row=5, column=4)

btncapsu = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="U", command=lambda: btnClick('U')).grid(row=5, column=5)

btncapsv = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="V", command=lambda: btnClick('V')).grid(row=5, column=6)

btncapsw = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="W", command=lambda: btnClick('W')).grid(row=5, column=7)

btncapsx = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="X", command=lambda: btnClick('X')).grid(row=5, column=8)

btncapsy = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="Y", command=lambda: btnClick('Y')).grid(row=5, column=9)

btncapsz = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="Z", command=lambda: btnClick('Z')).grid(row=5, column=10)

btnf1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="Ω", command=lambda: btnClick('Ω')).grid(row=6, column=0)

btnf2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="≈", command=lambda: btnClick('≈')).grid(row=6, column=1)

btnf3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="ç", command=lambda: btnClick('ç')).grid(row=6, column=2)

btnf4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="√", command=lambda: btnClick('√')).grid(row=6, column=3)

btnf5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="∫", command=lambda: btnClick('∫')).grid(row=6, column=4)

btnf6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="˜", command=lambda: btnClick('˜')).grid(row=6, column=5)

btnf7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="µ", command=lambda: btnClick('µ')).grid(row=6, column=6)

btnf8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="≤", command=lambda: btnClick('≤')).grid(row=6, column=7)

btnf9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="¯", command=lambda: btnClick('¯')).grid(row=6, column=8)

btnf10 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="≥", command=lambda: btnClick('.')).grid(row=6, column=9)

btnf11 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="˘", command=lambda: btnClick('˘')).grid(row=6, column=10)

btnf12 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="÷", command=lambda: btnClick('÷')).grid(row=7, column=0)

btnf13 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¿", command=lambda: btnClick('¿')).grid(row=7, column=1)

btnf14 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="å", command=lambda: btnClick('å')).grid(row=7, column=2)

btnf15 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="ß", command=lambda: btnClick('ß')).grid(row=7, column=3)

btnf16 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="∂", command=lambda: btnClick('∂')).grid(row=7, column=4)

btnf17 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="ƒ", command=lambda: btnClick('ƒ')).grid(row=7, column=5)

btnf18 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="©", command=lambda: btnClick('©')).grid(row=7, column=6)

btnf19 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="˙", command=lambda: btnClick('˙')).grid(row=7, column=7)

btnf20 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="∆", command=lambda: btnClick('∆')).grid(row=7, column=8)

btnf21 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="˚", command=lambda: btnClick('˚')).grid(row=7, column=9)

btnf22 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¬", command=lambda: btnClick('¬')).grid(row=7, column=10)

btnf23 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="…", command=lambda: btnClick('…')).grid(row=8, column=0)

btnf24 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="Ú", command=lambda: btnClick('Ú')).grid(row=8, column=1)

btnf25 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="æ", command=lambda: btnClick('æ')).grid(row=8, column=2)

btnf26 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="Æ", command=lambda: btnClick('Æ')).grid(row=8, column=3)

btnf27 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="œ", command=lambda: btnClick('œ')).grid(row=8, column=4)

btnf28 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="∑", command=lambda: btnClick('∑')).grid(row=8, column=5)

btnf29 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="´", command=lambda: btnClick('´')).grid(row=8, column=6)

btnf30 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="®", command=lambda: btnClick('®')).grid(row=8, column=7)

btnf31 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="†", command=lambda: btnClick('†')).grid(row=8, column=8)

btnf32 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¥", command=lambda: btnClick('¥')).grid(row=8, column=9)

btnf33 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¨", command=lambda: btnClick('¨')).grid(row=8, column=10)

btnf34 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="ˆ", command=lambda: btnClick('ˆ')).grid(row=9, column=0)

btnf35 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="ø", command=lambda: btnClick('ø')).grid(row=9, column=1)

btnf36 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="π", command=lambda: btnClick('π')).grid(row=9, column=2)

btnf37 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="“", command=lambda: btnClick('“')).grid(row=9, column=3)

btnf38 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="”", command=lambda: btnClick('”')).grid(row=9, column=4)

btnf39 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="‘", command=lambda: btnClick('Ω')).grid(row=9, column=5)

btnf40 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="’", command=lambda: btnClick('Ω')).grid(row=9, column=6)

btnf41 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="«", command=lambda: btnClick('Ω')).grid(row=9, column=7)

btnf42 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="»", command=lambda: btnClick('Ω')).grid(row=9, column=8)

btnf43 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="≠", command=lambda: btnClick('≠')).grid(row=9, column=9)

btnf44 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="±", command=lambda: btnClick('±')).grid(row=9, column=10)

btnf45 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¡", command=lambda: btnClick('¡')).grid(row=10, column=0)

btnf46 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="™", command=lambda: btnClick('™')).grid(row=10, column=1)

btnf47 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="£", command=lambda: btnClick('£')).grid(row=10, column=2)

btnf48 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¢", command=lambda: btnClick('¢')).grid(row=10, column=3)

btnf49 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="∞", command=lambda: btnClick('∞')).grid(row=10, column=4)

btnf50 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="§", command=lambda: btnClick('§')).grid(row=10, column=5)

btnf51 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="¶", command=lambda: btnClick('¶')).grid(row=10, column=6)

btnf52 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="•", command=lambda: btnClick('•')).grid(row=10, column=7)

btnf53 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="ª", command=lambda: btnClick('ª')).grid(row=10, column=8)

btnf54 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="º", command=lambda: btnClick('º')).grid(row=10, column=9)

btnf55 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="°", command=lambda: btnClick('°')).grid(row=10, column=10)

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", command=lambda: btnClick('0')).grid(row=11, column=0)

btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", command=lambda: btnClick('1')).grid(row=11, column=1)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", command=lambda: btnClick('2')).grid(row=11, column=2)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", command=lambda: btnClick('3')).grid(row=11, column=3)

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", command=lambda: btnClick('4')).grid(row=11, column=4)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", command=lambda: btnClick('5')).grid(row=11, column=5)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", command=lambda: btnClick('6')).grid(row=11, column=6)

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", command=lambda: btnClick('7')).grid(row=11, column=7)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", command=lambda: btnClick('8')).grid(row=11, column=8)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", command=lambda: btnClick('9')).grid(row=11, column=9)

btn10 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
               text="10", command=lambda: btnClick('10')).grid(row=11, column=10)

cal.mainloop()