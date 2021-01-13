import sys
sys.path.append(r"E:\FrameWork\Pages")
from Page.automating_webshop import AutomatingWebshop

class TestRegister:
    def test_fun(self):
        aw = AutomatingWebshop()
        aw.launch_url()
        aw.click_reg()
        aw.click_radio()
        aw.enter_fname()
        aw.enter_lname()
        aw.enter_email()
        aw.enter_password()
        aw.confirm_password()
        aw.click_register()
