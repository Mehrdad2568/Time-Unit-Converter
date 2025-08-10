from tkinter import *
from tkinter import ttk, font
import os
main_dir = os.path.dirname(__file__)
icon_dir = os.path.abspath(os.path.join(main_dir, 'assets', 'icon.png'))
root = Tk()
root.title('Time Unit Converter')
icon = PhotoImage(file=icon_dir)
root.iconphoto(True, icon)
root.resizable(0, 0)
default_font = font.nametofont("TkDefaultFont")
root.option_add("*Font", default_font)
menu_bar = Menu()
help_menu = Menu(menu_bar, tearoff=0)
def help_page(*args):
    help_win = Toplevel(root)
    help_win.title('Help')
    help_win.resizable(0, 0)
    help_text =(
    "A simple way to convert time units when you need it!\n\n"
    "How to use:\n"
    "Enter the numbers for the time unit you are going to convert from, then select a time unit that you want to convert to. "
    'The converter has two modes, "Cumulative" and "Normal"; if you don’t check the "Cumulative" check box, the previous output '
    'will be cleared and replaced with the new output. If you check the "Cumulative" check box, the converter will output the sum '
    'of all outputs since checking the box until you press the "Clear" button or use Ctrl+0.\n\n'
    "Shortcuts:\n"
    "Calculation: Ctrl+Enter\n"
    "Clear: Ctrl+0\n"
    "Cumulative toggle: Ctrl+M\n"
    "Help: Ctrl+H\n"
    "About: Ctrl+A"
    )
    help_text_box = Text(help_win, width=40, wrap='word', height=15, spacing2=3)
    help_text_box.grid(padx=6, pady=6)
    help_text_box.insert(END, help_text)
    help_text_box.config(state=DISABLED)
    help_scrollbar = ttk.Scrollbar(help_win, orient="vertical", command=help_text_box.yview)
    help_scrollbar.grid(row=0, column=1, sticky="ns")
    help_text_box.configure(yscrollcommand=help_scrollbar.set)
    help_win.transient(root)
    help_win.grab_set()
    help_win.wait_window()
help_menu.add_command(label='View Help', command=help_page)
def about_page(*args):
    about_win = Toplevel(root)
    about_win.title('About')
    about_win.resizable(0, 0)
    about_text = (
    "Time Unit Converter\n"
    "Version 1.0.0.0\n"
    "© 2025 Mehrdad Farzane\n\n"
    "A simple and efficient tool for converting between different time units.\n"
    "Built using Python and Tkinter."
    )
    ttk.Label(about_win, text=about_text, justify=LEFT, wraplength=360).grid(padx=6, pady=6)
    about_win.transient(root)
    about_win.grab_set()
    about_win.wait_window()
help_menu.add_command(label='About', command=about_page)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)
times = ('Normal year', 'Leap year', '30 day month', '31 day month', 'Week', 'Day', 'Hour', 'Minute', 'Second', 'Millisecond')
ttk.Label(text='Year:').grid(row=0, column=0)
year_input = ttk.Entry()
year_input.grid(row=0, column=1, pady=3, padx=3)
year_radio_var = IntVar(value=365)
ttk.Radiobutton(text='Normal', value=365, variable=year_radio_var).grid(row=0, column=2)
ttk.Radiobutton(text='Leap', value=366, variable=year_radio_var).grid(row=0, column=3)
ttk.Label(text='Month:').grid(row=1, column=0)
month_input = ttk.Entry()
month_input.grid(row=1,column=1, pady=3, padx=3)
month_radio_var = IntVar(value=30)
ttk.Radiobutton(text='30', value=30, variable=month_radio_var).grid(row=1, column=2)
ttk.Radiobutton(text='31', value=31, variable=month_radio_var).grid(row=1, column=3)
ttk.Label(text='Week:').grid(row=2, column=0)
week_input = ttk.Entry()
week_input.grid(row=2, column=1, pady=3, padx=3)
ttk.Label(text='Day:').grid(row=3, column=0)
day_input = ttk.Entry()
day_input.grid(row=3, column=1, pady=3, padx=3)
ttk.Label(text='Hour:').grid(row=4, column=0)
hour_input = ttk.Entry()
hour_input.grid(row=4, column=1, pady=3, padx=3)
ttk.Label(text='Minute:').grid(row=5, column=0)
minute_input = ttk.Entry()
minute_input.grid(row=5, column=1, pady=3, padx=3)
ttk.Label(text='Second:').grid(row=6, column=0)
second_input = ttk.Entry()
second_input.grid(row=6, column=1, pady=3, padx=3)
ttk.Label(text='Millisecond:').grid(row=7, column=0)
millisecond_input = ttk.Entry()
millisecond_input.grid(row=7, column=1, pady=3, padx=3)
entry_color_style = ttk.Style()
entry_color_style.configure("Valid.TEntry", foreground="black")
entry_color_style.configure("Invalid.TEntry", foreground="red")
output_var = StringVar()
radio_column = -1
ttk.Label(text='Output forms:').grid(row=8, column=0)
for time in times[0:5]:
    radio_column += 1
    ttk.Radiobutton(text=time, value=time, variable=output_var).grid(row=9, column=radio_column)
radio_column = -1
for time in times[5:10]:
    radio_column += 1
    ttk.Radiobutton(text=time, value=time, variable=output_var).grid(row=10, column=radio_column)
res = 0
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
inputs = (
    year_input, month_input, week_input, day_input,
    hour_input, minute_input, second_input, millisecond_input
    )
def digit_rounder(value):
    return int(value) if value % 1 == 0 else value
ms = 1
s  = ms * 1000
m = 60 * s
h = 60 * m
d = 24 * h
w = 7 * d
DIVISION_TABLE = {
        'Normal year': 365 * d,
        'Leap year': 366 * d,
        '30 day month': 30 * d,
        '31 day month': 31 * d,
        'Week': w,
        'Day': d,
        'Hour': h,
        'Minute': m,
        'Second': s,
        'Millisecond': ms,
    }
def divisor_units(choice):
    return DIVISION_TABLE.get(choice)
def calculation(*args):
    clear_button.config(state=NORMAL)
    global res
    if checkbox_var.get() == 0:
        res = 0
    output_text.config(state=NORMAL)
    try:
        year_data, month_data, week_data, day_data, hour_data, minute_data, second_data, millisecond_data = (
            0 if inp.get() == '' else float(inp.get()) for inp in inputs
        )
        res += millisecond_data + (second_data * s) + (minute_data * m) + (hour_data * h) + (day_data * d) + (week_data * w) + (month_data * month_radio_var.get() * d) + (year_data * year_radio_var.get() * d)
        choice = output_var.get()
        divisor = divisor_units(choice)
        if not divisor:
            output = 'Please select an output form.'
        else:
            output = digit_rounder(res / divisor)
        output_text.delete(1.0, END)
        try:
            output_text.insert(END, f"{output:,} {output_var.get()+('' if output == 1 else 's')}")
        except ValueError:
            output_text.insert(END, output)
    except ValueError:
        output_text.config(state=NORMAL)
        output_text.delete(1.0, END)
        output_text.insert(END, "Please enter float numbers.")
    output_text.config(state=DISABLED)
def validate_entry(event):
    widget = event.widget
    widget.configure(style="Valid.TEntry" if isfloat(widget.get()) else "Invalid.TEntry")
    toggle_calculate_button()
def res_clearer(*args):
    global res
    res = 0
    for inp in inputs:
        inp.delete(0, END)
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)
    output_text.config(state=DISABLED)
    clear_button.config(state=DISABLED)
calculate_button = ttk.Button(text='Calculate', command=calculation, width=88)
calculate_button.grid(column=1, columnspan=4, pady=3, padx=3)
checkbox_var = IntVar(value=0)
ttk.Checkbutton(text='Cumulative', variable=checkbox_var).grid(row=11, padx=3)
calculate_button.config(state=DISABLED)
def toggle_calculate_button(*args):
    if output_var.get() and all(isfloat(inp.get()) or inp.get() == '' for inp in inputs):
        calculate_button.config(state=NORMAL)
    else:
        calculate_button.config(state=DISABLED)
output_text = Text(width=112, height=3)
output_text.grid(columnspan=5)
output_text.config(state=DISABLED)
clear_button = ttk.Button(text='Clear', command=res_clearer, width=112)
clear_button.grid(columnspan=5, pady=3, padx=3)
clear_button.config(state=DISABLED)
root.bind('<Control-Return>', calculation)
root.bind('<Control-0>', res_clearer)
root.bind('<Control-H>', help_page)
root.bind('<Control-h>', help_page)
root.bind('<Control-A>', about_page)
root.bind('<Control-a>', about_page)
def checkbox_shortcut(*args):
    checkbox_var.set(not checkbox_var.get())
root.bind('<Control-M>', checkbox_shortcut)
root.bind('<Control-m>', checkbox_shortcut)
output_var.trace_add("write", toggle_calculate_button)
for inp in inputs:
    inp.bind("<KeyRelease>", validate_entry)
root.mainloop()
