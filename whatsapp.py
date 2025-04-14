import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Setup Chrome options (Headless mode jika ingin browser tidak muncul)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment jika ingin headless
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Buka WhatsApp Web
driver.get('https://web.whatsapp.com/')
print("\n\nPlease MAXIMIZE the WhatsApp window before proceeding...")
print("Scan the QR code, then press ENTER to continue...\n")
input('Press ENTER after scanning QR code...')

# Ambil data dari user
name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter how many times to send the message: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').strip().upper()

# Cari dan klik chat
try:
    user = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
    user.click()
except Exception as e:
    print(f"[!] Could not find the chat with '{name}'. Error: {e}")
    driver.quit()
    exit()

# Tunggu hingga kotak input pesan yang benar tersedia
time.sleep(3)

# Temukan kotak input pesan dalam container _ak1r
try:
    msg_box = driver.find_element(By.XPATH, '//div[contains(@class, "_ak1r")]//div[@role="textbox" and @data-lexical-editor="true"]')
except Exception as e:
    print(f"[!] Could not locate correct message box. Error: {e}")
    driver.quit()
    exit()

# Kirim pesan berulang kali
for i in range(count):
    msg_final = f"<Status: {i+1}/{count}> {msg}" if bot_prompt == 'Y' else msg
    msg_box.send_keys(msg_final)
    time.sleep(0.5)

    try:
        send_button = driver.find_element(By.XPATH, '//button[@aria-label="Kirim" or @aria-label="Send"]')
        send_button.click()
    except Exception as e:
        print(f"[!] Failed to click send button. Error: {e}")

    time.sleep(gap)

# Pesan penutup
msg_box.send_keys('Pesan selesai dikirim.')
try:
    send_button = driver.find_element(By.XPATH, '//button[@aria-label="Kirim" or @aria-label="Send"]')
    send_button.click()
except:
    pass

print("Messages sent. Closing in 30 seconds...")
time.sleep(30)
driver.quit()
