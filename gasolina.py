import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Carregando dados 
df = pd.read_csv("gasolina.csv")


#Gerando gráfico linha 
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))
sns.lineplot(x="dia", y="venda", data=df, marker="o", color="b", linewidth=2.5)
plt.title("Valor da Gasolina por Dia")
plt.xlabel("Dia")
plt.ylabel("Venda")
plt.grid(True)
plt.tight_layout()


#Salvando grafico em PNG
plt.savefig("gasolina.png")