# Data & Mesh related abstractions for internal Blender functions

import bpy


def getVcolLayers():
    """List Vertex Color Layers"""

    return


def createVcolLayer(C, vcolname: str):
    """Create a Vertex Color Layer"""
    if name and C.object:
        C.object.data.vertex_colors.new(name=vcolname)
        # vcols=C.object.data.vertex_colors.keys()


    return


def removeVcolLayer(C, vcolname: str):
    """Remove the given Vertex Color Layer """

    if vcol and C.object:
        C.object.data.vertex_colors.remove(C.object.data.vertex_colors[vcolname])


def fillVcolLayer(obj, vcolname: str, color_rgba: tuple):
    """Fill the given Vertex Color Layer with the Color parameter values"""

    mesh = obj.data

    vcollayer = mesh.vertex_colors[vcolname]

    i = 0
    for poly in mesh.polygons:
        for idx in poly.loop_indices:
            vcollayer.data[i].color = color_rgba
            i += 1


def fillVcolLayerVmesh(obj, vcolname: str, color_rgba: tuple):
    """Fill the given Vertex Color Layer with the Color parameter values using Bmesh"""
    
    #BMESH
    #bm.verts.ensure_lookup_table()

    import bmesh
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)

    color_layer = bm.loops.layers.color[vcolname]
    # make a random color dict for each vert
    # vert_color = random_color_table[vert]

    def random_color(alpha=1):
        return [uniform(0, 1) for c in "rgb"] + [alpha]
    
    for face in bm.faces:
        for loop in face.loops:
            loop[color_layer] = color_rgba
            
    bm.to_mesh(mesh)  
        
    

def applyVcolLayer(vcolname: str):

    return
