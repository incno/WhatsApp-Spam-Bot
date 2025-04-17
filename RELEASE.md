# Release Notes - WhatsApp-Spam-Bot v3.0

**Release Date**: April 17, 2024  
**Maintainer**: Fatony Ahmad Fauzi

---

## 🌟 **New Features**

| Feature                | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
| **Clipboard Support**  | Paste pre-copied messages (text+emojis) directly into WhatsApp Web.       |
| **OS-Aware Shortcuts** | Auto-switch between `Ctrl` (Windows/Linux) and `Cmd` (macOS) for pasting. |
| **Live Timestamp**     | Append current time (e.g., `3:13 AM`) to messages dynamically.            |

---

## 🐞 **Bug Fixes**

- Fixed `NoSuchElementException` for send button in multilingual interfaces.
- Resolved clipboard encoding issues with special characters and emojis (🌤✅).
- Removed redundant QR code scan prompts.

---

## ⚙️ **Optimizations**

- Reduced element detection latency using `Explicit Waits`.
- Streamlined message-loop logic for better performance.
- Updated error messages for clearer debugging.

---

## 📊 **Compatibility**

- **Selenium**: 4.15+
- **ChromeDriver**: v140+
- **Python**: 3.8+
- **OS**: Windows 10+, macOS Ventura+, Linux (Ubuntu 22.04+)

---

## 🔗 **Links**

- [GitHub Repository](https://github.com/Akshayjyoti/WhatsApp-Spam-Bot)
- [ChromeDriver Setup Guide](https://chromedriver.chromium.org/)
