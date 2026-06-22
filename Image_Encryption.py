from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# -------- Encrypt / Decrypt Logic --------
def process_image(mode):
    if not file_path.get():
        messagebox.showerror("Error", "Please select an image first!")
        return
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number as key!")
        return

    img = Image.open(file_path.get()).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if mode == "encrypt":
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
            else:
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save Image As"
    )
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", f"Image {mode}ed and saved!")
        show_preview(save_path)

def browse_file():
    path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if path:
        file_path.set(path)
        show_preview(path)

def show_preview(path):
    img = Image.open(path)
    img.thumbnail((250, 250))
    photo = ImageTk.PhotoImage(img)
    preview_label.config(image=photo)
    preview_label.image = photo

# -------- GUI Setup --------
root = Tk()
root.title("Image Encryption Tool - PRODIGY_CS_02")
root.geometry("500x550")
root.config(bg="#1e1e2e")

Label(root, text="🔐 Image Encryption Tool", font=("Arial", 18, "bold"),
      bg="#1e1e2e", fg="#cdd6f4").pack(pady=15)

file_path = StringVar()

Button(root, text="📁 Browse Image", command=browse_file,
       bg="#89b4fa", fg="#1e1e2e", font=("Arial", 11, "bold"),
       width=20).pack(pady=5)

Label(root, text="Selected File:", bg="#1e1e2e", fg="#a6adc8").pack()
Label(root, textvariable=file_path, bg="#1e1e2e", fg="#cdd6f4",
      wraplength=400, font=("Arial", 8)).pack()

Label(root, text="Enter Key (Number):", bg="#1e1e2e",
      fg="#a6adc8", font=("Arial", 11)).pack(pady=10)
key_entry = Entry(root, font=("Arial", 12), width=10, justify="center")
key_entry.pack()

Button(root, text="🔒 Encrypt Image",
       command=lambda: process_image("encrypt"),
       bg="#a6e3a1", fg="#1e1e2e", font=("Arial", 11, "bold"),
       width=20).pack(pady=8)

Button(root, text="🔓 Decrypt Image",
       command=lambda: process_image("decrypt"),
       bg="#f38ba8", fg="#1e1e2e", font=("Arial", 11, "bold"),
       width=20).pack(pady=5)

preview_label = Label(root, bg="#1e1e2e")
preview_label.pack(pady=10)

root.mainloop()
