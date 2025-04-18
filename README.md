# WhatsApp-Spam-Bot

Python code for a WhatsApp automation tool: [whatsapp.py](https://github.com/Akshayjyoti/WhatsApp-Spam-Bot/blob/main/whatsapp.py)  
**Version**: 3.0  
**Latest Testing**: April 17, 2024  
**Maintainer**: Fatony Ahmad Fauzi

---

## 🚀 **Version 3.0 Updates**

### 🔄 **Core Improvements**

- **Clipboard Integration**:
  - Support **copy-paste messages with emojis** directly from clipboard (Ctrl+V/Cmd+V).
- **Enhanced Multi-OS Support**:
  - Auto-detect OS for shortcut keys (Windows: `Ctrl`, macOS: `Cmd`).
- **Dynamic Message Formatting**:
  - Optional timestamp (`3:13 AM`) appended automatically.
  - Bot status prompt (`<Status: X/Y>`) now includes real-time progress.
- **Stability Upgrades**:
  - Added `WebDriverWait` for robust element detection.
  - Improved error handling for network fluctuations.

### 🛠️ **Technical Updates**

- **Selenium 4.15+ Compatibility**:
  - Optimized XPath for WhatsApp Web's 2024 UI:
    - Message box: `//div[contains(@class, "_ak1r")]//div[@role="textbox"]`
    - Send button: `//button[.//span[@data-icon="send"]]`
- **ChromeDriver v140+ Support**:
  - Added auto-driver management via `webdriver_manager`.
- **Code Refactoring**:
  - Modularized functions for message sending and clipboard handling.

---

## 🧪 **Usage Guide**

1. **Prerequisites**:
   ```bash
   pip install selenium pyperclip webdriver-manager
   ```
2. **Run the Script**:
   ```bash
   python whatsapp.py
   ```
3. **Workflow**:

- Scan QR Code via WhatsApp Web.
- Input Parameters:
  - `User/Group Name`: **Case-sensitive** target chat name.
  - `Message Source`: Choose between **clipboard** (Y) or **manual input** (N).
  - `Count`: Number of messages (e.g., `10`).
  - `Interval`: Delay between messages in seconds (e.g., `1.5`).
  - `Bot Prompt`: Add status prefix (Y/N).

---

## ⚠️ Critical Notes

- **Chrome Window**: Maximize immediately after QR scan for element detection.
- **Clipboard Usage**: Copy text+emojis before running the script if using clipboard mode.
- **Rate Limits**: Avoid intervals < 1 second to prevent account restrictions.
- **Debugging**: Use **F12 Developer Tools** to inspect DOM changes.

---

## 📜 Disclaimer

This tool is for **educational purposes only**. Misuse (e.g., spamming) may violate WhatsApp's Terms of Service and result in account bans. Use responsibly.
