import sys, os, numpy, pandas
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # adiciona as pastas fora de src no caminho python

class Titanic:
    def __init__(self):
        self.df = pandas.read_csv("recursos/titanic.csv")
    
    def filtrar_df(self, filtro):
        return self.df.loc[self.df[filtro[0]] == filtro[1]]
    
    def media(self, filtro, coluna):

        df_filtrado = self.filtrar_df(filtro)

        media = round(df_filtrado[coluna].mean(), 2)

        print(f"média {coluna} onde {filtro[0]} == {filtro[1]}: {media}")
        return media

    
    def moda(self, filtro, coluna):

        df_filtrado = self.filtrar_df(filtro)

        moda = round(df_filtrado[coluna].mode().values[0])
        
        print(f"moda {coluna} onde {filtro[0]} == {filtro[1]}: {moda}")
        return moda
    
    def mediana(self, filtro, coluna):

        df_filtrado = self.filtrar_df(filtro)

        mediana = round(df_filtrado[coluna].median(), 2)

        print(f"mediana {coluna} onde {filtro[0]} == {filtro[1]}: {mediana}")
        return mediana

    def desvio_padrao(self, filtro, coluna):

        df_filtrado = self.filtrar_df(filtro)

        desvio_padrao = df_filtrado[coluna].std().round(3)

        print(f"desvio_padrao {coluna} onde {filtro[0]} == {filtro[1]}: {desvio_padrao}")
        return desvio_padrao

    def histograma(self, coluna):
        i = self.df.sort_values(by=coluna)
        plt.hist(i[coluna], bins=8, label="Histograma")
        plt.show()