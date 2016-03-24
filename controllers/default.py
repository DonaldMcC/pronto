# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

from pronto_functions import commandlist,sendcommand

def index():
    startupshapes = db(db.startup.id>0).select()
    cellsjson = '['
    slotarray = '['
    linkarray = '['
    palarray = '['

    for row in startupshapes:
        template=row.shape_template.shape_json % (row.shape_name, row.posx, row.posy,
                                                      row.stroke, row.fill,row.textstring)
        cellsjson += template + ','
        if row.shape_name[:3] == 'slt':
            slotarray += '"' + row.shape_name + '",'
        if row.shape_name[:3] == 'pal':
            palarray += '"' + row.shape_name + '",'

    startlinks = db(db.startlinks.id>0).select()
    for row in startlinks:
        template=row.shape_template.shape_json % (row.shape_name, row.sourceid, row.targetid)
        cellsjson += template + ','
        linkarray += '"' + row.shape_name + '",'
        

    cellsjson = cellsjson[:-1]+']'
    slotarray = slotarray[:-1]+']'
    linkarray = linkarray[:-1]+']'
    palarray = palarray[:-1]+']'
    return dict(cellsjson=XML(cellsjson), slotarray=XML(slotarray), linkarray=XML(linkarray), palarray=XML(palarray))

def shapelist():

    sentlist = request.vars.stringarray.split(',')
    mainstring=''
    funcstring=''
    
    mainlist = sentlist[:12]
    funclist = sentlist[12:16]
    
    for cmd in mainlist:
        if cmd[:6] == 'objfwd':
            mainstring+='F'
        elif cmd[:6] == 'objrgt':
            mainstring +='R'
        elif cmd[:6] == 'objlft':
            mainstring +='L'
        elif cmd[:6] == 'objfnc':
            mainstring +='X'

    # not supporting function in function as that is infinite
    for cmd in funclist:
        if cmd[:6] == 'objfwd':
            funcstring+='F'
        elif cmd[:6] == 'objrgt':
            funcstring +='R'
        elif cmd[:6] == 'objlft':
            funcstring +='L'

    print(mainstring)
    print(funcstring)
    
    
    finalblock = commandlist(mainstring, funcstring)
    invert = False
    if invert:
        reverseblock = ''
        for x in finalblock:
            if x == 'F':
                reverseblock+='B'
            elif x == 'R':
                reverseblock+='L'
            elif x == 'L':
                reverseblock+='R'
            elif x == 'B':
                reverseblock+='F'
        finalblock=reverseblock        

    serialsetup = db(db.serialport.id > 0).select().first()    
    sendcommand(finalblock, serialsetup.routinename, serialsetup.baud)

    return finalblock

def teststring():
    teststring = 'FRFRL'
    functionblock = ''
    
    finalblock = commandlist(teststring, functionblock)

    sendcommand(finalblock)
    return dict(teststring=teststring)
    
def serialport():
    if db(db.serialport.id > 0).isempty():
        db.serialport.insert()
    grid = SQLFORM.grid(db.serialport, create=False, deletable=False, searchable=False, csv=False, user_signature=False)
    return dict(grid=grid) 
    
    
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
