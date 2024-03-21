import tkinter as tk
from PIL import Image, ImageTk
import os
import time

root = None

def install_libraries():
    os.system("pip install requests")
    os.system("pip install subprocess")
    os.system("pip install bs4")

def create_request_files():
    current_directory = os.getcwd()

    # request.txt dosyasını oluştur
    request_file_path = os.path.join(current_directory, 'log', 'request.txt')
    with open(request_file_path, 'w') as file:
        file.write(".")

    # subprocess.txt dosyasını oluştur
    request_file_path = os.path.join(current_directory, 'log', 'subprocess.txt')
    with open(request_file_path, 'w') as file:
        file.write(".")

    # bs4.txt dosyasını oluştur
    request_file_path = os.path.join(current_directory, 'log', 'bs4.txt')
    with open(request_file_path, 'w') as file:
        file.write(".")

def clear_screen():
    # Ekranı temizle
    os.system("clear")

def setup_libraries():
    install_libraries()
    create_request_files()
    clear_screen()
    show_output()
    root.update()  # Pencereyi güncelle
    time.sleep(1)
    show_output2()
    root.update()  # Pencereyi güncelle
    time.sleep(1)
    setup_completed()

def show_output():
    # Ekranın alt kısmından başlayarak çıktıları göster
    output_text = "Library İnstalled✓" 

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Arial", 15), fg="red",bg="white")
    output_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    root.update()  # Pencereyi güncelle
    time.sleep(1)
    
def show_output2():
    output_text = "Codes İnstalled✓" 

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Arial", 15), fg="red",bg="white")
    output_label.place(relx=1.0, rely=0.9, anchor=tk.CENTER)
    root.update()  # Pencereyi güncelle
    time.sleep(1)

def setup_completed():
    # Yeni bir pencere oluştur ve "Setup Completed" yazısını göster
    setup_window = tk.Toplevel(root)
    setup_window.title("Setup Completed")

    # Pencere boyutunu ayarla
    window_width = 600
    window_height = 400
    setup_window.geometry("%dx%d" % (window_width, window_height))
    setup_window.resizable(False, False)  # Pencerenin boyutunu değiştiremezsiniz

    # Pencere arka plan rengini beyaz yap
    setup_window.configure(bg="white")

    # "Setup Completed" yazısını göster
    setup_label = tk.Label(setup_window, text="Setup Completed", font=("Helvetica", 24, "bold"), fg="green", bg="white")
    setup_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def create_window():
    global root
    # Ana pencere oluştur
    root = tk.Tk()
    root.title("BloodFire")

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
   
