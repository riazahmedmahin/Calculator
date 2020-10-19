import tikinder as tk
import time as tm
def display_time():
    current_time  =tm.staftime('%I:%M:&S:%p')
    clock_label["text"]=current_time
    clock_label.after(5000,display_time)

'''my_window =tk.Tk()
my_window.title("Digital Clock")
clock_label=tk.Label(my_window,font="arial 80",bg="black",fg="red")
clock_label.grid(row=0,column=0)
display_time()'''
my_window.mainloop()