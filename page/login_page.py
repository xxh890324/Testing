from poium import Page, Element


class LoginPage(Page):
    username = Element(id_="find.ai.android:id/userNameView")
    password = Element(id_="find.ai.android:id/pwdView")
    login_button = Element(id_="find.ai.android:id/loginBtnView")
