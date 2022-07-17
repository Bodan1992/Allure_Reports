import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_decorator_steps():
    open_main_page()
    searching_for_a_repository('Bodan1992/Bodan1992-JS')
    follow_the_repository_link('Bodan1992/Bodan1992-JS')
    switch_to_tab_issues()
    checking_the_number_issue_with_number('#1')

@allure.step('Open main page')
def open_main_page():
    browser.open("https://github.com/")

@allure.step('Searching for a repository {repo}')
def searching_for_a_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()

@allure.step('Follow the repository link {repo}')
def follow_the_repository_link(repo):
    s(by.link_text(repo)).click()

@allure.step('Switch to tab Issues')
def switch_to_tab_issues():
    s("#issues-tab").click()

@allure.step('Checking the number Issue with number {number}')
def checking_the_number_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)