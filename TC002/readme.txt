Prerequisites:
- Drivers (chromedriver.exe) added to environmental variables, or present in test folder. The drivers versions have to be in sinc with installed browsers. Internet Explorer is exluded, because Trello does not support it.
- Selenium webdriver package (in command line "pip install selenium")
- HtmlTestrinner (in command line "pip install html-test-Runner)


Setup:
- provide email and password of a registered account for Trello in email.txt file
	example:
	email = test@wp.pl
	password = 12345678

Execution:
- In command line within the directory of the test case type in "python trello002.py"

Results are exported to a HTML file in Report catalogue.