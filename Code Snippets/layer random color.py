import rhinoscriptsyntax as rs
import random
from System.Drawing import Color

layers = rs.LayerNames()

def randomcolor():
    red = int(255*random.random())
    green = int(255*random.random())
    blue = int(255*random.random())
    return Color.FromArgb(red,green,blue)
    
for layer in layers:
    rs.LayerColor(layer, randomcolor())