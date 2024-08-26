from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the banking application
driver.get("http://bankingapp.com/login")

# Enter username
driver.find_element_by_id("username").send_keys("testuser")

# Enter password
driver.find_element_by_id("password").send_keys("password123")

# Click Login button
driver.find_element_by_id("loginBtn").click()

# Verify successful login
assert "Account Overview" in driver.title

# Close the browser
driver.quit()
