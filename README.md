# 🔐 Password Strength Check Lambda

A Python AWS Lambda–style function that validates password strength during user registration.  
It checks for password length, character diversity, and rejects common weak passwords (e.g., `password123`, `admin`, etc.).

---

## 🧩 Features
- ✅ Minimum length validation (8+ characters)
- 🔠 Requires uppercase and lowercase letters
- 🔢 Requires at least one number
- 💥 Requires at least one special character
- 🚫 Denies common weak passwords
- 📦 Simple AWS Lambda handler structure
- 🧪 Easily testable locally or as part of a backend flow

---

## 🧰 Usage

### 1️⃣ Run Locally
```bash
python password_check_lambda.py
