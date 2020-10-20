# INSTANT KEYFRAME TYPE v1.0 - 3Dview Addon - Blender 2.8
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
    "name": "Instant Keyframe Type",
    "author": "Vinícius Fidelis PK",
    "tracker_url": "http://bit.ly/2PUonQv", # relatar defeito
    "wiki_url": "http://wiki.blender.org/index.php", # documentação
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Nkey Panel > Animate -> InstantKeyType",
    "description": "Make keyframes with instantly type defined",
    "warning": "",
    "support": "COMMUNITY",
    "category": "Animation"}
    
    
import bpy
from bpy.types import Panel


#bpy.ops.anim.keying_set_active_set(type='LocRotScale') #Define LocRocScale keying by default


class OPERADOR_ch(bpy.types.Operator): 
    bl_label = 'chave'
    bl_idname = 'on.chave_tipo'
    bl_description = 'Keyframe as KEY'

    def execute(self, context):
        bpy.context.scene.tool_settings.keyframe_type = 'KEYFRAME' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

class OPERADOR_ext(bpy.types.Operator):
    bl_label = 'extremo'
    bl_idname = 'on.extremo_tipo'
    bl_description = 'Keyframe as Extreme'

    def execute(self, context):
        bpy.context.scene.tool_settings.keyframe_type = 'EXTREME' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

class OPERADOR_pss(bpy.types.Operator): 
    bl_label = 'passagem'
    bl_idname = 'on.passagem_tipo'
    bl_description = 'Keyframe as Breakdown'

    def execute(self, context): 
        bpy.context.scene.tool_settings.keyframe_type = 'BREAKDOWN' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

class OPERADOR_ent(bpy.types.Operator): 
    bl_label = 'entre'
    bl_idname = 'on.entre_tipo'
    bl_description = 'Keyframe as Inbetween'

    def execute(self, context): 
        bpy.context.scene.tool_settings.keyframe_type = 'JITTER' 
        bpy.ops.anim.keyframe_insert() 
        
        return {'FINISHED'}

# UI 
class Posetipo_Painel(Panel):
    bl_label = "InstantKeyframeType"
    bl_idname = "VIEW3D_PT_InstantKeyType"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animate"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        #Texto Lembre-se
        row = layout.row()
        row.label(text="Remember to set keying", translate=True, icon='ERROR')
        
        #Botão da Chave
        row = layout.row()
        row.operator('on.chave_tipo', text='KEY', icon='MESH_CIRCLE')
        
        #Botao do Extremo
        row = layout.row()
        row.operator('on.extremo_tipo', text='Extreme', icon='DECORATE_KEYFRAME')
        
        #Botao da Passagem
        row = layout.row()
        row.operator('on.passagem_tipo', text='Breakdown', icon='DECORATE_ANIMATE')
    
        #Botao do Entre
        row = layout.row()
        row.operator('on.entre_tipo', text='Inbetween', icon='DECORATE')
        
def register():
    bpy.utils.register_class(OPERADOR_ch)
    bpy.utils.register_class(OPERADOR_ext)
    bpy.utils.register_class(OPERADOR_pss)
    bpy.utils.register_class(OPERADOR_ent)
    bpy.utils.register_class(Posetipo_Painel)
    
    
def unregister():
    bpy.utils.register_class(OPERADOR_ch)
    bpy.utils.register_class(OPERADOR_ext)
    bpy.utils.register_class(OPERADOR_pss)
    bpy.utils.register_class(OPERADOR_ent)
    bpy.utils.register_class(Posetipo_Painel)

if __name__ == "__main__":
    register()
else:
    unregister()