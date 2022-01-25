import justpy as jp
from WebApp.layout import DefaultLayout
from WebApp.page import Page

class About(Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)


        divMain = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=divMain, text="About page", classes="text-4xl m-2")
        jp.Div(a=divMain, text="""YALALALALLALALLA
        ALLALALALALALALLAALLA
        ALLALALALALALALAL
        ALLALALALALALA
        ALALALALALALllll""", classes="text-lg")

        return wp


