from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- setup trình duyệt ---
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')
options.add_argument('--disable-logging')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- 1. Truy cập trang danh sách FAQ ---
base_url = "https://fchat.vn"
faq_list_url = f"{base_url}/faq"
driver.get(faq_list_url)
time.sleep(3)

# --- 2. Lấy tất cả link câu hỏi ---
faq_links = driver.find_elements(By.CSS_SELECTOR, "ul.noidung-hoidap li.name-faq a")
urls = [a.get_attribute("href") for a in faq_links]
urls = [base_url + u if u.startswith("/") else u for u in urls]

print(f"🔗 Tìm thấy {len(urls)} câu hỏi FAQ")

# --- 3. Tạo file TXT ---
with open("faq_fchat.txt", "w", encoding="utf-8") as f:

    # --- 4. Duyệt từng trang câu hỏi ---
    for i, url in enumerate(urls, start=1):
        driver.get(url)
        # time.sleep(1.5)

        try:
            container = driver.find_element(By.CSS_SELECTOR, "div.content-faq.traloi")
            question = container.find_element(By.CSS_SELECTOR, "h1").text.strip()

            paragraphs = container.find_elements(By.TAG_NAME, "p")
            answers = [p.text.strip() for p in paragraphs if p.text.strip()]
            answer_text = "\n".join(answers)

            print(f"\n✅ [{i}] {question}")

            # --- Ghi vào file TXT ---
            f.write(f"Q{i}: {question}\n")
            f.write(f"{answer_text}\n")
            f.write("\n" + "-"*80 + "\n\n")

        except Exception as e:
            print(f"⚠️ Lỗi ở {url}: {e}")

driver.quit()
print("\n🎉 Crawl xong! Dữ liệu lưu ở file: faq_fchat.txt")
