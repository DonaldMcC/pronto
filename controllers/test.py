import gluon.contrib.simplejson

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Testing the pronto")

    cells=[{"type":"basic.Rect","position":{"x":200,"y":30},"size":{"width":100,"height":30},"angle":0,"id":"test","z":1,"attrs":{"rect":{"fill":"blue"},"text":{"text":"my box","fill":"white"}}}]

    cellsjson = gluon.contrib.simplejson.dumps(cells)

    return dict(message=T('Hello World'),cellsjson=cellsjson)

def setup():
    #This will setup the basic shapes once we can draw them


    return dict(message=T('Hello World'),cellsjson=cellsjson)

def palette():
    #This will setup the basic shapes once we can draw them

    response.flash = T("Palette")

    cells=[{"type":"basic.Rect","position":{"x":200,"y":30},"size":{"width":100,"height":30},"angle":0,"id":"test","z":1,"attrs":{"rect":{"fill":"blue"},"text":{"text":"my box","fill":"white"}}}]

    cellsjson = gluon.contrib.simplejson.dumps(cells)
    return dict(message=T('Hello World'),cellsjson=cellsjson)