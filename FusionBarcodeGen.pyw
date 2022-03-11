import tkinter as tk
from tkinter import ttk, messagebox

class FusionBarcodeGen:
    def __init__(self, window):
        window.title("FusionBarcodeGen")
        window.grid_columnconfigure(0, weight = 1, uniform = "half")
        window.grid_columnconfigure(1, weight = 1, uniform = "half")
        self.outerInput = ttk.LabelFrame(window, text = "Input")
        self.outerInput.grid(row = 0, column = 0, padx = 8, pady = 8, sticky = "NSEW")
        self.outerInput.grid_rowconfigure(0, weight = 1)
        self.outerInput.grid_columnconfigure(0, weight = 1)
        self.innerInput = ttk.Frame(self.outerInput)
        self.innerInput.grid(row = 0, column = 0, padx = 4, pady = 4, sticky = "NSEW")
        self.innerInput.grid_columnconfigure(0, weight = 1)
        self.innerInput.grid_rowconfigure(0, weight = 1)
        self.numInputText = tk.StringVar()
        self.numInput = ttk.Entry(self.innerInput, textvariable = self.numInputText, width = 12)
        self.numInput.grid(row = 0, column = 0, padx = 4, pady = 4)
        self.generate = ttk.Button(self.innerInput, text = "Generate", command = lambda: self.generateBarcode())
        self.generate.grid(row = 1, column = 0, padx = 4, pady = 4)
        self.outerBarcode = ttk.LabelFrame(window, text = "Barcode")
        self.outerBarcode.grid(row = 0, column = 1, padx = 8, pady = 8, sticky = "NSEW")
        self.outerBarcode.grid_rowconfigure(0, weight = 1)
        self.outerBarcode.grid_columnconfigure(0, weight = 1)
        self.innerBarcode = ttk.Frame(self.outerBarcode)
        self.innerBarcode.grid(row = 0, column = 0, padx = 4, pady = 4, sticky= "NSEW")
        self.innerBarcode.grid_columnconfigure(0, weight = 1)
        self.innerBarcode.grid_rowconfigure(0, weight = 1)
        self.barcode = tk.Canvas(self.innerBarcode, bg = "black", highlightthickness = 0, height = 32, width = 64)
        self.barcode.grid(row = 0, column = 0)

    def generateBarcode(self):
        self.barcode.delete("all")
        try:
            input = int(self.numInput.get())
            if ( 0 <= input <= 255 ):
                binaryText = format(input, "08b")[::-1]
                j = 16

                for i in range(0, len(binaryText)):
                    if binaryText[i] == '0':
                        self.barcode.create_line(j + 1, 32, j + 1, 0, width = 2, fill = "black")
                        self.barcode.create_line(j + 3, 32, j + 3, 0, width = 2, fill = "white")
                    elif binaryText[i] == '1':
                        self.barcode.create_line(j + 1, 32, j + 1, 0, width = 2, fill = "white")
                        self.barcode.create_line(j + 3, 32, j + 3, 0, width = 2, fill = "black")
                    j += 4
            else:
                msgBox = messagebox.showerror("Error", "Input is not in [0, 255]!")
        except:
            msgBox = messagebox.showerror("Error", "Input is not an integer!")

def main():
    root = tk.Tk()
    root.resizable(0, 0)
    gui = FusionBarcodeGen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
