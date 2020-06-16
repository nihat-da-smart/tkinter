import tkinter as tk
import pandas as pd

root = tk.Tk()

diabetes = pd.read_csv('pima-indians-diabetes.csv')


explanation = diabetes

w2 = tk.Label(root,
              justify=tk.LEFT,
              padx = 10,
              text=explanation).pack(side="left")
root.mainloop()



