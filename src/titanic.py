import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import inquirer
import seaborn as sns
from scipy.stats import norm
from colorama import Fore

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # adiciona as pastas fora de src no caminho python

class Titanic:
    def __init__(self):
        self.df = pd.read_csv("recursos/titanic.csv")
    
    def filtrar_df(self, filtro):
        if type(filtro[1]) == str:
            filtro[1] = int(filtro[1]) if filtro[1].isdigit() else filtro[1]
        return self.df.loc[self.df[filtro[0]] == filtro[1]]
    
    def media(self, filtro, coluna):
        df_filtrado = self.filtrar_df(filtro)
        media = round(df_filtrado[coluna].mean(), 2)
        print(f"{Fore.GREEN}média {coluna} onde {filtro[0]} == {filtro[1]}: {media} {Fore.RESET}\n\n")
        return media
    
    def moda(self, filtro, coluna):
        df_filtrado = self.filtrar_df(filtro)
        moda = round(df_filtrado[coluna].mode().values[0])
        print(f"{Fore.GREEN}moda {coluna} onde {filtro[0]} == {filtro[1]}: {moda} {Fore.RESET}\n\n")
        return moda
    
    def mediana(self, filtro, coluna):
        df_filtrado = self.filtrar_df(filtro)
        mediana = round(df_filtrado[coluna].median(), 2)
        print(f"{Fore.GREEN}mediana {coluna} onde {filtro[0]} == {filtro[1]}: {mediana} {Fore.RESET}\n\n")
        return mediana

    def desvio_padrao(self, filtro, coluna):
        df_filtrado = self.filtrar_df(filtro)
        desvio_padrao = df_filtrado[coluna].std().round(3)
        print(f"{Fore.GREEN}desvio_padrao {coluna} onde {filtro[0]} == {filtro[1]}: {desvio_padrao} {Fore.RESET}\n\n")
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

    def mapa_cores(self, x_col, y_col, color_col, cmap='viridis'):
        x = self.df[x_col]
        y = self.df[y_col]
        colors = self.df[color_col]
        plt.scatter(x, y, c=colors, cmap=cmap)
        plt.colorbar()
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'Dispersão de {x_col} vs {y_col} com mapa de cores de {color_col}')
        plt.show()

    def pontos_proporcionais(self, x_col='Age', y_col='Fare', size_col='Fare', color_col='Survived', scale_factor=2, cmap='viridis'):
        filtered_data = self.df.dropna(subset=[x_col, y_col, size_col])
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(
            x=filtered_data[x_col],
            y=filtered_data[y_col],
            s=filtered_data[size_col] * scale_factor,
            c=filtered_data[color_col],
            cmap=cmap,
            alpha=0.6,
            edgecolors='w',
            linewidth=0.5
        )
        plt.colorbar(scatter, label=color_col)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'{y_col} vs {x_col} (Tamanho do ponto proporcional a {size_col})')
        plt.show()
