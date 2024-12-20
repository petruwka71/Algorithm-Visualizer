import tkinter as tk
import random

class AlgorithmVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.array = [random.randint(10, 300) for _ in range(50)]
        self.bars = []
        self.create_bars()

        self.start_button = tk.Button(root, text="Start Bubble Sort", command=self.start_sort)
        self.start_button.pack(pady=10)

    def create_bars(self):
        self.canvas.delete("all")
        bar_width = 800 // len(self.array)
        self.bars = []
        for i, height in enumerate(self.array):
            x0 = i * bar_width
            y0 = 400 - height
            x1 = x0 + bar_width - 2
            y1 = 400
            bar = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            self.bars.append(bar)

    def start_sort(self):
        self.bubble_sort()

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.update_bars(j, j+1)
        
    def update_bars(self, idx1, idx2):
        self.canvas.itemconfig(self.bars[idx1], fill="red")
        self.canvas.itemconfig(self.bars[idx2], fill="red")
        self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]
        self.create_bars()
        self.root.update_idletasks()
        self.canvas.itemconfig(self.bars[idx1], fill="blue")
        self.canvas.itemconfig(self.bars[idx2], fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    visualizer = AlgorithmVisualizer(root)
    root.mainloop()
