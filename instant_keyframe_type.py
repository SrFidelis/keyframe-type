bl_info = {
    "name": "PoseTipo",
    "author": "Canal CGI Brasil - Vínicius S. Fidelis",
    "link": "http://bit.ly/2PUonQv",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "api": 35853,
    "location": "View3D > Nkey Panel > Animate -> PoseTipo",
    "description": "Cria keyframes com o tipo determinado",
    "warning": "",
    "category": "Animation"}

import bpy
from bpy.types import Panel

#bpy.ops.anim.keying_set_active_set(type='LocRotScale') #Definir Keying por padrão

def registrar(nome): #Função para registrar classes
    bpy.utils.register_class(nome)


class OPERADOR_ch(bpy.types.Operator): #Operador da chave
    bl_label = 'chave'
    bl_idname = 'on.chave_tipo'
    bl_description = 'Keyframe como Chave'

    def execute(self, context): #Função que define como chave e cria keyframe
        bpy.context.scene.tool_settings.keyframe_type = 'KEYFRAME' #Definindo como Chave
        bpy.ops.anim.keyframe_insert() #Criando o keyframe
        
        return {'FINISHED'}

registrar(OPERADOR_ch) #Registrando a classe acima



class OPERADOR_ext(bpy.types.Operator): #Operador do extremo
    bl_label = 'extremo'
    bl_idname = 'on.extremo_tipo'
    bl_description = 'Keyframe como Extremo'

    def execute(self, context): #Função que define como extremo e cria keyframe
        bpy.context.scene.tool_settings.keyframe_type = 'EXTREME' #Definindo como Extremo
        bpy.ops.anim.keyframe_insert() #Criando o keyframe
        
        return {'FINISHED'}

registrar(OPERADOR_ext) #Registrando a classe acima


class OPERADOR_pss(bpy.types.Operator): #Operador da passagem
    bl_label = 'passagem'
    bl_idname = 'on.passagem_tipo'
    bl_description = 'Keyframe como Passagem'

    def execute(self, context): #Função que define como passagem e cria keyframe
        bpy.context.scene.tool_settings.keyframe_type = 'BREAKDOWN' #Definindo como Passagem
        bpy.ops.anim.keyframe_insert() #Criando o keyframe
        
        return {'FINISHED'}

registrar(OPERADOR_pss) #Registrando a classe acima


class OPERADOR_ent(bpy.types.Operator): #Operador do entre
    bl_label = 'entre'
    bl_idname = 'on.entre_tipo'
    bl_description = 'Keyframe como Entre'

    def execute(self, context): #Função que define como entre e cria keyframe
        bpy.context.scene.tool_settings.keyframe_type = 'JITTER' #Definindo como Entre
        bpy.ops.anim.keyframe_insert() #Criando o keyframe
        
        return {'FINISHED'}

registrar(OPERADOR_ent) #Registrando a classe acima

# UI - COMO E ONDE VAI APARECER NO BLENDER
class PosetipoPainel(Panel): #Aparencia no programa
    bl_label = "PoseTipo"
    bl_idname = "VIEW3D_PT_posetipo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animate"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        #Texto Lembre-se
        row = layout.row()
        row.label(text="Lembre-se do Keying", translate=True, icon='ERROR')
        
        #Botão da Chave
        row = layout.row()
        row.operator('on.chave_tipo', text='Chave', icon='MESH_CIRCLE')
        
        #Botao do Extremo
        row = layout.row()
        row.operator('on.extremo_tipo', text='EXTREMO', icon='DECORATE_KEYFRAME')
        
        #Botao da Passagem
        row = layout.row()
        row.operator('on.passagem_tipo', text='Passagem', icon='DECORATE_ANIMATE')
    
        #Botao do Entre
        row = layout.row()
        row.operator('on.entre_tipo', text='Entre', icon='DECORATE')
        
registrar(PosetipoPainel) #Registro da classe da aparencia no programa
