import json
import random
import subprocess
import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog, messagebox, colorchooser
import pyautogui
import pyperclip
import os
from SLanguage import SLanguage


# 文件路径
webnamedata_path = 'webname.txt'
webpathdata_path = 'webpath.txt'
appnamedata_path = 'appname.txt'
apppathdata_path = 'apppath.txt'
colorpath = "color.txt"

# 定义文件路径

options = "options.txt"

if not os.path.exists(options):
    with open(options, 'w', encoding='utf-8') as file:
        # 将字典转换为JSON格式的字符串
        my_dict = {"screenshot_save_path":"","bg":"#ffffff","open_path":'false','slider_value':"1",'language':'chinese'}
        json_str = json.dumps(my_dict, ensure_ascii=False, indent=4)
        # 将字符串写入文件
        file.write(json_str)

with open(options, 'r', encoding='utf-8') as file:
    # 读取文件的全部内容
    json_str = file.read()
    # 将JSON字符串转换回字典
    _options = json.loads(json_str)
screenshot_save_path = _options["screenshot_save_path"]
bg = _options['bg']
open_path = _options["open_path"]
Language = SLanguage(_options)


try:
    # 检查文件是否存在
    if not os.path.exists(screenshot_save_path):
        # 拆分路径为目录和文件名
        dir_name, file_name = os.path.split(screenshot_save_path)

        # 如果目录不存在，则创建目录
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

            # 创建文件
        with open(screenshot_save_path, 'w') as file:
            file.write('This is a new file.\n')
            print(f"文件 {screenshot_save_path} 已创建。")
    else:
        print(f"文件 {screenshot_save_path} 已存在。")
except:
    pass


# 现在可以像之前那样检查文件是否存在并创建它
if not os.path.exists(webnamedata_path):
    with open(webnamedata_path, 'w') as file:
        # 将列表转换为字符串并写入文件
        # 使用join方法将列表元素连接成一个字符串，每个元素之间用换行符分隔
        file.write('add')


with open(webnamedata_path, 'r') as file:
    # 读取文件的所有行并保存为一个列表
    # splitlines方法按行分割字符串，返回一个列表
    web_1 = file.read().splitlines()
    print(web_1)




# 现在可以像之前那样检查文件是否存在并创建它
if not os.path.exists(webpathdata_path):
    with open(webpathdata_path, 'w', encoding='utf-8') as file:
        # 将字典转换为JSON格式的字符串
        my_dict = {}
        json_str = json.dumps(my_dict, ensure_ascii=False, indent=4)
        # 将字符串写入文件
        file.write(json_str)
else:
    print(f"文件 {webpathdata_path} 已存在。")
with open(webpathdata_path, 'r', encoding='utf-8') as file:
    # 读取文件的全部内容
    json_str = file.read()
    # 将JSON字符串转换回字典
    webpath_1 = json.loads(json_str)


# 现在可以像之前那样检查文件是否存在并创建它
if not os.path.exists(appnamedata_path):
    with open(appnamedata_path, 'w') as file:
        # 将列表转换为字符串并写入文件
        # 使用join方法将列表元素连接成一个字符串，每个元素之间用换行符分隔
        file.write('add')
else:
    print(f"文件 {appnamedata_path} 已存在。")

with open(appnamedata_path, 'r') as file:
    # 读取文件的所有行并保存为一个列表
    # splitlines方法按行分割字符串，返回一个列表
    app_1 = file.read().splitlines()
    print(app_1)




# 现在可以像之前那样检查文件是否存在并创建它
if not os.path.exists(apppathdata_path):
    with open(apppathdata_path, 'w', encoding='utf-8') as file:
        # 将字典转换为JSON格式的字符串
        my_dict = {}
        json_str = json.dumps(my_dict, ensure_ascii=False, indent=4)
        # 将字符串写入文件
        file.write(json_str)

with open(apppathdata_path, 'r', encoding='utf-8') as file:
    # 读取文件的全部内容
    json_str = file.read()
    # 将JSON字符串转换回字典
    apppath_1 = json.loads(json_str)

initial_text = ">"
app = []
web = []
for i in app_1:
    app.append(i)

for i in web_1:
    web.append(i)

app_path = apppath_1
web_path = webpath_1
debug=['app_data','app_path_data','options_data','web_data','web_path_data']
path = []
browser = []
completions_1 = ["open",                      "quit", "screenshot", "settings",'debug']
completions_2 = [["app", "web",],        [""],       ["full"],         [""]      ,      debug]
completions_3 = [app,      web,              [""],         [""],             [""],            [""]]
completions_4 = [[""],     [""],               [""],          [""],                [""],          [""]]
completions = [completions_1, completions_2, completions_3, completions_4]


def replace_last_word(sentence, new_word):
    # 将句子按空格分割成单词列表
    words = sentence.split(" ")
    # 检查列表是否为空
    if words:
        # 替换最后一个单词
        words[-1] = new_word
        # 将单词列表重新组合成句子
        new_sentence = ' '.join(words)
    else:
        # 如果句子为空，返回原始句子或新单词（取决于您想要的行为）
        new_sentence = ">"
    return new_sentence


class NoBorderWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)  # 移除窗口边框
        self.geometry("300x200")  # 设置窗口大小
        self.bind("<B1-Motion>", self.on_move)  # 绑定鼠标左键拖动事件
        self.bind("<Button-1>", self.on_mouse_down)  # 绑定鼠标左键按下事件
        self.bind("<ButtonRelease-1>", self.on_mouse_up)  # 绑定鼠标左键释放事件
        self.x_offset = self.y_offset = 0  # 鼠标相对于窗口左上角的偏移量

    def on_mouse_down(self, event):
        # 获取鼠标相对于窗口左上角的坐标
        self.x_offset = event.x
        self.y_offset = event.y

    def on_move(self, event):
        # 计算新的窗口位置
        x = self.winfo_x() - self.x_offset + event.x
        y = self.winfo_y() - self.y_offset + event.y
        # 移动窗口到新位置
        self.geometry(f"+{int(x)}+{int(y)}")

    def on_mouse_up(self, event):
        # 在这里可以添加鼠标释放时的处理逻辑，如果需要的话
        pass

    # 创建并运行无边框窗口


class AutoCompleteEntry(tk.Entry):
    def __init__(self, master, completions_1, completions_2, completions_3, font=None, **kwargs):
        super().__init__(master, font=font, **kwargs)  # 传递font和其他关键字参数
        self.cmdele = [""]
        self.ele = ["", "", ""]
        self.completions_1 = completions_1
        self.completions_2 = completions_2
        self.completions_3 = completions_3
        self.completions = [self.completions_1, self.completions_2, self.completions_3]
        self.var = tk.StringVar()
        self.var.trace("w", self.changed)
        self["textvariable"] = self.var
        self.bind("<KeyPress>", self.on_key_press)

    def changed(self, *args):

        try:
            self.cmdele.clear()
            for i in range(len(self.var.get().split(">/")[1].split(" "))):
                self.cmdele.append(self.var.get().split(">/")[1].split(" ")[i])
                print(self.cmdele)
        except:
            self.cmdele = [""]

        if self.cmdele[0] in self.completions_1:
            self.ele[0] = self.cmdele[0]

    def _list(self, list, ele):
        try:
            num = list.index(ele)
        except:
            num = 0

        return num

    def on_key_press(self, event):
        if event.char == "\t":  # Tab key
            print(self.cmdele)
            if len(self.cmdele) == 1:
                for possible in self.completions_1:
                    if self.cmdele[0] in possible and self.cmdele[0] != possible:
                        original_sentence = self.var.get()
                        new_word = possible
                        print(possible)
                        modified_sentence = ">/" + replace_last_word(original_sentence, new_word)

                        self.delete(0, tk.END)
                        self.insert(0, modified_sentence)
                        return "break"
                        break
                    elif self.cmdele[0] == possible:
                        try:
                            new_word = self.completions_1[self._list(self.completions_1, possible) + 1]
                        except:
                            new_word = self.completions_1[0]
                        original_sentence = self.var.get()
                        modified_sentence = ">/" + replace_last_word(original_sentence, new_word)
                        self.delete(0, tk.END)
                        self.insert(0, modified_sentence)
                        return "break"
                        break
            elif len(self.cmdele) == 2:
                if self.cmdele[0] == "open":
                    for possible in self.completions_2[0]:
                        if self.cmdele[1] in possible and self.cmdele[1] != possible:
                            original_sentence = self.var.get()
                            new_word = possible
                            # print(possible)
                            modified_sentence = replace_last_word(original_sentence, new_word)

                            self.delete(0, tk.END)
                            self.insert(0, modified_sentence)
                            return "break"
                            break
                        elif self.cmdele[1] == possible:
                            try:
                                new_word = self.completions_2[0][self._list(self.completions_2[0], possible) + 1]
                            except:
                                new_word = self.completions_2[0][0]
                            original_sentence = self.var.get()
                            modified_sentence = replace_last_word(original_sentence, new_word)
                            self.delete(0, tk.END)
                            self.insert(0, modified_sentence)
                            return "break"
                            break
                if self.cmdele[0] == "screenshot":
                    for possible in self.completions_2[2]:
                        if self.cmdele[1] in possible and self.cmdele[1] != possible:
                            original_sentence = self.var.get()
                            new_word = possible
                            # print(possible)
                            modified_sentence = replace_last_word(original_sentence, new_word)

                            self.delete(0, tk.END)
                            self.insert(0, modified_sentence)
                            return "break"
                            break
                        elif self.cmdele[1] == possible:
                            try:
                                new_word = self.completions_2[2][self._list(self.completions_2[2], possible) + 1]
                            except:
                                new_word = self.completions_2[2][0]
                            original_sentence = self.var.get()
                            modified_sentence = replace_last_word(original_sentence, new_word)
                            self.delete(0, tk.END)
                            self.insert(0, modified_sentence)
                            return "break"
                            break
                if self.cmdele[0] == "debug":
                    for possible in self.completions_2[4]:
                        if self.cmdele[1] in possible and self.cmdele[1] != possible:
                            original_sentence = self.var.get()
                            new_word = possible
                            # print(possible)
                            modified_sentence = replace_last_word(original_sentence, new_word)

                            self.delete(0, tk.END)
                            self.insert(0, modified_sentence)
                            return "break"
                            break
                        elif self.cmdele[1] == possible:
                            try:
                                new_word = self.completions_2[4][self._list(self.completions_2[4], possible) + 1]
                            except:
                                new_word = self.completions_2[4][0]
                            original_sentence = self.var.get()
                            modified_sentence = replace_last_word(original_sentence, new_word)
                            self.delete(0, tk.END)
                            self.insert(0, modified_sentence)
                            return "break"
                            break
            elif len(self.cmdele) == 3:
                if self.cmdele[0] == "open":
                    if self.cmdele[1] == 'app':
                        for possible in self.completions_3[0]:
                            if self.cmdele[2] in possible and self.cmdele[2] != possible:
                                original_sentence = self.var.get()
                                new_word = possible
                                # print(possible)
                                modified_sentence = replace_last_word(original_sentence, new_word)

                                self.delete(0, tk.END)
                                self.insert(0, modified_sentence)
                                return "break"
                                break
                            elif self.cmdele[2] == possible:
                                try:
                                    new_word = self.completions_3[0][self._list(self.completions_3[0], possible) + 1]
                                except:
                                    new_word = self.completions_3[0][0]
                                original_sentence = self.var.get()
                                modified_sentence = replace_last_word(original_sentence, new_word)
                                self.delete(0, tk.END)
                                self.insert(0, modified_sentence)
                                return "break"
                                break
                    if self.cmdele[1] == 'web':
                        for possible in self.completions_3[1]:
                            if self.cmdele[2] in possible and self.cmdele[2] != possible:
                                original_sentence = self.var.get()
                                new_word = possible
                                # print(possible)
                                modified_sentence = replace_last_word(original_sentence, new_word)

                                self.delete(0, tk.END)
                                self.insert(0, modified_sentence)
                                return "break"
                                break
                            elif self.cmdele[2] == possible:
                                try:
                                    new_word = self.completions_3[1][self._list(self.completions_3[1], possible) + 1]
                                except:
                                    new_word = self.completions_3[1][0]
                                original_sentence = self.var.get()
                                modified_sentence = replace_last_word(original_sentence, new_word)
                                self.delete(0, tk.END)
                                self.insert(0, modified_sentence)
                                return "break"
                                break


def on_key_release(event):
    # 获取Entry控件的当前文本内容
    text = event.widget.get()

    try:
        cmd = text.split("/")[1].split(" ")
    except:
        if text.split("<debug>:")[0] == '':
            entry_widget.config(fg='green')
            cmd = [""]
        else:
            entry_widget.config(fg='red')
            cmd = [""]

    if text == "":
        tk.Entry.insert(entry_widget, 0, initial_text)
        entry_widget.config(fg='black')
    if cmd[len(cmd) - 1] == "":
        entry_widget.config(fg='red')

    if len(cmd) == 1:
        if cmd[0] in completions_1:
            entry_widget.config(fg='green')
        else:
            if text.split("<debug>:")[0] == '':
                entry_widget.config(fg='green')

            else:
                entry_widget.config(fg='red')

    elif len(cmd) == 2:
        try:
            index = completions_1.index(cmd[0])
            if cmd[1] in completions_2[index]:
                entry_widget.config(fg='brown')
            else:
                entry_widget.config(fg='red')
        except:
            entry_widget.config(fg='red')
    elif len(cmd) == 3:
        try:
            index1 = completions_1.index(cmd[0])
            index2 = completions_2[index1].index(cmd[1])
            if cmd[2] in completions_3[index2]:
                entry_widget.config(fg='purple')
            else:
                entry_widget.config(fg='red')
        except:
            entry_widget.config(fg='red')




def on_key_press(event):
    if event.keysym == "Escape":
        root.withdraw()
        hotkey_window.deiconify()
    try:
        if event.char == '\r' or event.keysym == 'Return':
            if entry_widget.get().split("<debug>:")[0] == '':
                entry_widget.delete(0, tk.END)
            elif entry_widget.get().split("<Error>:")[0] == '':
                entry_widget.delete(0, tk.END)
            elif entry_widget.get() == '':
                entry_widget.config(fg='black')
            else:
                cmd = entry_widget.get().split(">/")[1]
                cmds = cmd.split(" ")
                print(cmds)

                if cmds[0] == "quit":
                    root.destroy()
                if cmds[0] == 'open':
                    if cmds[1] == 'app':
                        if cmds[2] == 'add':
                            text = ''
                            select_ = []

                            def copy():

                                text_to_copy = app_path[select_[0]]
                                pyperclip.copy(text_to_copy)

                            def delete():
                                selected_index = listbox.curselection()
                                if selected_index:
                                    # 删除选中的项
                                    listbox.delete(selected_index[0])
                                    del app[app.index(select_[0])]
                                    app_path.pop(select_[0])
                                    editmenu.entryconfig(0, state='disabled')
                                    editmenu.entryconfig(1, state='disabled')


                            def select_directory():
                                file_path = filedialog.askopenfilename(
                                    title=Language.select_directory_title,
                                    filetypes=[(Language.filetypes_1, "*.exe"), (Language.filetypes_2, "*.*")]
                                )
                                appname = file_path.split("/")[len(file_path.split("/")) - 1]
                                app.append(appname)
                                app_path[appname] = file_path
                                list()

                            def on_select(event):
                                editmenu.entryconfig(0, state='normal')
                                editmenu.entryconfig(1, state='normal')

                                select_.clear()
                                # 获取被选中的项的索引
                                selected_index = listbox.curselection()
                                # 获取被选中的项的值
                                selected_item = listbox.get(selected_index)
                                select_.append(selected_item)

                            def apply():
                                with open(appnamedata_path, 'w') as file:
                                    # 将列表转换为字符串并写入文件
                                    # 使用join方法将列表元素连接成一个字符串，每个元素之间用换行符分隔
                                    file.write('\n'.join(app))
                                with open(apppathdata_path, 'w', encoding='utf-8') as file:
                                    # 将字典转换为JSON格式的字符串
                                    json_str = json.dumps(app_path, ensure_ascii=False, indent=4)
                                    # 将字符串写入文件
                                    file.write(json_str)
                                lable.config(text=Language.save_l)

                            def cancel():
                                addapp.destroy()

                            addapp = tk.Tk()
                            addapp.geometry("300x300")
                            addapp.title("add_app")
                            # 创建菜单栏
                            menubar = tk.Menu(addapp)

                            # 创建文件菜单
                            filemenu = tk.Menu(menubar, tearoff=0)
                            filemenu.add_command(label=Language.open_l, command=select_directory)
                            filemenu.add_command(label=Language.save_, command=apply)
                            filemenu.add_separator()  # 添加分隔线
                            filemenu.add_command(label=Language.quit_, command=cancel)

                            # 创建编辑菜单
                            editmenu = tk.Menu(menubar, tearoff=0)
                            editmenu.add_command(label=Language.del_, command=delete, state="disabled")
                            editmenu.add_command(label=Language.copy_path, command=copy, state='disabled')

                            # 添加菜单到菜单栏
                            menubar.add_cascade(label=Language.file_, menu=filemenu)
                            menubar.add_cascade(label=Language.edit, menu=editmenu)

                            # 显示菜单
                            addapp.config(menu=menubar)
                            listbox = tk.Listbox(addapp)

                            # 插入一些项目到Listbox中
                            def list():
                                listbox.delete(0, tk.END)
                                pass
                                for i in app:
                                    if i == 'add':
                                        continue

                                    listbox.insert(tk.END, i)

                            list()

                            # 当选中一个项时调用on_select函数
                            listbox.bind('<<ListboxSelect>>', on_select)
                            listbox.pack(expand=True, fill='both')
                            lable = tk.Label(addapp, text=text)
                            lable.pack()

                        if cmds[2] in app and cmds[2] != 'add':
                            # 要打开的exe文件的路径
                            exe_path = app_path[cmds[2]]

                            # 使用subprocess.Popen打开exe程序
                            # 不捕获输出，让程序在后台运行
                            process = subprocess.Popen(exe_path)

                            # 此时，应用程序已经开始运行，Python脚本会继续执行
                            # 如果你需要确保应用程序已经启动，可以稍微等待一下
                            # 例如，使用time.sleep(seconds)来等待几秒钟
                            import time
                            time.sleep(1)  # 等待1秒以确保应用程序有时间启动

                            # 脚本继续执行其他任务...
                            # 注意：此时应用程序仍然在后台运行，Python脚本不会等待它结束
                    elif cmds[1] == 'web':
                        if cmds[2] == 'add':
                            text = ''
                            select_ = []

                            def copy():

                                text_to_copy = web_path[select_[0]]
                                pyperclip.copy(text_to_copy)

                            def delete():
                                selected_index = listbox.curselection()
                                if selected_index:
                                    # 删除选中的项
                                    listbox.delete(selected_index[0])
                                    del app[app.index(select_[0])]
                                    web_path.pop(select_[0])
                                    editmenu.entryconfig(0, state='disabled')
                                    editmenu.entryconfig(1, state='disabled')


                            def select_directory():
                                entry = tk.Tk()
                                entry_ = tk.Entry(entry, font=font_style)
                                entry_.pack()

                                def get():
                                    file_path = entry_.get()
                                    print(file_path)
                                    webname = file_path.split("/")[2]
                                    web.append(webname)
                                    web_path[webname] = file_path
                                    list_()
                                    entry.destroy()

                                button = tk.Button(entry, command=get, text=Language.add)
                                button.pack()

                            def on_select(event):
                                editmenu.entryconfig(0, state='normal')
                                editmenu.entryconfig(1, state='normal')

                                select_.clear()
                                # 获取被选中的项的索引
                                selected_index = listbox.curselection()
                                # 获取被选中的项的值
                                selected_item = listbox.get(selected_index)
                                select_.append(selected_item)

                            def apply():
                                with open(webnamedata_path, 'w') as file:
                                    # 将列表转换为字符串并写入文件
                                    # 使用join方法将列表元素连接成一个字符串，每个元素之间用换行符分隔
                                    file.write('\n'.join(web))
                                with open(webpathdata_path, 'w', encoding='utf-8') as file:
                                    # 将字典转换为JSON格式的字符串
                                    json_str = json.dumps(web_path, ensure_ascii=False, indent=4)
                                    # 将字符串写入文件
                                    file.write(json_str)
                                lable.config(text=Language.save_l)

                            def cancel():
                                webapp.destroy()

                            webapp = tk.Tk()
                            webapp.geometry("300x300")
                            webapp.title("web_app")
                            # 创建菜单栏
                            menubar = tk.Menu(webapp)

                            # 创建文件菜单
                            filemenu = tk.Menu(menubar, tearoff=0)
                            filemenu.add_command(label=Language.open_l, command=select_directory)
                            filemenu.add_command(label=Language.save_, command=apply)
                            filemenu.add_separator()  # 添加分隔线
                            filemenu.add_command(label=Language.quit_, command=cancel)

                            # 创建编辑菜单
                            editmenu = tk.Menu(menubar, tearoff=0)
                            editmenu.add_command(label=Language.del_, command=delete, state="disabled")
                            editmenu.add_command(label=Language.copy_web_path, command=copy, state='disabled')

                            # 添加菜单到菜单栏
                            menubar.add_cascade(label=Language.file_, menu=filemenu)
                            menubar.add_cascade(label=Language.edit, menu=editmenu)

                            # 显示菜单
                            webapp.config(menu=menubar)
                            listbox = tk.Listbox(webapp)

                            # 插入一些项目到Listbox中
                            def list_():
                                listbox.delete(0, tk.END)
                                pass
                                for i in web:
                                    if i == 'add':
                                        continue

                                    listbox.insert(tk.END, i)

                            list_()

                            # 当选中一个项时调用on_select函数
                            listbox.bind('<<ListboxSelect>>', on_select)
                            listbox.pack(expand=True, fill='both')
                            lable = tk.Label(webapp, text=text)
                            lable.pack()

                        if cmds[2] in web and cmds[2] != 'add':
                            import webbrowser
                            webbrowser.open(web_path[cmds[2]])
                if cmds[0] == "screenshot":
                    if cmds[1] == 'full':
                        # 截取整个屏幕的截图

                        namenum = random.randint(-999999999999, 999999999999)
                        # 截取整个屏幕
                        screenshot = pyautogui.screenshot()

                        # 保存截图到文件
                        global screenshot_save_path
                        path = screenshot_save_path.replace("/","\\")

                        subprocess.Popen(f'explorer /select,"{path}"')
                        print(path)

                if cmds[0] == 'settings':
                    def on_slider_change(value):
                        with open(options, 'w', encoding='utf-8') as file:
                            _options['slider_value'] = str(value)
                            # 将字典转换为JSON格式的字符串
                            json_str = json.dumps(_options, ensure_ascii=False, indent=4)
                            # 将字符串写入文件
                            file.write(json_str)
                        root.attributes('-alpha', float(_options['slider_value']))

                    set = tk.Tk()
                    set.geometry("300x400")
                    set.title("settings")
                    set.resizable(False, False)

                    lable_0 = tk.Label(set, text=Language.screenshot_settings)
                    lable_0.pack()
                    lable_0.place(x=0, y=0)
                    screenshot_path = tk.Label(set, text="path:" + screenshot_save_path, fg="green")
                    screenshot_path.pack()
                    screenshot_path.place(x=10, y=20)

                    def choose_color():
                        # 使用colorchooser模块的askcolor函数打开一个颜色选择器对话框
                        # 返回选定的颜色值，格式为(RGB元组, #RRGGBB字符串)
                        color = colorchooser.askcolor()
                        if color is not None:
                            # 获取选定的颜色的RGB元组
                            rgb = color[0]
                            # 获取选定的颜色的#RRGGBB字符串表示
                            hex_color = color[1]
                            global bg
                            bg = hex_color
                            entry_widget.config(bg=hex_color)
                            color_button.config(bg=hex_color)
                            with open(options, 'w', encoding='utf-8') as file:
                                _options['bg'] = hex_color
                                # 将字典转换为JSON格式的字符串
                                json_str = json.dumps(_options, ensure_ascii=False, indent=4)
                                # 将字符串写入文件
                                file.write(json_str)

                    def select_directory():
                        directory = filedialog.askdirectory()
                        global screenshot_save_path
                        screenshot_save_path = directory
                        screenshot_path.config(text=screenshot_save_path)

                    def save():
                        with open(options, 'w') as file:
                            _options['screenshot_save_path'] = screenshot_save_path

                            # 将字典转换为JSON格式的字符串
                            json_str = json.dumps(_options, ensure_ascii=False, indent=4)
                            # 将字符串写入文件
                            file.write(json_str)

                    def on_checkbox_change():
                        if _options['open_path'] == 'false':
                            _options['open_path'] = 'true'
                        else:
                            _options['open_path'] = 'false'
                        with open(options, 'w') as file:
                            open_ = json.dumps(_options, ensure_ascii=False, indent=4)
                            # 将字符串写入文件
                            file.write(open_)
                        choose_v.config(text=Language.open_folder_s + _options['open_path'])
                    def set_language():
                        if _options['language'] == 'chinese':
                            _options['language'] = 'english'
                            with open(options, 'w') as file:
                                open_ = json.dumps(_options, ensure_ascii=False, indent=4)
                                # 将字符串写入文件
                                file.write(open_)

                        else:
                            _options['language'] = 'chinese'
                            with open(options, 'w') as file:
                                open_ = json.dumps(_options, ensure_ascii=False, indent=4)
                                # 将字符串写入文件
                                file.write(open_)
                        # 显示信息提示窗口
                        messagebox.showinfo("Prompt", "Need to restart to reset language")
                        quit()


                    open_button = tk.Button(set, text=Language.screenshot_path_l, command=select_directory)
                    open_button.pack()
                    open_button.place(x=10, y=40)

                    save_button = tk.Button(set, text=Language.save_, command=save)
                    save_button.pack()
                    save_button.place(x=150, y=40)
                    lable_1 = tk.Label(set,
                                       text="---------------------------------------------------------------------")
                    lable_1.pack()
                    lable_1.place(x=0, y=110)
                    lable_2 = tk.Label(set, text=Language.theme_l)
                    lable_2.pack()
                    lable_2.place(x=0, y=130)
                    # 创建一个按钮，点击时调用choose_color函数
                    color_button = tk.Button(set, text=Language.choose_color, command=choose_color, bg=bg)
                    color_button.pack()
                    color_button.place(x=10, y=155)

                    choose_v = tk.Button(set, text=Language.open_folder_s + _options['open_path'],
                                         command=on_checkbox_change)
                    choose_v.pack()
                    choose_v.place(x=10, y=70)
                    apply_button = tk.Button(set, text=Language.apply_l, command=set.destroy)
                    apply_button.pack()
                    apply_button.place(x=250, y=350)
                    lable_2 = tk.Label(set,
                                       text="---------------------------------------------------------------------")
                    lable_2.pack()
                    lable_2.place(x=0, y=270)
                    lable_language = tk.Label(set,
                                       text=Language.language_l)
                    lable_language.pack()
                    lable_language.place(x=0, y=290)
                    language_button = tk.Button(set, text=Language.language, command=set_language)
                    language_button.pack()
                    language_button.place(x=10, y=320)
                    slider = tk.Scale(set, from_=0.1, to=1, resolution=0.01, orient=tk.HORIZONTAL,length=200,
                                      label=Language.slider_l,
                                      command=on_slider_change)
                    slider.pack()
                    slider.place(x=9, y=200)
                    slider.set(_options['slider_value'])

                entry_widget.delete(0, tk.END)

                if cmds[0] == 'debug':
                    if cmds[1] in debug:
                        text = ''
                        if cmds[1] == debug[0]:
                            text = "<debug>: " + debug[0] + ":" + str(app)

                        elif cmds[1] == debug[1]:
                            text = "<debug>: " + debug[1] + ":" + str(apppath_1)

                        elif cmds[1] == debug[2]:
                            text = "<debug>: " + debug[2] + ":" + str(_options)

                        elif cmds[1] == debug[3]:
                            text = "<debug>: " + debug[3] + ":" + str(web)

                        elif cmds[1] == debug[4]:
                            text = str(webpath_1)
                        entry_widget.insert(tk.END, text)
                        entry_widget.config(fg='green')
                        entry_widget.config(fg='green')
    except:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(tk.END, '<Error>: '+'Please check if your command is correct.')


root = tk.Tk()
root.wm_attributes("-topmost", True)

root.overrideredirect(True)
root.geometry("100000x20+2+1027")
# 创建Entry控件
font_style = tkfont.Font(family='Minecraft AE', size=12, weight='normal')
entry_widget = AutoCompleteEntry(root, font=font_style ,bg = bg, completions_1=completions_1,
                                 completions_2=completions_2, completions_3=completions_3)
entry_widget.insert(0, initial_text)
entry_widget.pack(fill="x", expand=True)
# 绑定<KeyRelease>事件到on_key_release函数
entry_widget.bind('<KeyRelease>', on_key_release)
root.bind("<Key>", on_key_press)  # 绑定键盘事件到处理函数


def on_ctrl_slash():
    # 显示root窗口
    if root.winfo_exists():
        root.deiconify()  # 显示root窗口
        hotkey_window.withdraw()


root.withdraw()  # 初始时隐藏root窗口
root.attributes('-alpha', float(_options['slider_value']))
hotkey_window = NoBorderWindow()
hotkey_window.geometry("35x30+1850+1000")
hotkey_window.attributes('-alpha', 10)  # 设置窗口透明度为完全透明
hotkey_window.wm_attributes("-topmost", True)  # 设置窗口位置为屏幕左上角
button = tk.Button(hotkey_window, text="/", command=on_ctrl_slash,font=font_style,fg='purple')  # 创建一个按钮控件，并设置点击时的回调函数
button.pack()  # 将按钮添加到窗口中
button.place(x=0, y=0)
hotkey_window.focus_force()  # 强制设置焦点到窗口
hotkey_window.focus_set()  # 设置窗口为当前焦点窗口
root.mainloop()




