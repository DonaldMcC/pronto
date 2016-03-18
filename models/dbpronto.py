# This will contain the basic palette shapes
# which appear to be forward, left, right and function
# but there is a possibility to go backwards too

# need to figure out how I am storing the shape date
db.define_table('shape_template',
                Field('shape_type', 'string'),
                Field('shape_prefix', 'string', comment='Three character prefix for ids created with this shape'),
                Field('shape_json', 'text'),
                Field('description', 'text'),
                Field('cub_action', 'text', comment='The code to be executed on the cubetto'))

# Likelihood is that there will just be one of each template shape in the palette
# but the background will also be here but with interactive false and the standard
# links will also be in here I think any circuit which has complete bits up to a point
# can be used in this circuit so not a lot of point in making two
# so this can be palette, background shapes and links

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

# So this should actually just be a list of up to 16 objects
# possibly change to list:reference
# then we will add some standard setup boilerplate which should be easy enough

db.define_table('program',
                Field('routinename', 'string'),
                Field('shape_list', 'list:integer'),
                Field('description', 'text'),
                Field('userid', 'reference auth_user'))
