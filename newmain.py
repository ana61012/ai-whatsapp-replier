from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from google import genai
from dotenv import load_dotenv
import os

def remove_non_bmp_characters(text):
    # This removes emojis and other special characters that crash Selenium
    return ''.join(c for c in text if c <= '\uFFFF')

# ----------- LOAD API KEY -----------

load_dotenv()

API_KEY = os.getenv("GEMINI_KEY")

# Create Gemini client (NEW SDK STYLE)
client = genai.Client(api_key=API_KEY)


def get_gemini_reply(user_message):
    try:
        prompt = f"""
        You are a helpful and friendly WhatsApp chatbot.
        
        User message:
        {user_message}
        
        Reply naturally like a real human.
        """
        
        print("Sending prompt to Gemini...")

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt[:1000]
        )

        print("Gemini Response received.")
        
        return response.text

    except Exception as e:
        print("------ GEMINI API ERROR ------")
        print(e)
        print("------------------------------")
        return "Hi! I'm currently facing API limits, but I’ll get back to you soon "



# ----------- SELENIUM PART -----------

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")

print("Scan QR code...")
time.sleep(20)

print("Logged in!")

driver.maximize_window()

wait = WebDriverWait(driver, 60)

print("Opening chat...")

search_boxes = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[contenteditable="true"]'))
)

search_box = search_boxes[0]

search_box.click()

a = input("Enter contact name: ")

search_box.send_keys(a)
time.sleep(3)

contact = wait.until(
    EC.element_to_be_clickable((By.XPATH, f'//span[@title="{a}"]'))
)

contact.click()

print("Chat opened successfully!")
time.sleep(3)

print("\nReading chat messages with sender details...\n")

messages = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//div[contains(@class,"copyable-text")]')
    )
)

chat_history = []

for msg in messages:
    try:
        sender_info = msg.get_attribute("data-pre-plain-text")

        text_element = msg.find_element(By.XPATH, './/span')
        message_text = text_element.text.strip()

        if sender_info and message_text:
            chat_history.append(f"{sender_info} {message_text}")

    except:
        pass


print("----- FULL CHAT HISTORY -----\n")

for line in chat_history:
    print(line)

print("\n-----------------------------")

last_message = chat_history[-1]

print("\nLast message detected:", last_message)

print("\nSending to Gemini AI...")

ai_reply = get_gemini_reply(last_message)

print("Gemini Reply:", ai_reply)




# ----------- SEND AI REPLY BACK -----------

input_boxes = driver.find_elements(By.CSS_SELECTOR, 'div[contenteditable="true"]')
message_box = input_boxes[-1]

message_box.click()

# --- THE FIX IS HERE ---
# Clean the text to remove the emoji before typing
clean_reply = remove_non_bmp_characters(ai_reply)

message_box.send_keys(clean_reply)
message_box.send_keys(Keys.ENTER)

print("\nAI Reply Sent Successfully!")
time.sleep(10)

driver.quit()
