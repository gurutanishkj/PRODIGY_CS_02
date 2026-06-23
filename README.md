# PRODIGY_CS_02

## Pixel Manipulation for Image Encryption

### Prodigy InfoTech Cyber Security Internship – Task 02

## Description

This project is a simple Image Encryption and Decryption Tool developed using Python. The application uses pixel manipulation techniques to encrypt and decrypt images by modifying RGB pixel values using a user-defined key.

A graphical user interface (GUI) built with Tkinter allows users to select images, enter an encryption key, and perform encryption or decryption operations easily.

## Features

* Encrypts images using a numeric key.
* Decrypts encrypted images using the same key.
* Supports PNG, JPG, JPEG, and BMP image formats.
* Displays image previews within the application.
* User-friendly graphical interface.
* Preserves image dimensions during processing.

## How It Works

* The user selects an image using the Browse Image button.
* A numeric key is entered for encryption or decryption.
* During encryption, the key value is added to each RGB pixel component.
* During decryption, the same key value is subtracted from each RGB pixel component.
* The processed image is saved and displayed in the preview section.

## Code Explanation

* `Image.open()` loads the selected image.
* `convert("RGB")` converts the image into RGB format.
* `pixels[x, y]` accesses individual pixel values.
* `(r + key) % 256`, `(g + key) % 256`, `(b + key) % 256` encrypt pixel values.
* `(r - key) % 256`, `(g - key) % 256`, `(b - key) % 256` decrypt pixel values.
* `ImageTk.PhotoImage()` displays image previews in the GUI.

## Technologies Used

* Python 3
* Tkinter
* Pillow (PIL)

## Requirements

Install Pillow before running the project:

```bash
pip install pillow
```

## How to Run

```bash
python Image_Encryption.py
```

## Example

### Input

Select Image: original image.png

Enter Key: 26

Click: Encrypt Image

### Output

Encrypted image is generated and saved successfully.

### Decryption

Select Image: encrypted image.png

Enter Key: 26

Click: Decrypt Image

### Result

The original image is restored successfully.

## Project Files

* Image_Encryption.py
* original image.png
* encrypted image.png
* decrypt image.png
* README.md

## Learning Outcomes

* Image Processing Basics
* Pixel Manipulation Techniques
* Encryption and Decryption Concepts
* GUI Development using Tkinter
* Working with Images using Pillow

## Internship Details

**Organization:** Prodigy InfoTech

**Domain:** Cyber Security

**Task:** Task 02 – Pixel Manipulation for Image Encryption
