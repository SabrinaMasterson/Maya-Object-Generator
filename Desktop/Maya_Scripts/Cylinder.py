import maya.cmds as cmds

import random

def PolyCylinders(\
x = random.uniform(-10,10),\
x_r = 1,\
y = random.uniform(0,20),\
y_r = 1,\
z = random.uniform(-10,10),\
z_r = 1,\
xRot = random.uniform( 0, 360 ),\
xRot_r = 10,\
yRot = random.uniform( 0, 360 ),\
yRot_r = 10,\
zRot = random.uniform( 0, 360 ),\
zRot_r = 10,\
r = random.uniform(0,2),\
r_r = .1,\
g = random.uniform(0,2),\
g_r = .1,\
b = random.randint(0,2),\
b_r = .1,\
scaleF = random.uniform( 0.3, 1.5 ),\
scaleF_r = .1,\
):
    
    def change(start,min,max,rate):
    	if random.randint(0,5) == 0:
    		rate = (-1 * rate)
    	start += rate
    	if start < min or start > max:
    		rate = (-1 * rate)
    		start += rate
    	return start,rate
    
    for i in range( 0, 50 ):
       
       #create cube
    	cmds.polyCylinder( sx=1, sy=1, sz=1, h=1, n='cylinder{}'.format(i))
    	
    	#vary location
    	x = change(x,-10,10,x_r)[0]
    	x_r = change(x,-10,10,x_r)[1]
    	y = change(y,0,20,y_r)[0]
    	y_r = change(y,0,20,y_r)[1]
    	z = change(z,-10,10,z_r)[0]
    	z_r = change(z,-10,10,z_r)[1]
    	
    	#vary rotation
    	xRot = change(xRot,1,360,xRot_r)[0]
    	xRot_r = change(xRot,1,360,xRot_r)[1]
    	yRot = change(yRot,1,360,yRot_r)[0]
    	yRot_r = change(yRot,1,360,yRot_r)[1]
    	zRot = change(zRot,1,360,zRot_r)[0]
    	zRot_r = change(zRot,1,360,zRot_r)[1]
    	
    	#vary color
    	r = change(r,0,2,r_r)[0]
    	r_r = change(r,0,2,r_r)[1]
    	g = change(g,0,2,g_r)[0]
    	g_r = change(g,0,2,g_r)[1]
    	b = change(b,0,2,b_r)[0]
    	b_r = change(b,0,2,b_r)[1]
    	
    	#vary scale
    	scaleF = change(scaleF,0.3,1.5,scaleF_r)[0]
    	scaleF_r = change(scaleF,0.3,1.5,scaleF_r)[1]
    	
    	#apply variabels
    	cmds.rotate( xRot, yRot, zRot, 'cylinder{}'.format(i))
    	
    	cmds.scale(scaleF, scaleF, scaleF, 'cylinder{}'.format(i))
    	
    	cmds.move( x, y, z, 'cylinder{}'.format(i))
    	
    	cmds.sets( name='CylinderMaterial{}'.format(i), renderable=True, empty=True )
    	cmds.shadingNode( 'phong', name='CylinderShader{}'.format(i), asShader=True )
    	cmds.setAttr( 'CylinderShader{}'.format(i)+'.color', r, g, b, type='double3' )
    	cmds.surfaceShaderList( 'CylinderShader{}'.format(i), add='CylinderMaterial{}'.format(i))
    	cmds.sets( 'cylinder{}'.format(i), forceElement='CylinderMaterial{}'.format(i))
PolyCylinders()