Prerequisites:
- python 3.7.5 (or higher)
- Driver (chromedriver.exe) added to environmental variables, or present in test folder. The drivers version has to be in sinc with installed browsers. Internet Explorer is excluded, because Trello does not support it.
- Selenium webdriver package (in command line "pip install selenium")
- HtmlTestrinner (in command line "pip install html-test-Runner)
- XLUtils (in command line "pip install XLUtils")
- openpyxl (in command line "pip install openpyxl")


Setup:
- provide email and password of a registered account for Trello in email.txt file
	example:
	email = test@wp.pl

Execution:
- In command line within the directory of the test case type in "python trello004.py"

Results are exported to a HTML file in Report catalogue.
