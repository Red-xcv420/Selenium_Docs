#Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="ifl-InputFormField-146"]"}
"""Try using Full XPATH any error like this means the element was not found."""

#selenium.common.exceptions.JavascriptException: Message: javascript error: Invalid or unexpected token
"""Are you trying to execute Javascript to the browser using selenium?, Make sure your Javascript is written correctly."""

#AttributeError: 'NoneType' object has no attribute 'send_keys'
"""
Try these imports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""

#[<selenium.webdriver.remote.webelement.WebElement (session="1c402fdd805a809441060e8c5af66f93", element="ab74f36f-87d7-49c9-9669-63bb2a4f8790")>]
"""
Did you put .text, after you defined the element? Or did you just try to print it?

Try this...

Text_From_Element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, 'xpath goes here'))).text
print(Text_From_Element)
"""

#from session not created: This version of ChromeDriver only supports Chrome version 99
"""
The Chrome driver exe you downloaded does not work for your browser, The one you downloaded only supports 99, You have something else. 
Check your browser version and get the one you need from https://sites.google.com/chromium.org/driver/
"""

#Do you have a squiggle line under the imports for selenium?
"""
Open CMD and run this...
---

pip install selenium

---

If This Doesnt Work https://www.youtube.com/watch?v=Ua743l1J3cg Follow This
"""
