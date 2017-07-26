from selenium import webdriver
from time import sleep


browser = webdriver.Firefox() # or webdriver.Chrome()
print ('Opening Facebook')

browser.get('https://www.facebook.com/login.php')
sleep(2)

email = 'your email'
password = 'your password'
# feel free to add prompts to ask for user and pass
# a little more time... but a little more secure I would think

print('logging in')
emailElem = browser.find_element_by_id('email')
emailElem.send_keys(email)
passElem = browser.find_element_by_id('pass')
passElem.send_keys(password)
loginElem = browser.find_element_by_id('loginbutton')
loginElem.click()

message = str(input('Type your message to the group: '))
sleep(2)
print('Navigating to Facebook Group')
browser.get('https://www.facebook.com/groups/727893477272975')


print('Posting Message')

try:
    post_box = browser.find_element_by_xpath("//textarea[@class ='_4h98 navigationFocus']")
    post_box.click() # I added this so box will expand and then type your message.
    # without it, text box won't always expand and 'post button' will not be found by CSS selector
    post_box.send_keys(message)

except:
    print('No element found. Spell check/try a different selector.')

#obviously, if the text isn't found and located the post button won't work
#I split it this way for debugging purposes, to know where the script went wrong.

sleep(5)

try:
    post = browser.find_element_by_css_selector('button._1mf7._4jy0._4jy3._4jy1._51sy.selected._42ft')
    post.click()
    print('Message posted')

except:
    print('No post button element found.')


# You can remove code below if you do not want to close browser after posting
print('Closing Browser')
sleep(5)
browser.close()
