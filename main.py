from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.keys import Keys

class InstaBot:
    def __init__(self, username):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com/accounts/login")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath('//button[@type="submit"]')\
        #     .click()
        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
            # <a class=" _81NM2" href="/_worldly_goods/following/"><span class="g47SY lOXF2">319</span> following</a>
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        print("Total number not_following_back my account- ", len(not_following_back))

        im_not_following = [user for user in followers if user not in following]
        print(im_not_following)
        print("Total number I'm not_following_back - ", len(im_not_following))

        return not_following_back

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

    def unfollow_account(self, username):
       print(username)
       self.driver.get('https://www.instagram.com/' + username + '/')
       sleep(3)
       unfollow_xpath = '//span[@class="glyphsSpriteFriend_Follow u-__7"]'
       unfollow_confirm_xpath = "/html/body/div[4]/div/div/div[3]/button[1]"
       self.driver.find_element_by_xpath(unfollow_xpath)\
       .click()
       sleep(2)
       self.driver.find_element_by_xpath(unfollow_confirm_xpath)\
       .click()
       print("Username - " + username + " unfollowed")
       sleep(3)          

    def destroy(self, accounts):
        print("destruction started ")
        for i in range(15):
            uname = ''.join(accounts[i])
            print("i and uname" + str(i) + uname)
            my_bot.unfollow_account(uname)
               
my_bot = InstaBot('_worldly_goods')
not_following_back = my_bot.get_unfollowers()
my_bot.destroy(not_following_back)


