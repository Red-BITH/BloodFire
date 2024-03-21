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
    time.sleep(1)
    show_output2()

def show_output():
    # Ekranın alt kısmından başlayarak çıktıları göster
    output_text = "Library Installed✓" 

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Arial", 15), fg="red",bg="white")
    output_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    time.sleep(1)
    
def show_output2():
    output_text = "Codes Installed✓" 

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Arial", 15), fg="red",bg="white")
    output_label.place(relx=1.0, rely=0.9, anchor=tk.CENTER)

def create_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("BloodFire")
    new_window.geometry("600x400")
    new_window.configure(bg="white")

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
    label1 = tk.Label(new_window, image=photo1, bg="white")
    label1.grid(row=0, column=0, padx=10, pady=10)

    # Merkez üstte kırmızı yazıyı yerleştir
    label3 = tk.Label(new_window, text="BLOODFIRE", font=("Helvetica", 24, "bold"), fg="red", bg="white")
    label3.grid(row=0, column=1, padx=10, pady=10)

    # Üst sağda ikinci resmi yerleştir
    label2 = tk.Label(new_window, image=photo2, bg="white")
    label2.grid(row=0, column=2, padx=10, pady=10)

    # Setup completed yazısı
    setup_completed_label = tk.Label(new_window, text="Setup completed", font=("Arial", 15), fg="green", bg="white")
    setup_completed_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def create_window():
    global root
    # Ana pencere oluştur
    root = tk.Tk()
    root.title("BloodFire")

    # Pencere boyutunu ayarla
    window_width = 600
    window_height = 400
    root.geometry("%dx%d" % (window_width, window_height))
    root.resizable(False,
