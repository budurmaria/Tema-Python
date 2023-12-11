import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.figure(figsize=(10,10))
plt.plot(df.index,df['Durata'],label='Durata',marker='x')
plt.plot(df.index,df['Puls'],label='Puls',marker='x')
plt.plot(df.index,df['MaxPuls'],label='MaxPuls',marker='x')
plt.plot(df.index,df['Calorii'],label='Calorii',marker='x')
plt.title('Toate valorile')
plt.legend()

plt.figure(figsize=(10,10))
plt.plot(df['Durata'][:5],marker='x',label='Durata')
plt.plot(df['Puls'][:5],marker='x',label='Puls')
plt.title('Primele 5 Valori')
plt.legend()

ult = df[['Durata','Puls']].tail(5)
plt.figure(figsize=(10,10))
plt.plot(ult['Durata'],marker='x',label='Durata')
plt.plot(ult['Puls'],marker='x',label='Puls')
plt.title('Ultimele 5 Valori')
plt.legend()

plt.tight_layout()
plt.show()
