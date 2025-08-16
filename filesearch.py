import os
import threading
import tkinter as tk
from tkinter import messagebox, filedialog

# 搜索软件的函数（异步）
def search_software(name, root_dir, callback, progress_callback):
    def search():
        try:
            for entry in os.scandir(root_dir):
                if entry.is_dir():
                    progress_callback(entry.path)  # 更新搜索进度
                    search_software(name, entry.path, callback, progress_callback)
                elif entry.is_file() and entry.name.lower().endswith('.exe') and name.lower() in entry.name.lower():
                    callback(entry.path)
        except PermissionError:
            pass  # 忽略无权限访问的目录

    thread = threading.Thread(target=search)
    thread.start()

# GUI 界面
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("软件搜索工具")

        # 输入框
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # 选择搜索目录按钮
        self.select_dir_button = tk.Button(root, text="选择搜索目录", command=self.select_directory)
        self.select_dir_button.pack(side=tk.LEFT, padx=10)

        # 搜索按钮
        self.search_button = tk.Button(root, text="搜索", command=self.search)
        self.search_button.pack(side=tk.LEFT, padx=10)

        # 搜索进度标签
        self.progress_label = tk.Label(root, text="搜索进度：")
        self.progress_label.pack(pady=5)

        # 结果列表
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # 打开按钮
        self.open_button = tk.Button(root, text="打开", command=self.open_software)
        self.open_button.pack(side=tk.LEFT, padx=10)

        self.found_paths = []  # 存储搜索到的软件路径
        self.search_root = 'C:\\'  # 默认搜索根目录

    def select_directory(self):
        self.search_root = filedialog.askdirectory(initialdir=self.search_root)
        if self.search_root:
            messagebox.showinfo("提示", f"已选择搜索目录：{self.search_root}")

    def search(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showerror("错误", "请输入软件名称")
            return

        # 清空之前的搜索结果
        self.listbox.delete(0, tk.END)
        self.found_paths = []

        # 定义回调函数
        def callback(path):
            self.found_paths.append(path)
            self.listbox.insert(tk.END, path)

        def progress_callback(current_dir):
            self.progress_label.config(text=f"搜索进度：{current_dir}")

        # 开始异步搜索
        self.search_button.config(state="disabled")  # 禁用按钮防止重复点击
        search_software(name, self.search_root, callback, progress_callback)

        # 搜索完成后恢复按钮并提示
        self.root.after(1000, lambda: self.search_button.config(state="normal"))
        self.root.after(1000, lambda: messagebox.showinfo("提示", "搜索完成"))

    def open_software(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("错误", "请先选择一个软件")
            return

        path = self.found_paths[selected[0]]
        try:
            os.startfile(path)  # 打开选中的软件
        except Exception as e:
            messagebox.showerror("错误", f"打开软件失败：{e}")

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
