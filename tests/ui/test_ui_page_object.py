from modules.ui.page_objects.sing_in_page import SingInPage
import pytest


@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    # Creating a page object
    sing_in_page = SingInPage()

    # Open the page https://github.com/login
    sing_in_page.go_to()

     # Try to log in to the system GitHub
    sing_in_page.try_login("page_object@mistake.com", "wrong password")

    # Check that the name of the page is what we expect
    assert sing_in_page.check_title("Sign in to GitHub · GitHub")

    # Close the browser
    sing_in_page.close()
