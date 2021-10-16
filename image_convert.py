#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @Time    : 2021-10-08 19:59
# @Author  : Eddie Shen
# @Email   : sheneddie@outlook.com
# @File    : image_convert.py
# @Software: PyCharm


import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from webptools import dwebp


class Webp2jpg(object):
    def __init__(self):
        self.webp_paths = []
        self.save_dir = ''

    def openfile(self):
        self.webp_paths = filedialog.askopenfilenames(
            filetypes=[('picture', '.webp')])
        label_1.config(text="第一个webp文件位置：" + self.webp_paths[0])

    def save_images_dir(self):
        self.save_dir = filedialog.askdirectory()
        label_2.config(text="保存文件夹位置：" + self.save_dir)

    def convert_webp_jpg(self):
        if len(self.webp_paths) == 0:
            messagebox.showerror('Error', '请选择正确的文件咩咩咩！')
        else:
            progress.config(maximum=len(self.webp_paths))
            for i, webp_path in enumerate(self.webp_paths):
                pic_name = os.path.split(webp_path)[-1].split(".")[0]
                jpg_name = pic_name + '.jpg'
                input_image = '"' + webp_path + '"'
                output_image = '"' + os.path.join(self.save_dir, jpg_name) + '"'
                dwebp(input_image=input_image, output_image=output_image,
                      option="-o", logging="-v")
                os.remove(webp_path)
                progress.config(value=i + 1)
                windows.update()
            messagebox.showinfo('Info', '转换完成么么么！')
            progress.config(value=0)

    def open_result(self):
        os.startfile(self.save_dir)


if __name__ == '__main__':
    # Tk windows.
    windows = tk.Tk()
    windows.update()
    windows.geometry('800x300')
    windows.title('兔兔的webp转jpg工具')
    # webp to jpg.
    webp = Webp2jpg()
    # Button & Label
    button_1 = tk.Button(windows, text="选择webp文件", command=webp.openfile)
    button_1.pack()
    label_1 = tk.Label(windows)
    label_1.pack()
    button_2 = tk.Button(windows,
                         text="选择保存文件夹", command=webp.save_images_dir)
    button_2.pack()
    label_2 = tk.Label(windows)
    label_2.pack()
    button_3 = tk.Button(windows,
                         text="转换", command=webp.convert_webp_jpg)
    button_3.pack()
    progress = ttk.Progressbar(windows, length=200)
    progress.pack()
    button_4 = tk.Button(windows, text="打开结果文件夹", command=webp.open_result)
    button_4.pack()

    tk.mainloop()
