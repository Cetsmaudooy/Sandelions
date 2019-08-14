import rhinoscriptsyntax as rs

layers = rs.LayerNames()

i = 0

for layer in layers:
    a = (i,i,0)
    b = (i,i+1,0)
    rs.CurrentLayer(layer)
    rs.AddLine(a,b)
    i += 1
    