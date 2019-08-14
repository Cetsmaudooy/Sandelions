import rhinoscriptsyntax as rs

rs.AddLayer("_t")
rs.CurrentLayer("_t")

Layers = []
CurObjLayNames=[]
CurObjLayParentNames=[]

for layer in rs.LayerNames():
    if not rs.IsLayerLocked(layer):
        Layers.extend([layer])
        
Layers = list(dict.fromkeys(Layers))



CurObjs = rs.GetObjects("select object to keep layers on")

for CurObj in CurObjs:
  CurObjLayId = rs.ObjectLayer(CurObj)
  CurObjLayName = rs.LayerName(CurObjLayId, fullpath=True)
  CurObjLayNames.extend([CurObjLayName])
  CurObjLayNames = list(dict.fromkeys(CurObjLayNames))
  

for name in CurObjLayNames:
    for layer in Layers:
        if rs.IsLayerParentOf(name,layer):
            CurObjLayParentNames.extend([layer])
            
    CurObjLayParentNames = list(dict.fromkeys(CurObjLayParentNames))

layList = CurObjLayNames + CurObjLayParentNames

i =0
for layer in Layers:
    if layer not in layList and layer != "_t":
        rs.LayerLocked(layer,True)
        i += 1

rs.MessageBox(str(i) + " layers Locked" , 0 , title="SDQT_Sandelions")
