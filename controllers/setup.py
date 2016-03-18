#This will provide basic maintenance options on the main tables for now and
#also initial setup function to load the default template

def index():
    if db(db.serialport.id > 0).isempty():
        db.serialport.insert()
    return locals()

def shape_mgmt():
    grid = SQLFORM.grid(db.shape_template, orderby=[db.shape_template.shape_prefix])
    return locals()

def start_mgmt():
    grid = SQLFORM.grid(db.startup, orderby=[db.startup.shape_name],user_signature=False)
    return locals()

def program_mgmt():
    grid = SQLFORM.grid(db.program, orderby=[db.program.routine_name],user_signature=False)
    return locals()

def shape_setup():
    #so lets go with define these but replace parameters with relevant points
    #posx, posy, stroke, fill, and text will do for now I think

#m 0 385  L20 385 Q440 400 500 -140  L350 -270 L200 -140 Q150 50 20 0 L0 0 z
#old left m 0 200  L180 200 Q480 100 400 -40  L300 -80 L200 -40 Q150 50 80 20 L0 20 z
#new right m 0 0 L0 385 L80 400 Q200 380 200 560  L350 680 L500 560 Q450 0 80 0 L0 0
#old right m 0 0 L0 350 L80 350 Q200 300 200 490  L325 580 L450 490 Q450 0 80 0 L0 0

    fwdjson = r'''new joint.shapes.basic.Path({
   id: '%s',
   position: { x: %d, y: %d },
   z: 2,
   attrs: {
       path: { d: 'm 3 200  L153 200 L203 100 L153 0 L3 0 z ', stroke:'%s', fill: '%s' },
       text: { text: '%s', 'ref-y': .5, fill: 'white' }}})'''

    leftjson = r'''new joint.shapes.basic.Path({
           id: '%s',
   position: { x: %d, y: %d },
      z: 2,
   attrs: {
       path: { d: 'm 0 485  L20 485 Q440 500 500 -40  L350 -170 L200 -40 Q150 110 20 100 L0 100 z ', stroke:'%s', fill: '%s'  },
       text: { text: '%s', 'ref-y': .5, fill: 'white' }}})'''

    rightjson = r'''new joint.shapes.basic.Path({
           id: '%s',
   position: { x: %d, y: %d },
   z: 2,
   attrs: {
       path: { d: 'm 0 110 L0 495 L80 510 Q200 490 200 670  L350 790 L500 670 Q450 110 80 110 L0 110  ', stroke:'%s', fill: '%s' },
       text: { text: '%s', 'ref-y': .5, fill: 'white' }}})'''

    funcjson = r'''new joint.shapes.basic.Circle({
    id:'%s',
    size: { width: 70, height: 70 },
    position: {x: %d, y: %d},
    z: 2,
    attrs: {circle: { stroke:'%s', fill: '%s', transform: 'translate(25, 25)' }, text: {text:'%s', fill:'white'}}})'''

    slotjson = r'''new joint.shapes.basic.Path({
           id: '%s',
                    position: { x: %d, y: %d },
                    z: 2,
                attrs: {
                path: { d: 'm0 0 L0 200 l10 0 q20 -100 0 -200 z', stroke:'%s', fill:'%s'  },
                    text: { text: '%s', 'ref-y': .5, fill: 'white' }}})'''

    linkjson = r'''new joint.dia.Link({
    id: '%s',
    source: { id: '%s' },
    target: { id: '%s' },
    attrs: ({
    '.connection': { stroke: 'blue', 'stroke-width': 5 },
    '.marker-target': { fill: 'yellow', d: 'M 10 0 L 0 5 L 10 10 z' }})})'''

    shapelist = [{'shape_type': 'Forward', 'shape_prefix': 'fwd', 'shape_json': fwdjson, 'description': 'The shape to move forward',
                'cub_action': 'This will be code' },
               {'shape_type': 'Left', 'shape_prefix': 'lft', 'shape_json': leftjson, 'description': 'The shape to move left',
                'cub_action': 'This will be code' },
               {'shape_type': 'Right', 'shape_prefix': 'rgt', 'shape_json': rightjson, 'description': 'The shape to move right',
                'cub_action': 'This will be code' },
               {'shape_type': 'Function', 'shape_prefix': 'fnc', 'shape_json': funcjson, 'description': 'The function shape',
                'cub_action': 'This will be code' },
               {'shape_type': 'Slot', 'shape_prefix': 'slt', 'shape_json': slotjson, 'description': 'The holes on the board',
                'cub_action': 'na'},
               {'shape_type': 'Link', 'shape_prefix': 'lnk', 'shape_json': linkjson, 'description': 'The links between slots',
                'cub_action': 'na'}]

    db.shape_template.truncate()
    db.commit()

    for x in shapelist:
        db.shape_template.insert(**x)

    return locals()

def start_setup():
    #so this builds the full pallet of objects which I think we will basically define manually for now as one off setup
    #and that gives full control until it works - we can loop later
    #eventually will do a prompt for this but lets just delete and re-setup for now

    db.startup.truncate()
    db.startlinks.truncate()
    db.commit()


    fwdid=db(db.shape_template.shape_prefix=='fwd').select().first().id
    lftid=db(db.shape_template.shape_prefix=='lft').select().first().id
    rgtid=db(db.shape_template.shape_prefix=='rgt').select().first().id
    fncid=db(db.shape_template.shape_prefix=='fnc').select().first().id
    sltid=db(db.shape_template.shape_prefix=='slt').select().first().id
    lnkid=db(db.shape_template.shape_prefix=='lnk').select().first().id

    
# below could be made much less repetitive - however we may change so just leaving as is for now    
    
    startlist = [
{'shape_name': 'slt01', 'shape_template': sltid, 'description': 'Slot1', 'posx': 200, 'posy': 40, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot1', 'zindex': 2},
{'shape_name': 'slt02', 'shape_template': sltid, 'description': 'Slot2', 'posx': 380, 'posy': 40, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot2', 'zindex': 2},
{'shape_name': 'slt03', 'shape_template': sltid, 'description': 'Slot3', 'posx': 560, 'posy': 40, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot3', 'zindex': 2},
{'shape_name': 'slt04', 'shape_template': sltid, 'description': 'Slot4', 'posx': 740, 'posy': 40, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot4', 'zindex': 2},
{'shape_name': 'slt05', 'shape_template': sltid, 'description': 'Slot5', 'posx': 740, 'posy': 140, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot5', 'zindex': 2},
{'shape_name': 'slt06', 'shape_template': sltid, 'description': 'Slot6', 'posx': 560, 'posy': 140, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot6', 'zindex': 2},
{'shape_name': 'slt07', 'shape_template': sltid, 'description': 'Slot7', 'posx': 380, 'posy': 140, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot7', 'zindex': 2},
{'shape_name': 'slt08', 'shape_template': sltid, 'description': 'Slot8', 'posx': 200, 'posy': 140, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot8', 'zindex': 2},
{'shape_name': 'slt09', 'shape_template': sltid, 'description': 'Slot9', 'posx': 200, 'posy': 240, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot9', 'zindex': 2},
{'shape_name': 'slt10', 'shape_template': sltid, 'description': 'Slot10', 'posx': 380, 'posy': 240, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot10', 'zindex': 2},
{'shape_name': 'slt11', 'shape_template': sltid, 'description': 'Slot11', 'posx': 560, 'posy': 240, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot11', 'zindex': 2},
{'shape_name': 'slt12', 'shape_template': sltid, 'description': 'Slot12', 'posx': 740, 'posy': 240, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot12', 'zindex': 2},
{'shape_name': 'slt13', 'shape_template': sltid, 'description': 'Slot13', 'posx': 200, 'posy': 340, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot13', 'zindex': 2},
{'shape_name': 'slt14', 'shape_template': sltid, 'description': 'Slot14', 'posx': 380, 'posy': 340, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot14', 'zindex': 2},
{'shape_name': 'slt15', 'shape_template': sltid, 'description': 'Slot15', 'posx': 560, 'posy': 340, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot15', 'zindex': 2},
{'shape_name': 'slt16', 'shape_template': sltid, 'description': 'Slot16', 'posx': 740, 'posy': 340, 'stroke': 5, 'fill': 'black', 'textstring': 'Slot16', 'zindex': 2},
{'shape_name': 'palfwd01', 'shape_template': fwdid, 'description': 'Move Forward', 'posx': 50, 'posy': 40, 'stroke': 5, 'fill': 'red', 'textstring': 'Forward', 'zindex': 2},
{'shape_name': 'pallft02', 'shape_template': lftid, 'description': 'Move left', 'posx': 50, 'posy': 140, 'stroke': 5, 'fill': 'yellow', 'textstring': 'Left', 'zindex': 2},
{'shape_name': 'palrgt03', 'shape_template': rgtid, 'description': 'Move right', 'posx': 50, 'posy': 240, 'stroke': 5, 'fill': 'blue', 'textstring': 'Right', 'zindex': 2},
{'shape_name': 'palfnc04', 'shape_template': fncid, 'description': 'Function', 'posx': 50, 'posy': 340, 'stroke': 5, 'fill': 'green', 'textstring': 'Function', 'zindex': 2}]

    for x in startlist:
        db.startup.insert(**x)


    links = [{'shape_name': 'lnk01', 'shape_template': lnkid, 'sourceid': 'slt01', 'targetid': 'slt02', 'zindex': 2},
             {'shape_name': 'lnk02', 'shape_template': lnkid, 'sourceid': 'slt02', 'targetid': 'slt03', 'zindex': 2},
             {'shape_name': 'lnk03', 'shape_template': lnkid, 'sourceid': 'slt03', 'targetid': 'slt04', 'zindex': 2},
             {'shape_name': 'lnk04', 'shape_template': lnkid, 'sourceid': 'slt04', 'targetid': 'slt05', 'zindex': 2},
             {'shape_name': 'lnk05', 'shape_template': lnkid, 'sourceid': 'slt05', 'targetid': 'slt06', 'zindex': 2},
             {'shape_name': 'lnk06', 'shape_template': lnkid, 'sourceid': 'slt06', 'targetid': 'slt07', 'zindex': 2},
             {'shape_name': 'lnk07', 'shape_template': lnkid, 'sourceid': 'slt07', 'targetid': 'slt08', 'zindex': 2},
             {'shape_name': 'lnk08', 'shape_template': lnkid, 'sourceid': 'slt08', 'targetid': 'slt09', 'zindex': 2},
             {'shape_name': 'lnk09', 'shape_template': lnkid, 'sourceid': 'slt09', 'targetid': 'slt10', 'zindex': 2},
             {'shape_name': 'lnk10', 'shape_template': lnkid, 'sourceid': 'slt10', 'targetid': 'slt11', 'zindex': 2},
             {'shape_name': 'lnk11', 'shape_template': lnkid, 'sourceid': 'slt11', 'targetid': 'slt12', 'zindex': 2},
             {'shape_name': 'lnk13', 'shape_template': lnkid, 'sourceid': 'slt13', 'targetid': 'slt14', 'zindex': 2},
             {'shape_name': 'lnk14', 'shape_template': lnkid, 'sourceid': 'slt14', 'targetid': 'slt15', 'zindex': 2},
             {'shape_name': 'lnk15', 'shape_template': lnkid, 'sourceid': 'slt15', 'targetid': 'slt16', 'zindex': 2}]

    for x in links:
        db.startlinks.insert(**x)

    return locals()
