# This will contain the basic palette shapes
# which appear to be forward, left, right and function
# but there is a possibility to go backwards too

db.define_table('shape_template',
                Field('shape_type', 'string'),
                Field('shape_prefix', 'string', comment='Three character prefix for ids created with this shape'),
                Field('shape_json', 'text'),
                Field('description', 'text'),
                Field('cub_action', 'text', comment='The code to be executed on the cubetto'))

# There will just be one of each template shape in the palette

db.define_table('startup',
                Field('shape_name', 'string'),
                Field('shape_template', 'reference shape_template'),
                Field('description', 'text'),
                Field('posx', 'integer'),
                Field('posy', 'integer'),
                Field('stroke', 'string'),
                Field('fill', 'string'),
                Field('textstring', 'string'),
                 Field('zindex','integer'))

db.define_table('startlinks',
                Field('shape_name', 'string'),
                Field('shape_template', 'reference shape_template'),
                Field('sourceid', 'string'),
                Field('targetid', 'string'),
                Field('zindex','integer'))

db.define_table('program',
                Field('routinename', 'string'),
                Field('shape_list', 'list:integer'),
                Field('description', 'text'),
                Field('userid', 'reference auth_user'))
                
db.define_table('serialport',
                Field('routinename', 'string', default='/dev/ttyUSB0'),
                Field('baud', 'integer', default=9600),
                Field('paritey', 'string', default='None'),
                Field('stopbits', 'integer', default=1))

