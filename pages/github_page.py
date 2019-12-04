from base_page import BasePage
from selenium.webdriver.common.by import By


class GithubPage(BasePage):
	# This is the definition of the github url page
	url = (By.CSS_SELECTOR, 'https://github.com/qualityshepherd')

	# The username element is defined by a class here - the '.' is the selector symbol of a class
	username = (By.CSS_SELECTOR, '.vcard-fullname')

	def __init__(self, driver):
		super(GithubPage, self).__init__(driver)

	def loaded(self):
		''' defines when the page is loaded '''
		self.wait_for_element(self.username)