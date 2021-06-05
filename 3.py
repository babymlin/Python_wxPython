# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:46:58 2021

@author: babym
"""
#0430作業2
#101_AI班林建名

import os
import sys

def print_fun():
    print(
        f"工作路徑：{base_path}\n"
        "\t(0) 離開程式\n",
        "\t(1) 列出檔案\n",
        "\t(2) 列出資料夾\n",
        "\t(3) 顯示檔案內容\n",
        "\t(4) 刪除檔案\n",
        "\t(5) 執行檔案\n",
        "\t(6) 進入資料夾\n",
        "\t(7) 刪除資料夾\n",
        "\t(8) 回上層資料夾\n"
        )

def get_file():
    index = 0
    for item in folder_content:
        if os.path.isfile(base_path + '\\' + item):
            print(f"{index}", f"{item}")
            index += 1

def get_file2():
    index, file_list = 0, list()
    for item in folder_content:
        if os.path.isfile(base_path + '\\' + item):
            file_list.append(f"{item}")
            print(f"{index}", f"{item}")
            index += 1
    inp = input("請輸入檔案索引：")
    return file_list[int(inp)]

def get_folder():
    index = 0
    for item in folder_content:
        if os.path.isdir(base_path + '\\' + item):
            print(f"{index}", f"{item}")
            index += 1

def get_folder2():
    index, folder_list = 0, list()
    for item in folder_content:
        if os.path.isdir(base_path + '\\' + item):
            folder_list.append(f"{item}")
            print(f"{index}", f"{item}")
            index += 1
    inp = input("請輸入資料夾索引：")
    return folder_list[int(inp)]

base_path = os.getcwd()
folder_content = os.listdir(base_path)
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print_fun()
    inp = input("操作：")
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        if inp =="0":
            break
        elif inp == "1":
            get_file()
        elif inp =="2":
            get_folder()
        elif inp =="3":
            with open(get_file2(), "r", encoding="utf-8") as fp:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("================檔案開始================")
                for line in fp:
                    print(line,end="")
                print("\n================檔案結束================")
        elif inp =="4":
            os.remove(get_file2())
        elif inp =="5":
            os.system(get_file2())
        elif inp =="6":
            base_path = f"{base_path}\\{get_folder2()}"
        elif inp =="7":
            os.rmdir(get_folder2())
        elif inp =="8":
            base_path = os.path.dirname(base_path)
        print()
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
