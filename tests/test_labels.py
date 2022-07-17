import allure
from allure_commons.types import Severity


def test_dynamic_label():
    allure.dynamic.tag('Web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Tasks in the repository')
    allure.dynamic.story('Unauthorized user cannot create a task in the repository')
    allure.dynamic.link('https://github.com/', name='Testing')
    pass


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Bohdan')
@allure.feature('Tasks in the repository')
@allure.story('Authorized user can create a task in the repository')
@allure.link('https://github.com/', name='Testing')
def test_decorator_labels():
    pass












