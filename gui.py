import tkinter as tk
import core

def main():
    root = tk.Tk()
    root.title("Simple Calculator by @dev-kas")
    root.geometry("240x420")
    root.resizable(False, False)

    entry = tk.Entry(root, width=15, font=("Consolas", 20), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    localworkspace = ""
    tokLenHistory = []
    localTokLenHistory = []
    translation_map = {
        "xʸ": "^", "⅟x": "1/",
        "x²": "^2", "√x": "^0.5",
        "÷": "/", "×": "*",
    }

    visible_map = {
        "xʸ": "^", "⅟x": "1/",
        "x²": "²", "√x": "'s √ ",
    }

    button_layout = [
        "(",  ")",  "xʸ", "←",
        "⅟x", "x²", "√x", "÷",
        "7",  "8",  "9",  "×",
        "4",  "5",  "6",  "-",
        "1",  "2",  "3",  "+",
        "%",  "0",  ".",  "=",
    ]

    def on_button_click(b):
        nonlocal localworkspace
        if b == "=" :
            if localworkspace == "": return
            core.run()
            entry.delete(0, tk.END)
            entry.insert(0, core.get_workspace())
            entry.xview_moveto(1)
            localworkspace = ""
            tokLenHistory.clear()
            localTokLenHistory.clear()
            core.set_workspace("")
            return
        elif b == "←":
            entry.delete(0, tk.END)
            entry.insert(0, localworkspace)
            if not (localworkspace != "" and len(tokLenHistory) > 0 and len(localTokLenHistory) > 0): return
            localworkspace = localworkspace[:-localTokLenHistory.pop()]
            core.set_workspace(core.get_workspace()[:-tokLenHistory.pop()])
        else:
            localworkspace += visible_map.get(b, b)
            localTokLenHistory.append(len(visible_map.get(b, b)))

            core.write_workspace(translation_map.get(b, b))
            tokLenHistory.append(len(translation_map.get(b, b)))

        entry.delete(0, tk.END)
        entry.insert(0, localworkspace)
        entry.xview_moveto(1)

    for i, b in enumerate(button_layout):
        tk.Button(root, text=b, width=4, height=2,
                  font=("Consolas", 14),
                  command=lambda b=b: on_button_click(b)).grid(row=i // 4 + 1, column=i % 4)

    root.mainloop()
