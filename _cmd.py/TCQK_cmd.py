import rhinoscriptsyntax as rs
__author__ = "C"
__version__ = "2019.06.23"
__commandname__ = "TCQK"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):

  rs.AddLayer("_t")
  rs.CurrentLayer("_t")

  layers = rs.LayerNames()

  for layer in layers:
      if not rs.IsLayerVisible(layer):
          rs.LayerVisible(layer,True)
  return 0
