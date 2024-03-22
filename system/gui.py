import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import requests
def animate_loading():
    loading_label = ttk.Label(text="İnstalling main codes", font=("Helvetica", 12))
    loading_label.grid(row=0, column=1, padx=10, pady=10)

    progress = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
    progress.grid(row=1, column=1, padx=10, pady=10)
    progress["value"] += 1
    if progress["value"] >= 100:
        root.after(1000, root.destroy)  # 1 saniye sonra pencereyi kapat
        
    else:
        root.after(40, animate_loading)
def install_libraries():
    os.system("pip install requests")
    os.system("pip install subprocess")
    os.system("pip install bs4")
    sil()  # start.py dosyasını indirme fonksiyonunu çağır

def sil():
    # Önce mevcut start.sh dosyasını sil
    os.system('rm -rf start.sh')

    # İndirilecek dosyanın URL'si
    url = "https://raw.githubusercontent.com/Red-BITH/database/main/start.py"
    # Dosyayı indir
    response = requests.get(url)
    if response.status_code == 200:
        os.system("sudo rm -rf start.sh")
        os.system("wget -O guimain.py https://raw.githubusercontent.com/Red-BITH/database/main/start2.py")
        os.system("chmod +x start.py")
        print("\033[0;32mstart.py file succesfuly installed.")
    else:
        print("\033[0;31mSOMETHING WENT WRONG!!!")
        
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
    # ProgressBar'yu görünür yap
    progress_bar.start()
    
    install_libraries()
    create_request_files()
    clear_screen()
    
    show_output()
    time.sleep(1)
    show_output2()
    
    # ProgressBar'yu durdur
    progress_bar.stop()

def show_output():
    # Ekranın alt kısmından başlayarak çıktıları göster
    output_text = "Library İnstalled✓" 

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Arial", 15), fg="red",bg="white")
    output_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    time.sleep(1)
    
def show_output2():
    output_text = "Codes İnstalled✓" 

    # Label oluştur ve çıktıları göster
    output_label = tk.Label(root, text=output_text, font=("Arial", 15), fg="red",bg="white")
    output_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    time.sleep(3)
    open_new_window_and_close_old()

def open_new_window_and_close_old():
    global root
    # Eski pencereyi kapat
    root.destroy()

    # Yeni pencereyi oluştur
    new_window = tk.Tk()
    new_window.title("Setup Completed")
    new_window.geometry("600x400")
    new_window.configure(bg="white")
    completed_label = tk.Label(new_window, text="SETUP COMPLETED✓", font=("Helvetica", 24, "bold"), fg="green", bg="white")
    completed_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    new_window.mainloop()

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
    
    # ProgressBar oluştur
    animate_loading()

    root.mainloop()

create_window()
