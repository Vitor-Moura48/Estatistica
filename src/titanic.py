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

        ordenados = self.df.sort_values(by=coluna)
        plt.hist(ordenados[coluna], bins=8)
        plt.title(f"Histograma {coluna}")
        plt.show()
    
    def pizza(self, coluna):

        contagem = self.df[coluna].value_counts().to_dict()

        plt.pie(contagem.values(), labels=contagem.keys(), shadow=True, startangle=90, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title(f"Proporções {coluna}")
        plt.show()

    def mapa_cores(df, x_col, y_col, color_col, cmap='viridis'):

        x = df[x_col]
        y = df[y_col]
        colors = df[color_col]


        plt.scatter(x, y, c=colors, cmap=cmap)
        plt.colorbar()
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'Dispersão de {x_col} vs {y_col} com mapa de cores de {color_col}')
        plt.show()

    
    data = {
       'x': np.random.randint(1, 20, 15),
        'y': np.random.randint(80, 120, 15),
        'valor': np.random.randint(0, 100, 15)
    }
    df = pd.DataFrame(data)
    mapa_cores(df, 'x', 'y', 'valor')