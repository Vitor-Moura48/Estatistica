import sys, os, matplotlib, numpy, pandas

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # adiciona as pastas fora de src no caminho python
import recursos

# média dos que sobreviveram V
# mediana da idade dos que sobreviveram
# moda da idade dos que sobreviveram
# desvio padrão
# gráfico
# dristriuição normal

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

    print(media_vivos)
    print(media_mortos)
    print(mediana_vivos)
    print(mediana_mortos)
    print(moda_vivos)
    print(moda_mortos)
