import pandas as pd, numpy as np
def load():
    df=pd.read_excel('/root/.claude/uploads/5cace1cd-6515-5715-a2db-3fed9a0ee26e/88cf89c0-contactos_3.xlsx',dtype=str)
    df=df.replace({'-':np.nan,'':np.nan})
    df['fecha']=pd.to_datetime(df['Fecha'],format='%d/%m/%Y',errors='coerce')
    df['mes']=df['fecha'].dt.to_period('M')
    df['tags']=df['Tags'].fillna('').apply(lambda s:[t.strip() for t in s.split(',') if t.strip()])
    for c in ['Msgs enviados','Msgs recibidos','Reuniones']: df[c]=pd.to_numeric(df[c],errors='coerce')
    return df
