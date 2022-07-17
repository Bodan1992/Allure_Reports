"""
1. Добавить в requirements строчку   allure-pytest
2. В тесте нажать на иконку стрелки и нажать modify run configuration и(повторять в каждом тесте)
в строке additional arguments прописать --alluredir=allure-results
3. Установить алюр https://docs.qameta.io/allure/
4. В консоли прописать  allure serve tests/allure-results(где tests/allure-results путь где лежат отчеты)
5. Если нужно писать с шагами то это делается в test_steps,  именно прописать
    with allure.step('название шага'):
        browser.open("https://github.com/")-что делает
6. Если нужно написать через люмбду то пишут в test_lambda_steps, и нужно добавить декоратор +
    @allure.step('название шага')
7. Если нужно добавлять аттачмент файлы то пишут в test_attachments и указывают текст,тип файла.
    Чтобы увидеть все типы аттачи которые возможны нужно зажать ctrl и кликнуть на импорт attachment_type,
    и там будут отображены все возможные типы
8. Если нужна разметка тестов то пишут test_labels и указывают перед тестом "Разметку тестов всеми аннотациями"
    @allure.tag и т.д
9.
"""

