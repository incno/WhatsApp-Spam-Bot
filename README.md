# WhatsApp-Spam-Bot

Python code for a WhatsApp spam bot: https://github.com/Akshayjyoti/WhatsApp-Spam-Bot/blob/main/whatsapp.py  
Version 2.0  
Testing date: September 4, 2021

### ✅ Updated by: Fatony Ahmad Fauzi

### 🔄 Updated version: 2.01

### 🧪 Latest testing: April 14, 2025

---

## 🛠️ Changes & Improvements by Fatony Ahmad Fauzi:

- Migrated to latest **Selenium 4+** standards:
  - Replaced deprecated `find_element_by_*` with `find_element(By.*, ...)`.
- Updated XPath for:
  - **Message box** to accurately avoid search bar and target the correct chat input field.
  - **Send button** to match modern WhatsApp Web structure (`aria-label="Kirim"` or `"Send"`).
- Added handling for:
  - **Language variation** (`Kirim` for Indonesian, `Send` for English).
- Improved error handling for element detection (chat not found, message box not found, etc).
- Added flexible input box detection to adapt with future DOM changes (`_ak1r` container).
- Compatible with latest **ChromeDriver v135+** and WhatsApp Web UI updates.
- Optional **bot prompt** feature retained with option to disable.
- Added compatibility for both English and Indonesian UI.
- Removed unused import (`datetime`) if not in use.

---

## 🧪 Working Procedure:

1. Enter the name of user or group.
2. Enter your message.
3. Enter the number of times the message is to be sent.
4. Enter the interval (in seconds) between messages.
5. Optional bot prompt.
6. After pressing 'Enter', the bot will open the specific chat and start sending messages.

---

## ⚠️ Notes:

- Maximize the Chrome window as soon as it opens.
- Ignore warnings while entering name of user or group.
- Name of user or group must be entered **correctly (case sensitive)**.
- If elements cannot be found, use **Developer Tools (F12)** to inspect updated structure.

---

## ⚠️ Disclaimer:

This tool is for **educational** and **personal testing purposes only**. Do not use it for spamming or violating WhatsApp policies. Your account can be banned for abuse.
