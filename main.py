import tkinter as tk
from tkinter import ttk, font
import os


lang_dict = {
    'en': {
        'main_title': 'Time Unit Converter',
        'help': 'Help',
        'about': 'About',
        'help_text': 'A simple way to convert time units when you need it!\n\n'
                        'How to use:\n'
                        'Enter the numbers for the time unit you are going to convert from, then select a time unit that you want to convert to. '
                        'The converter has two modes, "Cumulative" and "Normal"; if you don’t check the "Cumulative" check box, the previous output '
                        'will be cleared and replaced with the new output. If you check the "Cumulative" check box, the converter will output the sum '
                        'of all outputs since checking the box until you press the "Clear" button or use Ctrl+0. You can also change the language'
                        'with the language dropdown menu at the top right corner of the app.\n\n'
                        'Shortcuts:\n'
                        'Calculation: Ctrl+Enter\n'
                        'Clear: Ctrl+0\n'
                        'Cumulative toggle: Ctrl+M\n'
                        'Help: Ctrl+H\n'
                        'About: Ctrl+A',
        'about_text': 'Time Unit Converter\n'
                        'Version 2.0.0.0\n'
                        '© 2025 Mehrdad Farzane\n\n'
                        'A simple and efficient tool for converting between different time units.\n'
                        'Built using Python and Tkinter.',
        'view_help': 'View Help',
        'normal_year': 'Normal year',
        'leap_year': 'Leap year',
        'year': 'Year',
        'month': 'month',
        '30_day_month': '30 day month',
        '31_day_month': '31 day month',
        'week': 'Week',
        'day': 'Day',
        'hour': 'Hour',
        'minute': 'Minute',
        'second': 'Second',
        'millisecond': 'Millisecond',
        'normal_option': 'Normal',
        'leap_option': 'Leap',
        '30_option': '30',
        '31_option': '31',
        'output_forms': 'Output forms',
        'calculate': 'Calculate',
        'cumulative': 'Cumulative',
        'clear': 'Clear',
        'output_form_not_selected_error': 'Please select an output form.',
        'invalid_value_error': 'Please enter float numbers.',
        'language': 'Language',
        'justify': tk.LEFT,
    },
    'فا': {
        'main_title': 'مبدل یکای زمان',
        'help': 'کمک',
        'about': 'درباره',
        'help_text': 'راهی ساده برای تبدیل یکا های زمانی وقتی به آن نیاز !دارید\n\n'
                        ':نحوه استفاده\n'
                        'اعداد یکای زمانی که می‌خواهید آن را تبدیل کنید را وارد کنید، سپس یکای زمانی ای را که می‌خواهید به آن تبدیل کنید را انتخاب کنید. '
                        'مبدل دو حالت دارد، حالت «جمع» و حالت «عادی»; اگر گزینه «جمع» را انتخاب نکنید، خروجی قبلی '
                        'پاک می‌شود و خروجی جدید جای آن را می‌گیرد. اگر گزینه «جمع» را انتخاب کنید، مبدل مجموع همه خروجی ها '
                        'از زمانی  که گزینه انتخاب شد  تا  زمانی که دکمه «پاک کردن» را فشار دهید یا از'
                        '\u202A Ctrl+0 \u202C'
                        'استفاده کنید. می‌توانید با استفاده از منوی تغییر زبان در بالا سمت چپ نرم افزار زبان را تغییر دهید.\u200F\n\n'
                        ':میانبر ها\n'
                        'Ctrl+Enter :محاسبه\n'
                        'Ctrl+۰ :پاک کردن\n'
                        'Ctrl+M :گزینه جمع\n'
                        'Ctrl+H :کمک\n'
                        'Ctrl+A :درباره',
        'about_text': 'مبدل یکای زمان\n'
                        'نسخه ۲.۰.۰.۰\n'
                        '© 2025 مهرداد فرزانه \n\n'
                        '.یک ابزار ساده و بهینه برای تبدیل میان یکا های زمانی متفاوت\n'
                        '.ساخته شده با استفاده از پایتون و تیکینتر',
        'view_help': 'مشاهده کمک',
        'normal_year': 'سال عادی',
        'leap_year': 'سال کبیسه',
        'year': 'سال',
        'month': 'ماه',
        '30_day_month': 'ماه ۳۰ روزه',
        '31_day_month': 'ماه ۳۱ روزه',
        'week': 'هفته',
        'day': 'روز',
        'hour': 'ساعت',
        'minute': 'دقیقه',
        'second': 'ثانیه',
        'millisecond': 'میلی‌ثانیه',
        'normal_option': 'عادی',
        'leap_option': 'کبیسه',
        '30_option': '۳۰',
        '31_option': '۳۱',
        'output_forms': 'شیوه های خروجی',
        'calculate': 'محاسبه',
        'cumulative': 'جمع',
        'clear': 'پاک کردن',
        'output_form_not_selected_error': 'لطفا یک شیوه خروجی انتخاب کنید.',
        'invalid_value_error': 'لطفا اعداد گویا وارد کنید.',
        'language': 'زبان',
        'justify': tk.RIGHT,
    }
}


windows_list = []
label_w_colon_list = []
menu_items_list = []
other_widgets_list = []
justify_list = []


main_dir = os.path.dirname(__file__)
icon_dir = os.path.abspath(os.path.join(main_dir, 'assets', 'icon.png'))
root = tk.Tk()
current_lang = tk.StringVar(value='en')


def lang_selection(key):
    '''
    Returns the correct translation of the key according to the selected language
    '''
    return lang_dict.get(current_lang.get(), {}).get(key, f'[{key}]')


def reg_window(window, key):
    '''
    Adds a new window to the windows_list
    '''
    windows_list.append((window, key))


def reg_label_w_colon(label, key, row=None, column=None, padx=0, pady=0, columnspan=1):
    '''
    Adds a new label with colon widget to the label_w_colon_list
    '''
    label_w_colon_list.append((label, key))
    justify_list.append((label, row, column, padx, pady, columnspan))


def reg_entry_textbox_dropdownmenus(widget, row=None, column=None, padx=0, pady=0, columnspan=1):
    '''
    Adds a new entry, textbox or dropdown widget to the justify_list
    '''    
    justify_list.append((widget, row, column, padx, pady, columnspan))


def reg_menu_item(menu, key, **command):
    '''
    Adds a new menu item to the menu-items_list
    '''
    menu.add_command(label=lang_selection(key), **command)
    idx = menu.index('end')
    menu_items_list.append((menu, idx, key))


def reg_menu_cascade(menu, key,submenu):
    menu.add_cascade(label=lang_selection(key), menu=submenu)
    idx = menu.index('end')
    menu_items_list.append((menu, idx, key))


def reg_other_widget(widget, key, row=None, column=None, padx=0, pady=0, columnspan=1):
    '''
    Adds a new widget to the other_widgets_list
    '''
    other_widgets_list.append((widget, key))
    justify_list.append((widget, row, column, padx, pady, columnspan))


def justify_widgets(num):
    '''
    Justifies the wisgets based on the selected languag
    '''
    return num if lang_selection('justify') == tk.LEFT or num is None else root.grid_size()[0] - 1 - num


def justify_colons(key):
    '''
    Justifies the colons based on the slected language
    '''
    return f'{lang_selection(key)}:' if lang_selection('justify') == tk.LEFT else f':{lang_selection(key)}'


def refresh(*args):
    '''
    Refreshes the every registered window, widgets and menus
    '''
    for window, key in windows_list:
        window.title(lang_selection(key))
    for widget, key in other_widgets_list:
        try:
            widget.config(text=lang_selection(key))
        except Exception as e:
            print('There was a problem updating this widget', widget, key, e)
    for label, key in label_w_colon_list:
        label.config(text=justify_colons(key))
    for widget, row, column, padx, pady, columnspan in justify_list:
        widget.grid(row=row, column=justify_widgets(column), padx=padx, pady=pady, columnspan=columnspan)              
    for menu, idx, key in menu_items_list:
        try:
            menu.entryconfig(idx, label=lang_selection(key))
        except Exception as e:
            print('There was a problem updating this widget', menu, idx, key, e)


current_lang.trace_add('write', refresh)


reg_window(root, 'main_title')
icon = tk.PhotoImage(file=icon_dir)
root.iconphoto(True, icon)
root.resizable(0, 0)
default_font = font.nametofont('TkDefaultFont')
root.option_add('*Font', default_font)
menu_bar = tk.Menu()
help_menu = tk.Menu(menu_bar, tearoff=0)


def help_page(*args):
    '''
    Creates a help page when the user requests it to be made.
    '''
    help_win = tk.Toplevel(root)
    help_win.title(lang_selection('help'))
    help_win.resizable(0, 0)
    help_text_box = tk.Text(help_win, width=40, wrap='word', height=15, spacing2=3, )
    help_text_box.grid(padx=6, pady=6)
    help_text_box.tag_configure('justify_tag', justify=lang_selection('justify'))
    help_text_box.insert(tk.END, lang_selection('help_text'), 'justify_tag')
    help_text_box.config(state=tk.DISABLED)
    help_scrollbar = ttk.Scrollbar(help_win, orient='vertical', command=help_text_box.yview)
    help_scrollbar.grid(row=0, column=1, sticky='ns')
    help_text_box.configure(yscrollcommand=help_scrollbar.set)
    help_win.transient(root)
    help_win.grab_set()
    help_win.wait_window()
reg_menu_item(help_menu, 'view_help', command=help_page)


def about_page(*args):
    '''
    Creates an about page when the user request it to be made.
    '''
    about_win = tk.Toplevel(root)
    about_win.title(lang_selection('about'))
    about_win.resizable(0, 0)
    ttk.Label(about_win, text=lang_selection('about_text'), justify=lang_selection('justify'), wraplength=360).grid(padx=6, pady=6)
    about_win.transient(root)
    about_win.grab_set()
    about_win.wait_window()


reg_menu_item(help_menu, 'about', command=about_page)
reg_menu_cascade(menu_bar, 'help', help_menu)
root.config(menu=menu_bar)

times = (
    'normal_year',
    'leap_year',
    '30_day_month',
    '31_day_month',
    'week',
    'day',
    'hour',
    'minute',
    'second',
    'millisecond'
    )
year_label = ttk.Label()
reg_label_w_colon(year_label, 'year', 0, 0)
year_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(year_input, 0, 1, 3, 3)
year_radio_var = tk.IntVar(value=365)
normal_year_opt = ttk.Radiobutton(value=365, variable=year_radio_var)
reg_other_widget(normal_year_opt, 'normal_option', 0, 2)
leap_year_opt = ttk.Radiobutton(value=366, variable=year_radio_var)
reg_other_widget(leap_year_opt, 'leap_option', 0, 3)
lang_label = ttk.Label()
reg_label_w_colon(lang_label, 'language', 0, 4)
lang_opt_menu = ttk.OptionMenu(root, current_lang, 'en', *lang_dict.keys())
reg_entry_textbox_dropdownmenus(lang_opt_menu, 0, 5)
month_label = ttk.Label()
reg_label_w_colon(month_label, 'month', 1, 0)
month_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(month_input, 1, 1, 3, 3)
month_radio_var = tk.IntVar(value=30)
thirty_month_opt = ttk.Radiobutton(value=30, variable=month_radio_var)
reg_other_widget(thirty_month_opt, '30_option', 1, 2)
thirty_one_month_opt = ttk.Radiobutton(value=31, variable=month_radio_var)
reg_other_widget(thirty_one_month_opt, '31_option', 1, 3)
week_label = ttk.Label()
reg_label_w_colon(week_label, 'week', 2, 0)
week_input = ttk.Entry()
week_input.grid(row=2, column=justify_widgets(1), pady=3, padx=3)
reg_entry_textbox_dropdownmenus(week_input, 2, 1, 3, 3)
day_label = ttk.Label()
reg_label_w_colon(day_label, 'day', 3, 0)
day_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(day_input, 3, 1, 3, 3)
hour_label = ttk.Label()
reg_label_w_colon(hour_label, 'hour', 4, 0)
hour_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(hour_input, 4, 1, 3, 3)
minute_label = ttk.Label()
reg_label_w_colon(minute_label, 'minute', 5, 0)
minute_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(minute_input, 5, 1, 3, 3)
second_label = ttk.Label()
reg_label_w_colon(second_label, 'second', 6, 0)
second_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(second_input, 6, 1, 3, 3)
millisecond_label = ttk.Label()
reg_label_w_colon(millisecond_label, 'millisecond', 7, 0)
millisecond_input = ttk.Entry()
reg_entry_textbox_dropdownmenus(millisecond_input, 7, 1, 3, 3)
entry_color_style = ttk.Style()
entry_color_style.configure('Valid.TEntry', foreground='black')
entry_color_style.configure('Invalid.TEntry', foreground='red')
output_var = tk.StringVar()
radio_column = -1
output_form_label = ttk.Label()
reg_label_w_colon(output_form_label, 'output_forms', 8, 0)
for time in times[0:5]:
    radio_column += 1
    reg_other_widget(ttk.Radiobutton(value=time, variable=output_var), time, 9, radio_column)
radio_column = -1
for time in times[5:10]:
    radio_column += 1
    reg_other_widget(ttk.Radiobutton(value=time, variable=output_var), time, 10, radio_column)
res_var = tk.DoubleVar(value=0)


def isfloat(value):
    '''
    Checks if the value is float or not.
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False
inputs = (
    year_input, month_input, week_input, day_input,
    hour_input, minute_input, second_input, millisecond_input
    )


ms = 1
s  = ms * 1000
m = 60 * s
h = 60 * m
d = 24 * h
w = 7 * d
DIVISION_TABLE = {
        'normal_year': 365 * d,
        'leap_year': 366 * d,
        '30_day_month': 30 * d,
        '31_day_month': 31 * d,
        'week': w,
        'day': d,
        'hour': h,
        'minute': m,
        'second': s,
        'millisecond': ms
    }


def calculation(*args):
    '''
    Calculates the result using the user's inputs.
    '''
    res = 0
    clear_button.config(state=tk.NORMAL)
    output_text.config(state=tk.NORMAL)
    output_text.tag_configure('justify_tag', justify=tk.RIGHT)
    try:
        year_data, month_data, week_data, day_data, hour_data, minute_data, second_data, millisecond_data = (
            0 if inp.get() == '' else float(inp.get()) for inp in inputs
        )
        res += millisecond_data + (second_data * s) + (minute_data * m) + (hour_data * h) + (day_data * d) + (week_data * w) + (month_data * month_radio_var.get() * d) + (year_data * year_radio_var.get() * d)
        if checkbox_var.get() == 0:
            res_var.set(res)
        else:
            res_var.set(res_var.get() + res)
        choice = output_var.get()
        multiplier = DIVISION_TABLE.get(choice)
        if not multiplier:
            output = lang_selection('output_form_not_selected_error')
        else:
            output = int(res_var.get() / multiplier) if (res_var.get() / multiplier) % 1 == 0 else res_var.get() / multiplier
        output_text.delete(1.0, tk.END)
        try:
            if lang_selection('justify') == tk.LEFT:
                output_text.insert(tk.END, f'{output:,} {lang_selection(output_var.get())+('' if output == 1 else 's')}')
            else:
                output_text.insert(tk.END, f'\u200F{output:,} {lang_selection(output_var.get())}', 'justify_tag')
        except ValueError:
            output_text.insert(tk.END, output)
    except ValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, lang_selection('invalid_value_error'))
    output_text.config(state=tk.DISABLED)


def validate_entry(event):
    '''
    Validate the entries' inputs by using the isfloat function.
    '''
    widget = event.widget
    widget.configure(style='Valid.TEntry' if isfloat(widget.get()) else 'Invalid.TEntry')
    toggle_calculate_button()


def res_clearer(*args):
    '''
    Clears the output as well as the entries.
    '''
    res_var.set(0)
    for inp in inputs:
        inp.delete(0, tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.config(state=tk.DISABLED)
    clear_button.config(state=tk.DISABLED)
calculate_button = ttk.Button(command=calculation, width=120)
reg_other_widget(calculate_button, 'calculate', 13, padx=3, pady=3, columnspan=6)
checkbox_var = tk.IntVar(value=0)
cumulative_checkbox = ttk.Checkbutton(variable=checkbox_var)
reg_other_widget(cumulative_checkbox, 'cumulative', 11, padx=3)
calculate_button.config(state=tk.DISABLED)


def toggle_calculate_button(*args):
    '''
    Disable or enable the 'Calculate' button based on the validity of the user's inputs.
    '''
    if output_var.get() and all(isfloat(inp.get()) or inp.get() == '' for inp in inputs):
        calculate_button.config(state=tk.NORMAL)
    else:
        calculate_button.config(state=tk.DISABLED)


output_text = tk.Text(width=120, height=3)
reg_entry_textbox_dropdownmenus(output_text, 12, columnspan=6)
output_text.config(state=tk.DISABLED)
clear_button = ttk.Button(command=res_clearer, width=120)
reg_other_widget(clear_button, 'clear', 14, padx=3, pady=3, columnspan=6)
clear_button.config(state=tk.DISABLED)
root.bind('<Control-Return>', calculation)
root.bind('<Control-0>', res_clearer)
root.bind('<Control-H>', help_page)
root.bind('<Control-h>', help_page)
root.bind('<Control-A>', about_page)
root.bind('<Control-a>', about_page)
root.bind('<Control-M>', lambda _: checkbox_var.set(not checkbox_var.get()))
root.bind('<Control-m>', lambda _: checkbox_var.set(not checkbox_var.get()))
output_var.trace_add('write', toggle_calculate_button)
for inp in inputs:
    inp.bind('<KeyRelease>', validate_entry)
refresh()
root.mainloop()
