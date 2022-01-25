import justpy as jp
from definition import Definition
from WebApp.layout import DefaultLayout
from WebApp.page import Page

class Dictionary(Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        divMain = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=divMain, text="Instant Dictionary", classes="text-4xl m-2")
        jp.Div(a=divMain, text="Get the definition of any English word instantly as you type.",
               classes="text-lg")

        input_div = jp.Div(a=divMain, classes="grid grid-cols-2")

        output_div = jp.Div(a=divMain, classes="m-2 p-2 text-lg border-2 h-40")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none "
                                     "focus:border-purple-500 "
                                     "py-2 px-4 ")

        input_box.on('input', cls.get_definition)


        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = Definition(widget.value).get()
        widget.outputdiv.text = "".join(defined)

