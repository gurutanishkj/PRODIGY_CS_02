# PRODIGY_CS_02

Pixel Manipulation for Image Encryption - Prodigy InfoTech Cyber Security Internship Task 02

## Description

A Python-based Image Encryption and Decryption Tool that uses pixel manipulation techniques to secure images. The application provides a graphical user interface (GUI) built using Tkinter and allows users to encrypt and decrypt images using a numeric key.

## Features

* Encrypts images using a user-defined key.
* Decrypts encrypted images using the same key.
* Supports PNG, JPG, JPEG, and BMP image formats.
* Displays image previews within the application.
* User-friendly graphical interface.
* Preserves image dimensions during processing.

## How It Works

* The user selects an image using the **Browse Image** button.
* A numeric key is entered for encryption or decryption.
* During encryption, the key value is added to each RGB pixel component.
* During decryption, the same key value is subtracted from each RGB pixel component.
* The processed image can be saved and previewed within the application.

## Code Explanation

* `Image.open()` loads the selected image.
* `convert("RGB")` converts the image into RGB format.
* `pixels[x, y]` accesses individual pixel values.
* `(value + key) % 256` encrypts pixel values.
* `(value - key) % 256` decrypts pixel values.
* `ImageTk.PhotoImage()` displays image previews in the GUI.

## Technologies Used

* Python 3
* Tkinter
* Pillow (PIL)

## Requirements

Install Pillow before running the program:

```bash
pip install pillow
```

## How to Run

```bash
python image_encryption.py
```

## Example

### Input

Select Image: nissan_gtr.jpg

Enter Key: 26

Click: Encrypt Image

### Output

Encrypted image is generated and saved.

### Decryption

Select Encrypted Image

Enter Key: 26

Click: Decrypt Image

### Result

Original image is successfully restored.

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
