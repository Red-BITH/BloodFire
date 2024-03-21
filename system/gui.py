import tkinter as tk
from PIL import Image, ImageTk
import os

import os

current_directory = os.getcwd()

request_file_path = os.path.join(current_directory, 'log', 'request.txt')

with open(request_file_path, 'w') as file:
    file.write(".")

os.system("pip install subprocess")


import os

current_directory = os.getcwd()

request_file_path = os.path.join(current_directory, 'log', 'subprocess.txt')

with open(request_file_path, 'w') as file:
    file.write(".")

os.system("pip install bs4")

import os

current_directory = os.getcwd()

request_file_path = os.path.join(current_directory, 'log', 'bs4.txt')
with open(request_file_path, 'w') as file:
    file.write(".")

def setup_libraries():
    show_output()

def show_output():
    # Ekranın alt kısmından başlayarak çıktıları göster
    output_text = "Output 1\nOutput 2\nOutput 3"  # İlgili çıktıları burada belirtin

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Helvetica", 12), bg="white")
    output_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def create_window():
    # Ana pencere oluştur
    root = tk.Tk()
    root.title("Orta Ölçülü Pencere")

    # Pencere boyutunu ayarla
    window_width = 600
    window_height = 400
    root.geometry("%dx%d" % (window_width, window_height))
    root.resizable(False, False)  # Pencerenin boyutunu değiştiremezsiniz

    # Pencere arka plan rengini beyaz yap
    root.configure(bg="white")

    # Resimleri yükle
    image_path1 = r"resim1.png"
    image_path2 = r"resim2.png"

    # Resimleri aç ve boyutlandır
    image1 = Image.open(image_path1)
    image1 = image1.resize((180, 200), Image.LANCZOS)  # Resmi yeniden boyutlandır
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open(image_path2)
    image2 = image2.resize((220, 200), Image.LANCZOS)  # Resmi yeniden boyutlandır
    photo2 = ImageTk.PhotoImage(image2)

    # Sol üst köşeye birinci resmi yerleştir
    label1 = tk.Label(root, image=photo1, bg="white")
    label1.grid(row=0, column=0, padx=10, pady=10)

    # Merkez üstte kırmızı yazıyı yerleştir
    label3 = tk.Label(root, text="BLOODFIRE", font=("Helvetica", 24, "bold"), fg="red", bg="white")
    label3.grid(row=0, column=1, padx=10, pady=10)

    # Üst sağda ikinci resmi yerleştir
    label2 = tk.Label(root, image=photo2, bg="white")
    label2.grid(row=0, column=2, padx=10, pady=10)

    # Butonu oluştur
    button_setup = tk.Button(root, text="Setup", font=("Helvetica", 16, "bold"), command=setup_libraries)
    button_setup.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()

create_window()

