# POSETIPO v1.0 - 3Dview Addon - Blender 2.8
#
# THIS SCRIPT IS LICENSED UNDER GPL, 
# please read the license block.
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "KeyframeType",
    "author": "Vinícius Fidelis PK",
    "tracker_url": "https://github.com/SrFidelis/keyframe-type/issues",
    "wiki_url": "https://github.com/SrFidelis/keyframe-type", 
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Nkey Panel > Animate -> KeyframeType",
    "description": "Creates a keyframe and defines its type.",
    "warning": "",
    "support": "COMMUNITY",
    "category": "Animation"}
    
    
import bpy
from bpy.types import Panel


#bpy.ops.anim.keying_set_active_set(type='LocRotScale') #Define LocRocScale keying by default
def deletarKeyframe():
    try:
        bpy.ops.anim.keyframe_delete()
    except:
        pass

class OPERADOR_ch(bpy.types.Operator): 
    bl_label = 'Key'
    bl_idname = 'on.chave_tipo'
    bl_description = 'Keyframe as Key'

    def execute(self, context): 
        deletarKeyframe()
        bpy.context.scene.tool_settings.keyframe_type = 'KEYFRAME' 
        bpy.ops.anim.keyframe_insert() 

        return {'FINISHED'}

class OPERADOR_ext(bpy.types.Operator): 
    bl_label = 'extreme'
    bl_idname = 'on.extremo_tipo'
    bl_description = 'Keyframe as extreme'

    def execute(self, context): 
        deletarKeyframe()        
        bpy.context.scene.tool_settings.keyframe_type = 'EXTREME' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

class OPERADOR_pss(bpy.types.Operator): 
    bl_label = 'breakdown'
    bl_idname = 'on.passagem_tipo'
    bl_description = 'Keyframe as breakdown'

    def execute(self, context): 
        deletarKeyframe()
        bpy.context.scene.tool_settings.keyframe_type = 'BREAKDOWN' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

class OPERADOR_ent(bpy.types.Operator): 
    bl_label = 'inbetween'
    bl_idname = 'on.entre_tipo'
    bl_description = 'Keyframe as inbetween'

    def execute(self, context): 
        deletarKeyframe()
        bpy.context.scene.tool_settings.keyframe_type = 'JITTER' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

# UI - COMO E ONDE VAI APARECER NO BLENDER
class Posetipo_Painel(Panel): 
    bl_label = "KeyframeType"
    bl_idname = "VIEW3D_PT_PoseTipo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animate"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Remember Keying", translate=True, icon='ERROR')
        
        row = layout.row()
        row.operator('on.chave_tipo', text='KEY', icon='MESH_CIRCLE')
        
        row = layout.row()
        row.operator('on.extremo_tipo', text='Extreme', icon='DECORATE_KEYFRAME')
        
        row = layout.row()
        row.operator('on.passagem_tipo', text='Breakdown', icon='DECORATE_ANIMATE')
    
        row = layout.row()
        row.operator('on.entre_tipo', text='Inbetween', icon='DECORATE')
        
def register():
    bpy.utils.register_class(OPERADOR_ch)
    bpy.utils.register_class(OPERADOR_ext)
    bpy.utils.register_class(OPERADOR_pss)
    bpy.utils.register_class(OPERADOR_ent)
    bpy.utils.register_class(Posetipo_Painel)
    
    
def unregister():
    bpy.utils.unregister_class(OPERADOR_ch)
    bpy.utils.unregister_class(OPERADOR_ext)
    bpy.utils.unregister_class(OPERADOR_pss)
    bpy.utils.unregister_class(OPERADOR_ent)
    bpy.utils.unregister_class(Posetipo_Painel)

if __name__ == "__main__":
    register()
