# PRODIGY_CS_02
# Pixel Manipulation for Image Encryption

## Prodigy InfoTech Cyber Security Internship – Task 02

### Description

This project is a simple Image Encryption and Decryption Tool developed using Python. The application uses pixel manipulation techniques to encrypt and decrypt images by modifying RGB pixel values using a user-defined key.

A graphical user interface (GUI) built with Tkinter allows users to select images, enter an encryption key, and perform encryption or decryption operations easily.

---

## Features

- Browse and select image files.
- Encrypt images using a numeric key.
- Decrypt encrypted images using the same key.
- Preview selected and processed images.
- User-friendly graphical interface.
- Supports PNG, JPG, JPEG, and BMP image formats.

---

## Technologies Used

- Python 3
- Tkinter
- Pillow (PIL)

---

## How It Works

### Encryption

For every pixel in the image:

```python
(r + key) % 256
(g + key) % 256
(b + key) % 256
```

The key value is added to each RGB component.

### Decryption

For every pixel in the image:

```python
(r - key) % 256
(g - key) % 256
(b - key) % 256
```

The same key is subtracted to restore the original image.

### Example

Original Pixel:

```text
(100, 150, 200)
```

Key:

```text
26
```

Encrypted Pixel:

```text
(126, 176, 226)
```

Decrypted Pixel:

```text
(100, 150, 200)
```

---

## Requirements

Install the Pillow library before running the project:

```bash
pip install pillow
```

---

## How to Run

Save the code as:

```text
image_encryption.py
```

Run the program using:

```bash
python image_encryption.py
```

or

```bash
py image_encryption.py
```

---

## Project Workflow

1. Launch the application.
2. Click **Browse Image**.
3. Select an image file.
4. Enter a numeric key.
5. Click **Encrypt Image**.
6. Save the encrypted image.
7. Open the encrypted image.
8. Enter the same key.
9. Click **Decrypt Image**.
10. Save the restored image.

---

## Sample Output

### Original Image

- User selects an image using the Browse button.
- The selected image is displayed in the preview area.

### Encrypted Image

- Image pixels are modified using the key.
- The encrypted image is saved and previewed.

### Decrypted Image

- The original image is restored using the same key.
- The decrypted image is displayed in the preview area.

---

## Learning Outcomes

- Image Processing Basics
- Pixel Manipulation Techniques
- Encryption and Decryption Concepts
- GUI Development using Tkinter
- Working with Images using Pillow

---

## Internship Details

**Company:** Prodigy InfoTech

**Domain:** Cyber Security

**Task:** Task 02 – Pixel Manipulation for Image Encryption

---
