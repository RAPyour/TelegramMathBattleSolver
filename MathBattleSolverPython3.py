from selenium.webdriver import Chrome

GAME_URL = 'https://tbot.xyz/math/#eyJ1Ijo4ODk5Njk3MDEsIm4iOiLjhaTjhaRQb3J0Z2FzIEQuIEFjZfCflKUgIiwiZyI6Ik1hdGhCYXR0bGUiLCJjaSI6IjE5MjA2NTk2ODYyODE4OTgzMzUiLCJpIjoiQlFBQUFOTVpBZ0JKRy1xbzQ3azk4X0tHd0Z3In01NGQ1OGUzMDU5MTNhNDI5MTgyNjhkYjUzNjI0NjZkMA'
WEBDRIVER_PATH = '/home/test/Downloads/chromedriver'
NUMBER_OF_WINS = 50

browser = Chrome(WEBDRIVER_PATH)
browser.get(GAME_URL)

#Start game
button = browser.find_element_by_id("button_correct")
button.click()

#Play 
i =0
while i<NUMBER_OF_WINS:
    task_x = int(browser.find_element_by_id("task_x").text.strip())
    task_op = browser.find_element_by_id("task_op").text
    task_y = int(browser.find_element_by_id("task_y").text.strip())
    task_res = int(browser.find_element_by_id("task_res").text.strip())
    print ("X:",task_x,"Operator:",task_op,"Y:",task_y,"Result:",task_res)

    result = -1
    if task_op=="/":
        result = task_x / task_y
    if task_op=="+":
        result = task_x + task_y
    if task_op=="–":
        result = task_x - task_y
    if task_op=="×":
        result = task_x * task_y
    
    print(result)
    button_wrong = button = browser.find_element_by_id("button_wrong")
    button_correct = button = browser.find_element_by_id("button_correct")
    if result==task_res:
        button_correct.click()
    else:
        button_wrong.click()
i=i+1
