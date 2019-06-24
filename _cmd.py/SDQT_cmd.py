import rhinoscriptsyntax as rs

__author__ = "C"
__version__ = "2019.06.23"
__commandname__ = "SDQT"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
  # this script can turn off layers of your selected object


  rs.AddLayer("_t")
  rs.CurrentLayer("_t")

  layers = rs.LayerNames()
  CurObjLayNames=[]

  CurObjs = rs.GetObjects("select object to keep layers on")

  for CurObj in CurObjs:
      CurObjLayId = rs.ObjectLayer(CurObj)
      CurObjLayName = rs.LayerName(CurObjLayId, fullpath=True)
      CurObjLayNames.extend([CurObjLayName])

  for layer in layers:
      if layer not in CurObjLayNames and layer != "_t":
          rs.LayerLocked(layer,True)
  return 0
