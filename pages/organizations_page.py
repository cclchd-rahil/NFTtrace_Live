from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class Organizations(BasePage):
    ORGANIZATIONS = (By.XPATH, "//body[1]/div[1]/main[1]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]/span[2]/div[1]/span[1]")
    CREATEORG = (By.XPATH, "//button[contains(text(),'Create Organization')]")
    ORGNAME = (By.NAME, "organizationName")
    SELECTINDUSTRY = (By.XPATH, "//select[@id='type']")
    CINGSTIN = (By.ID, "GSTIN")
    UDYOGAADHAR = (By.ID, "aadhaar")
    PAN = (By.ID, "pan")

