
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDemoWebShop(unittest.TestCase):

    def test_find_10_elements(self):
        driver = webdriver.Chrome()

        try:
            driver.get("https://demowebshop.tricentis.com/")
            driver.maximize_window()

            wait = WebDriverWait(driver, 10)

            # 1. By.NAME
            element1 = driver.find_element(By.NAME, "q")

            # 2-4. By.CLASS_NAME
            element2 = driver.find_element(By.CLASS_NAME, "header-links")
            element3 = driver.find_element(By.CLASS_NAME, "cart-label")
            element4 = driver.find_element(By.CLASS_NAME, "footer")

            # 5-6. By.ID
            element5 = driver.find_element(By.ID, "newsletter-email")
            element6 = driver.find_element(By.ID, "newsletter-subscribe-button")

            # 7-10. By.CSS_SELECTOR
            element7 = driver.find_element(By.CSS_SELECTOR, "a[href='/register']")
            element8 = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
            element9 = driver.find_element(By.CSS_SELECTOR, "a[href='/books']")
            element10 = driver.find_element(By.CSS_SELECTOR, "a[href='/electronics']")

            elements = [
                element1, element2, element3, element4, element5,
                element6, element7, element8, element9, element10
            ]

            for index, element in enumerate(elements, start=1):
                self.assertTrue(element.is_displayed())
                print(f"Элемент {index} найден: {element.tag_name}")

            self.assertEqual(len({element.id for element in elements}), 10)
            print("Все 10 элементов успешно найдены!")

        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()
