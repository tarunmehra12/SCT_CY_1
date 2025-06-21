# 🔐 Caesar Cipher Tool

This is a simple Caesar Cipher encryption and decryption tool written in Python.  
It supports encryption, decryption, and brute-force decoding without knowing the shift key.

---

## 📌 Features

- ✅ Encrypt messages with a Caesar Cipher shift
- ✅ Decrypt messages using the known shift
- ✅ Brute force decoding (try all 25 shifts to break a message)

---

## 🧠 How It Works

The Caesar Cipher shifts each letter in the message by a fixed number.  
For example, with a shift of 3:

- A → D  
- B → E  
- C → F  
- ...
- Z → C (it wraps around)

If decrypting, the program simply reverses the shift.

---

## 💻 How to Use

Run the program in terminal or VS Code:

```bash
python caesar_cipher.py
