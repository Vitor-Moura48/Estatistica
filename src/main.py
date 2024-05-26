import sys, os, numpy, pandas
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # adiciona as pastas fora de src no caminho python

# média dos que sobreviveram (V)
# mediana da idade dos que sobreviveram (V)
# moda da idade dos que sobreviveram (V)
# desvio padrão (V)
# gráfico
# distribuição normal

if __name__ == "__main__":
    df = pandas.read_csv("recursos/titanic.csv")

    vivos = df.loc[df['Survived'] == 1]
    mortos = df.loc[df['Survived'] == 0]

    media_vivos = round(vivos['Age'].mean(), 2)
    media_mortos = round(mortos['Age'].mean(), 2)

    mediana_vivos = round(vivos['Age'].median(), 2)
    mediana_mortos = round(mortos['Age'].median(), 2)

    moda_vivos = round(vivos["Age"].mode().values[0])
    moda_mortos = round(mortos["Age"].mode().values[0])
    
    desvio_padrao_idade_vivos = vivos['Age'].std().round(3)
    desvio_padrao_idade_mortos = mortos['Age'].std().round(3)

    print(media_vivos)
    print(media_mortos)
    print(mediana_vivos)
    print(mediana_mortos)
    print(moda_vivos)
    print(moda_mortos)
    print(desvio_padrao_idade_vivos)
    print(desvio_padrao_idade_mortos)

    i = df.sort_values(by='Age')
    plt.hist(i['Age'], bins=8, label='Histograma Idades')
    plt.show()