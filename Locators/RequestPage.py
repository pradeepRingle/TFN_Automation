from selenium.webdriver.common.by import By

tfnRequests = (By.XPATH, "a")
reqText1 = (By.XPATH, "//li[contains(@class,'pro-menu-item pro-sub-menu open')]//li[2]//div[1]")
reqButton1 = (By.XPATH, "//button[normalize-space()='New']")
reqTitle1 = (By.XPATH, "//*[@id='name']")
reqNumberTFN = (By.XPATH, "//*[@id='filled-number']")
reqType = (By.XPATH, "//label[2]")
reqCreate = (By.CSS_SELECTOR, "div[role='dialog'] button:nth-child(2)")
reqRecord = (By.TAG_NAME, "h1")
reqUnlock = (By.XPATH, "//tbody/tr[1]/td[1]/div[1]/button[2]/img[1]")
reqEdit = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/div/button[3]")
reqText2 = (By.XPATH, "//div[contains(@class,'k-spreadsheet-cell')][3]/div[@class='k-vertical-align-bottom']")
reqDropdown = (By.XPATH, "//*[@id='req-type']/option[3]")
reqBack = (By.XPATH, "//*[@id='root']/div/div[1]/header/div/div/nav/ol/li[3]/a")
reqPopUpMessage = (By.ID, "add-tfn-label")
reqSave = (By.TAG_NAME, "button")
reqRecord2 = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[1]")
reqData = (By.TAG_NAME, "div")
# Add Button
reqAddButton = (By.XPATH, "//button[normalize-space()='Add']")
reqPopUpMessage2 = (By.XPATH, "//p[@id='add-tfn-label']")
reqCancel = (By.XPATH, "//button[normalize-space()='Cancel']")

# Delete Button
reqDeleteButton = (By.TAG_NAME, "button")

# Add Note Button
reqAddNoteButton = (By.XPATH, "//button[normalize-space()='Add Note']")
reqText3 = (By.XPATH, "//textarea[contains(@placeholder,'Note')]")
reqAddButton2 = (By.XPATH, "//button[normalize-space()='ADD']")
