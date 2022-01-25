import justpy as jp
import inspect

from WebApp.page import Page
from WebApp.home import Home
from WebApp.about import About
from WebApp.dictionary import Dictionary

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)




# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(port=8001)
