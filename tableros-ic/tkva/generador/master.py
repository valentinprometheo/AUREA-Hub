import pandas as pd, numpy as np, json, re, warnings, unicodedata
warnings.filterwarnings('ignore')
df=pd.read_pickle('cur.pkl')
has=lambda t: df.tags.apply(lambda l:t in l)
txt=df['Resumen por IA'].fillna('').str.lower()
NOFIT=has('No Fit')
NODEM_T=df.tipo.isin(['Inmobiliaria','Proveedor','Equipo interno','Ya cliente (postventa)'])
df['nodem']=NODEM_T|NOFIT
df['compra']=~df.nodem            # consultas de compra (incluye sin procesar)
df['convo']=df['Msgs recibidos']>=2
df['proc']=df['Resumen por IA'].notna()
df['unavez']=df['Msgs recibidos']<=1
# hot (EDFAN final: unidad concreta, compra ya/corto plazo, contado/anticipo) ; visita aparte
df['h_unidad']=df['Tokko - Propiedades interesadas'].notna()|txt.str.contains(r'unidad (\d|[a-z]\d|[a-z]-?\d)|\b\d{1,2}[a-h]\b|uf ?\d')
df['h_ya']=txt.str.contains(r'(inmediat|lo antes posible|cuanto antes|este mes|pr[oó]ximo mes|en (las )?pr[oó]ximas semanas|corto plazo|urgen|ya mismo|compra ya)')
df['h_cont']=df.var_forma_de_pago.eq('contado')|txt.str.contains(r'(contado|tiene (el )?(dinero|anticipo)|dispone de (usd|u\$s|\d))')
df['hot']=df.compra&df.proc&(df.h_unidad|df.h_ya|df.h_cont)
VIS=has('Visita Agendada')|has('Visita Realizada')
lead_visit=txt.str.contains(r'(pidi[oó]|solicit[oó]|quiere|propuso|agend|coordin[oó]|confirm[oó]|acord[oó]).{0,40}(visita|reuni[oó]n|ver (el|la) (obra|unidad|departamento|showroom))')
df['visita_pedida']=df.compra&(df.var_tipo_derivacion.eq('visita')|VIS|lead_visit)
SEG=has('En Seguimiento')|has('Derivado')|VIS|has('En Negociación')|has('Convertido')|has('No Concretado')|df.var_tipo_derivacion.notna()|has('Re-contactar más adelante')
df['seg']=SEG
df['hot_sin']=df.hot&~SEG
df['calif_sin']=df.calif_amp&~SEG
df['humana']=df.compra&(VIS|has('En Negociación')|has('Convertido')|has('No Concretado'))
C=df[df.compra]
D={}
D['total']=len(df); D['nodem']=int(df.nodem.sum()); D['compra']=len(C)
D['nodem_det']={k:int(v) for k,v in {'Inmobiliarias':(df.tipo=='Inmobiliaria').sum(),'No Fit':NOFIT.sum(),'Proveedores':(df.tipo=='Proveedor').sum(),'Ya clientes (postventa)':(df.tipo=='Ya cliente (postventa)').sum(),'Equipo interno':(df.tipo=='Equipo interno').sum()}.items()}
D['convo']=int(C.convo.sum()); D['proc']=int(C.proc.sum()); D['convo_proc']=int((C.convo&C.proc).sum())
D['sinproc']=int((C.convo&~C.proc).sum()); D['sinproc_all']=int((~C.proc).sum())
D['calif']=[int(C.calif_str.sum()),int(C.calif_amp.sum())]
D['tagcal']=int((C.tags.apply(lambda l:'Calificado' in l)).sum())
D['tagcal_ok']=int((C.tags.apply(lambda l:'Calificado' in l)&C.calif_amp).sum())
D['hot']=int(C.hot.sum()); D['hot_sin']=int(C.hot_sin.sum()); D['hot_nocal']=int((C.hot&~C.calif_amp).sum())
D['hot_sig']={'unidad':int((C.hot&C.h_unidad).sum()),'ya':int((C.hot&C.h_ya).sum()),'contado':int((C.hot&C.h_cont).sum())}
D['visita']=int(C.visita_pedida.sum()); D['visita_tag']=int((C.visita_pedida&C.tags.apply(lambda l:'Visita Agendada' in l or 'Visita Realizada' in l)).sum())
D['seg']=int(C.seg.sum()); D['calif_seg']=int((C.calif_amp&C.seg).sum()); D['calif_sin']=int(C.calif_sin.sum())
D['humana']=int(C.humana.sum())
for t in ['Visita Agendada','Visita Realizada','En Negociación','Convertido','No Concretado','En Seguimiento','Derivado','Calificado','En Conversación','Nuevo Lead','Fantasma','Re-contactar más adelante','Ya conoce a Vanesa']:
    D.setdefault('tags',{})[t]=[int(has(t).sum()),int((has(t)&df.compra).sum())]
D['conv_tipo']=df[has('Convertido')].tipo.value_counts().to_dict()
# obligatorios / sumas sobre conversaron&procesadas
B=C[C.convo&C.proc]; D['B']=len(B)
D['obl1']=int((B.proy_ok|B.zona_ok).sum()); D['obl2']=int(((B.proy_ok|B.zona_ok)&B.tip_any).sum())
D['s_fin']=int(B.s_fin.sum()); D['s_cap']=int(B.s_cap_amp.sum()); D['s_cap_str']=int(B.s_cap_str.sum()); D['s_int']=int(B.s_int.sum())
D['tip_any']=int(B.tip_any.sum()); D['proy']=int(B.proy_ok.sum()); D['zona']=int(B.zona_ok.sum())
D['cal_B']=int(B.calif_amp.sum()); D['cal_B_str']=int(B.calif_str.sum())
D['drop']=[int((~(B.proy_ok|B.zona_ok)).sum()),int(((B.proy_ok|B.zona_ok)&~B.tip_any).sum()),int((B.obl_amp&(B.sum_amp<2)).sum())]
# coverage on processed compra
P=C[C.proc]; D['P']=len(P)
cov={}
for name,col in [('Proyecto','var_proyecto_interes'),('Tipología','var_tipologia_buscada'),('Destino','var_destino'),('Objetivo búsqueda','var_objetivo_busqueda'),('Presupuesto (sin ceros)','pres'),('Forma de pago','var_forma_de_pago'),('Canal origen','var_canal_origen'),('Tipo derivación','var_tipo_derivacion'),('Barrios (Tokko)','Tokko - Barrios interesados'),('Propiedades (Tokko)','Tokko - Propiedades interesadas'),('Links (Tokko)','Tokko - Links de propiedades'),('ID Anuncio','ID Anuncio'),('Email','Email'),('Fecha visita','var_fecha_visita'),('Asesor asignado','var_asesor_asignado'),('Historial','var_historial')]:
    cov[name]=[int(P[col].notna().sum()),round(P[col].notna().mean()*100,1)]
cov['Finalidad (destino, objetivo o tag)']=[int(P.s_fin.sum()),round(P.s_fin.mean()*100,1)]
D['cov']=cov
D['pres_cero']=int((pd.to_numeric(P.var_presupuesto,errors='coerce')==0).sum())
pr=P.pres.dropna(); D['pres']=[int(len(pr)),int(pr.median()),int(pr.quantile(.25)),int(pr.quantile(.75))]
D['pres_bins']={str(k):int(v) for k,v in pd.cut(pr,[0,80000,120000,160000,200000,1e9],labels=['hasta 80 mil','80 a 120 mil','120 a 160 mil','160 a 200 mil','más de 200 mil']).value_counts().sort_index().items()}
# demanda distributions on processed compra
def dist(s,split=True):
    s=s.dropna()
    if split: s=s.str.split(r',\s*').explode().str.strip()
    return {k:int(v) for k,v in s.value_counts().items()}
D['d_proy']=dist(P.var_proyecto_interes); D['d_tip']=dist(P.var_tipologia_buscada)
D['d_tip_multi']=int(P.var_tipologia_buscada.fillna('').str.contains(',').sum())
zon=P['Tokko - Barrios interesados'].fillna('').str.replace(' y ',', ').str.split(r',\s*').explode().str.strip()
zon=zon[zon!=''].replace({'Nuñez':'Núñez','Nunez':'Núñez'}); D['d_zona']={k:int(v) for k,v in zon.value_counts().head(10).items()}; D['zona_n']=int(P['Tokko - Barrios interesados'].notna().sum())
fin=pd.Series(np.select([P.var_destino.eq('inversion')|P.var_objetivo_busqueda.eq('inversion'),P.var_destino.eq('vivienda')|P.var_objetivo_busqueda.eq('uso_personal'),P.var_destino.eq('mixto'),P.tags.apply(lambda l:'Inversor' in l),P.tags.apply(lambda l:'Consumidor final' in l)],['Inversión','Vivienda','Mixto','Inversión','Vivienda'],'') ,index=P.index)
P=P.assign(fin=fin); D['d_fin']={k:int(v) for k,v in fin[fin!=''].value_counts().items()}
D['d_pago']=dist(P.var_forma_de_pago,False); D['d_canal']=dist(P.var_canal_origen,False)
# canal origen quality (compra procesada conversó)
q=B.groupby(B.var_canal_origen.fillna('Sin dato')).agg(n=('Nombre','size'),cal=('calif_amp','sum'),cal_s=('calif_str','sum'),hot=('hot','sum'))
D['canal_q']={k:[int(r.n),int(r.cal),int(r.cal_s),int(r.hot)] for k,r in q.sort_values('n',ascending=False).iterrows()}
D['canal_nofit']={k:int(v) for k,v in df[NOFIT].var_canal_origen.fillna('Sin dato').value_counts().items()}
# project table on B
rows=[]
for p in ['Maker Núñez','Liberti','Maker Crespo','Green Line','Maker Belgrano','Drago Select']:
    m=P.var_proyecto_interes.fillna('').str.contains(p); s=P[m]; sb=s[s.convo]
    tips=s.var_tipologia_buscada.dropna(); tips=tips[~tips.str.contains(',')].value_counts()
    nf=df[NOFIT&df.var_proyecto_interes.fillna('').str.contains(p)]
    rows.append({'p':p,'n':int(len(s)),'cal':int(sb.calif_amp.sum()),'cal_s':int(sb.calif_str.sum()),'conv':int(len(sb)),'inv':int((s.fin=='Inversión').sum()),'viv':int((s.fin=='Vivienda').sum()),'fin_req':int(s.var_forma_de_pago.isin(['financiado','apto_credito']).sum()),'tip':', '.join(tips.index[:2]),'hot':int(s.hot.sum()),'nofit':int(len(nf)),'calsin':int(s.calif_sin.sum())})
D['proj']=rows; D['proy_n']=int(P.var_proyecto_interes.notna().sum())
# ads
df['ad1']=df['ID Anuncio'].fillna('').str.split(',').str[0].str.strip().replace('',np.nan)
def nm(s):
    s=unicodedata.normalize('NFKC',str(s)).replace('⁣',' ')
    s=re.sub(r'\s+',' ',s).strip(); return s
ads=[]
for aid,g in df[df.ad1.notna()].groupby('ad1'):
    gc=g[g.compra]; gb=gc[gc.convo&gc.proc]
    pj=gc.var_proyecto_interes.dropna().str.split(r',\s*').explode().value_counts()
    ads.append({'id':aid,'name':nm(g.Anuncio.iloc[0])[:90],'n':int(len(g)),'compra':int(len(gc)),'nodem':int(g.nodem.sum()),'nofit':int((g.nofit).sum()),'sinproc':int((~g.proc).sum()),'convo':int(gc.convo.sum()),'cal':int(gb.calif_amp.sum()),'cal_s':int(gb.calif_str.sum()),'hot':int(gc.hot.sum()),'unavez':int(gc.unavez.sum()),'inv':int(((gc.var_destino.eq('inversion'))|gc.var_objetivo_busqueda.eq('inversion')).sum()),'viv':int(((gc.var_destino.eq('vivienda'))|gc.var_objetivo_busqueda.eq('uso_personal')).sum()),'pj':pj.index[0] if len(pj) else '-','pj_n':int(pj.iloc[0]) if len(pj) else 0,'pj_tot':int(gc.var_proyecto_interes.notna().sum()),'fin':int(gc.var_forma_de_pago.isin(['financiado','apto_credito']).sum()),'desde':g.fecha.min().strftime('%d/%m'),'hasta':g.fecha.max().strftime('%d/%m'),'multi':int(g['ID Anuncio'].str.contains(',').sum())})
ads=sorted(ads,key=lambda a:-a['n']); D['ads']=ads
D['con_ad']=int(df.ad1.notna().sum()); D['multi_ad']=int(df['ID Anuncio'].fillna('').str.contains(',').sum())
noad=df[df.ad1.isna()]; gc=noad[noad.compra]; gb=gc[gc.convo&gc.proc]
D['noad']={'n':int(len(noad)),'compra':int(len(gc)),'nodem':int(noad.nodem.sum()),'convo':int(gc.convo.sum()),'cal':int(gb.calif_amp.sum()),'b':int(len(gb)),'hot':int(gc.hot.sum()),'unavez':int(gc.unavez.sum())}
D['ad_b']={a['id']:0 for a in ads}
for a in ads:
    g=df[(df.ad1==a['id'])&df.compra&df.convo&df.proc]; a['b']=int(len(g))
# weekly
w=df.set_index('fecha'); grp=w.groupby(pd.Grouper(freq='W-SUN'))
WK=[]
for k,g in grp:
    gc=g[g.compra]
    WK.append({'wk':(k-pd.Timedelta(days=6)).strftime('%d/%m'),'n':int(len(g)),'compra':int(len(gc)),'convo':int(gc.convo.sum()),'proc':int((gc.convo&gc.proc).sum()),'sinproc':int((gc.convo&~gc.proc).sum()),'cal':int(gc.calif_amp.sum()),'cal_s':int(gc.calif_str.sum()),'ad':int(g.ad1.notna().sum()),'noresp':int((g['Msgs enviados']==0).sum()),'nodem':int(g.nodem.sum())})
D['weeks']=WK
# gap
gap=(df.fecha>='2026-08-29')&(df.fecha<='2026-09-15')
G=df[gap]; D['gap']={'n':int(len(G)),'compra':int(G.compra.sum()),'convo':int((G.compra&G.convo).sum()),'sinproc':int((G.compra&G.convo&~G.proc).sum()),'noproc_all':int((~G.proc).sum()),'noresp':int((G['Msgs enviados']==0).sum()),'ad':int(G.ad1.notna().sum())}
# no response overall
D['noresp']=int((C['Msgs enviados']==0).sum()); D['noresp_out']=int(((C['Msgs enviados']==0)&~gap[C.index]).sum())
# monthly
M=[]
for m,g in df.groupby(df.mes.astype(str)):
    gc=g[g.compra]; gb=gc[gc.convo&gc.proc]
    days=g.fecha.dt.day.nunique() if m!='2026-07' else 10
    M.append({'m':m,'n':int(len(g)),'compra':int(len(gc)),'convo':int(gc.convo.sum()),'b':int(len(gb)),'cal':int(gb.calif_amp.sum()),'cal_s':int(gb.calif_str.sum()),'ad':int(g.ad1.notna().sum()),'nodem':int(g.nodem.sum()),'nodem_b2b':int(g.tipo.isin(['Inmobiliaria','Proveedor']).sum()),'sinproc':int((gc.convo&~gc.proc).sum()),'noresp':int((g['Msgs enviados']==0).sum()),'hot':int(gc.hot.sum()),'env':int(g['Msgs enviados'].sum())})
D['months']=M
# tags by month
TB={}
for t in ['Nuevo Lead','En Conversación','En Seguimiento','Calificado','Derivado','No Fit','Visita Agendada','Visita Realizada','En Negociación','Convertido','No Concretado']:
    TB[t]={m:int(g.tags.apply(lambda l:t in l).sum()) for m,g in df.groupby(df.mes.astype(str))}
TB['Sin tags']={m:int((g.tags.str.len()==0).sum()) for m,g in df.groupby(df.mes.astype(str))}
D['tagsm']=TB
# messages by recipient type
env=df['Msgs enviados']
D['env']={'total':int(env.sum()),'conv':int(env[df.compra&df.convo].sum()),'unavez':int(env[df.compra&~df.convo].sum()),'n_unavez':int((df.compra&~df.convo).sum()),'inmo':int(env[df.tipo=='Inmobiliaria'].sum()),'prov':int(env[df.tipo=='Proveedor'].sum()),'nofit':int(env[NOFIT].sum()),'post':int(env[df.tipo=='Ya cliente (postventa)'].sum()),'eq':int(env[df.tipo=='Equipo interno'].sum())}
o=df[df.fecha>='2026-10-01']; D['oct_env']=int(o['Msgs enviados'].sum()); D['oct_n']=len(o); D['oct_ad']=int(o.ad1.notna().sum())
# derivacion
D['deriv']=dist(C.var_tipo_derivacion,False); D['deriv_inmo_comp']=int((C.var_tipo_derivacion=='inmobiliaria').sum())
# inmobiliarias
I=df[df.tipo=='Inmobiliaria']
D['inmo']={'n':len(I),'activa':int(I.tags.apply(lambda l:'Inmobiliaria Activa' in l).sum()),'contactar':int(I.tags.apply(lambda l:'Inmobiliaria a Contactar' in l).sum()),'inmo_tag':int(I.tags.apply(lambda l:'Inmobiliaria' in l).sum()),'conv':int((I['Msgs recibidos']>=2).sum()),'env':int(I['Msgs enviados'].sum()),'jul22':int((I.fecha=='2026-07-22').sum()),'proy':dist(I.var_proyecto_interes)}
PV=df[df.tipo=='Proveedor']; D['prov']={'n':len(PV),'conv':int((PV['Msgs recibidos']>=2).sum()),'env':int(PV['Msgs enviados'].sum())}
D['nodem_m']={m['m']:[m['nodem_b2b'],m['n']] for m in M}
# no fit motives
nfm=pd.read_pickle('nofit_motivo.pkl').motivo.value_counts(); D['nofit_m']={k:int(v) for k,v in nfm.items()}
D['nofit_canal_LT']=int((NOFIT&df.var_canal_origen.eq('LT')).sum())
# LT
L=df[df.var_canal_origen.eq('LT')]; Lc=L[L.compra]; Lb=Lc[Lc.convo&Lc.proc]
D['LT']={'n':len(L),'compra':len(Lc),'b':len(Lb),'cal':int(Lb.calif_amp.sum()),'cal_s':int(Lb.calif_str.sum()),'nofit':int(L.nofit.sum()),'unavez':int(Lc.unavez.sum()),'oct':int((L.fecha>='2026-10-01').sum())}
W=df[df.var_canal_origen.eq('WhatsApp')]; Wb=W[W.compra&W.convo&W.proc]; D['WA']={'b':len(Wb),'cal':int(Wb.calif_amp.sum())}
IG=df[df.var_canal_origen.eq('Instagram')]; Ib=IG[IG.compra&IG.convo&IG.proc]; D['IG']={'b':len(Ib),'cal':int(Ib.calif_amp.sum())}
D['canal_inst']=int((df.Canal=='Instagram').sum())
# audiences
D['aud']={'hot':D['hot'],'calif':D['calif'][1],'inv':int((P.fin=='Inversión').sum()),'viv':int((P.fin=='Vivienda').sum()),'calsin':D['calif_sin'],'hotsin':D['hot_sin'],'excl':int(df.nodem.sum()),'tel':int(df['Teléfono'].notna().sum()),'mail':int(df.Email.notna().sum())}
D['email_n']=int(df.Email.notna().sum())
json.dump(D,open('D.json','w'),ensure_ascii=False,indent=1,default=int)
df.to_pickle('cur2.pkl')
