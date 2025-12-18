import tkinter

root = tkinter.Tk()

root.geometry("650x650")
root.title("2048")

label = tkinter.Label(root, text = '2048', font = ('Clear Sans', 20), pady=20)
label.pack()

gameframe = tkinter.Frame(root)
gameframe.columnconfigure(0, weight=0)
gameframe.columnconfigure(1, weight=0)
gameframe.columnconfigure(2, weight=0)
gameframe.columnconfigure(3, weight=0)

tile = tkinter.Label(gameframe, text='2', font = ('Clear Sans', 15))
tile2 = tkinter.Label(gameframe, text='2', font = ('Clear Sans', 15))

tile.grid(row=0, column=0)
tile2.grid(row=1, column=0)
gameframe.pack()

root.mainloop()