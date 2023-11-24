from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    menu = '//ul[@class ="MuiList-root MuiList-padding"] /a"'
    todo_list = '//ul[@ aria-label="completed todo"]//li'
    unchecked_todo = '//ul[@ aria-label="completed todo"] // li // input[@ type="checkbox"]'
    view_todo = '// ul[@ aria-label="completed todo"] // li // span[text()="view"]'
    todo_add_button = '// div/a // span[text()="Add"]'

