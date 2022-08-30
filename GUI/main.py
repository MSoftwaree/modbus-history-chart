from GUI.frames import Frames, tk
from tkinter import messagebox
import os


def on_closing():
    if messagebox.askokcancel("Exit", f"Are you sure you want to quit?\n"
                                      f"Your chart will be removed!"):
        try:
            os.remove(directory_path + 'history.jpeg')
        except:
            pass
        win.destroy()


# Window settings
win = tk.Tk()
win.title("Modbus History Chart")
width_value = win.winfo_screenwidth()
height_value = win.winfo_screenheight()
win.geometry("1200x750")
win.resizable(0, 0)

win.protocol("WM_DELETE_WINDOW", on_closing)

# Chart location
directory_path = os.getenv("APPDATA")

frames = Frames(directory_path)

# Add frames
main = frames.main_frame(win)
frames.configuration_frame(main)
frames.registers_frame(main)
frames.buttons_frame(main)
frames.chart_frame()

# Run window
win.mainloop()
