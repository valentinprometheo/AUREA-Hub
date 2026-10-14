import sys; sys.path.insert(0,'.')
from load import load
import pandas as pd, numpy as np, re
df=load()
has=lambda t: df.tags.apply(lambda l:t in l)
INMO=has('Inmobiliaria')|has('Inmobiliaria Activa')|has('Inmobiliaria a Contactar')
PROV=has('Proveedor'); EQ=has('Equipo'); POST=has('Cliente ya compró'); NOFIT=has('No Fit')
VARS=['var_proyecto_interes','var_tipologia_buscada','var_destino','var_objetivo_busqueda','var_forma_de_pago','var_tipo_derivacion','Tokko - Barrios interesados']
df['pres']=pd.to_numeric(df.var_presupuesto,errors='coerce'); df.loc[df.pres<=0,'pres']=np.nan
SINPROC=df['Resumen por IA'].isna()&(df.tags.str.len()==0)&df[VARS].isna().all(axis=1)
def tipo(i):
    if EQ[i]: return 'Equipo interno'
    if PROV[i]: return 'Proveedor'
    if INMO[i]: return 'Inmobiliaria'
    if POST[i]: return 'Ya cliente (postventa)'
    if SINPROC[i]: return 'Sin procesar'
    return 'Comprador'
df['tipo']=[tipo(i) for i in df.index]
ZONAS=['núñez','nuñez','nunez','belgrano','villa crespo','almagro','barracas','manzanares','liberti','drago','sarmiento','cabildo']
df['zona_ok']=df['Tokko - Barrios interesados'].fillna('').str.lower().apply(lambda s:any(z in s for z in ZONAS))
df['proy_ok']=df.var_proyecto_interes.notna()
df['tip_any']=df.var_tipologia_buscada.notna()
df['tip_single']=df.var_tipologia_buscada.fillna('').apply(lambda s: s!='' and ',' not in s)
df['s_fin']=df.var_destino.notna()|df.var_objetivo_busqueda.notna()|has('Inversor')|has('Consumidor final')
df['s_cap_str']=df.pres.notna()|df.var_forma_de_pago.isin(['financiado','apto_credito','contado'])
df['s_cap_amp']=df.s_cap_str|df.var_forma_de_pago.notna()
VIS=has('Visita Agendada')|has('Visita Realizada')
NEG=has('En Negociación')
df['s_int']=df.var_tipo_derivacion.isin(['visita','negociacion'])|VIS|NEG
df['obl_str']=df.proy_ok & df.tip_single
df['obl_amp']=(df.proy_ok|df.zona_ok) & df.tip_any
df['sum_str']=df.s_fin.astype(int)+df.s_cap_str.astype(int)
df['sum_amp']=df.s_fin.astype(int)+df.s_cap_amp.astype(int)+df.s_int.astype(int)
df['calif_str']=(df.tipo=='Comprador')&~NOFIT&df.obl_str&(df.sum_str>=2)
df['calif_amp']=(df.tipo=='Comprador')&~NOFIT&df.obl_amp&(df.sum_amp>=2)
df['nofit']=NOFIT
# hot
txt=df['Resumen por IA'].fillna('').str.lower()
df['h_visita']=df.var_tipo_derivacion.eq('visita')|VIS|txt.str.contains(r'visit|reuni[oó]n|coordinar')
df['h_unidad']=df['Tokko - Propiedades interesadas'].notna()|txt.str.contains(r'unidad\s+\w*\d|uf\s*\d|piso \d')
df['h_contado']=df.var_forma_de_pago.eq('contado')|txt.str.contains(r'contado')
df['h_neg']=df.var_tipo_derivacion.eq('negociacion')|NEG
df['hot']=(df.tipo=='Comprador')&~NOFIT&(df.h_visita|df.h_unidad|df.h_contado|df.h_neg)
human=has('Derivado')|VIS|NEG|has('Convertido')|has('No Concretado')|df.var_tipo_derivacion.notna()|has('En Seguimiento')|has('Calificado')
df['hot_sin_seg']=df.hot&~human
df['respondio']=df['Msgs recibidos']>0
df['ad']=df['ID Anuncio'].notna()
df.to_pickle('cur.pkl')
