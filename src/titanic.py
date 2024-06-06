import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import inquirer
from scipy.stats import norm
from scipy import stats
from colorama import Fore

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # adiciona as pastas fora de src no caminho python

class Titanic:
    def __init__(self):
        self.df = pd.read_csv("recursos/titanic.csv")

    def obter_filtro(self):
        coluna_filtro = self.colunas_menu("Escolha uma coluna de filtro")
        valor_filtro = self.atributo_menu(coluna_filtro) 
        return coluna_filtro, valor_filtro
    
    def filtrar_df(self, coluna, valor):
        if type(valor) == str:
            valor = int(valor) if valor.isdigit() else valor
        return self.df.loc[self.df[coluna] == valor]
    
    def media(self):
        coluna_filtro, valor_filtro = self.obter_filtro()
        df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
        coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
        media = round(df_filtrado[coluna].mean(), 2)
        print(f"{Fore.GREEN}média {coluna} onde {coluna_filtro} == {valor_filtro}: {media} {Fore.RESET}\n\n")
        return media
    
    def moda(self):
        coluna_filtro, valor_filtro = self.obter_filtro()
        df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
        coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
        moda = df_filtrado[coluna].mode().values[0]
        print(f"{Fore.GREEN}moda {coluna} onde {coluna_filtro} == {valor_filtro}: {moda} {Fore.RESET}\n\n")
        return moda
    
    def mediana(self):
        coluna_filtro, valor_filtro = self.obter_filtro()
        df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
        coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
        mediana = round(df_filtrado[coluna].median(), 2)
        print(f"{Fore.GREEN}mediana {coluna} onde {coluna_filtro} == {valor_filtro}: {mediana} {Fore.RESET}\n\n")
        return mediana

    def desvio_padrao(self):
        coluna_filtro, valor_filtro = self.obter_filtro()
        df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
        coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
        desvio_padrao = df_filtrado[coluna].std().round(3)
        print(f"{Fore.GREEN}desvio_padrao {coluna} onde {coluna_filtro} == {valor_filtro}: {desvio_padrao} {Fore.RESET}\n\n")
        return desvio_padrao

    def histograma(self):
        coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
        ordenados = self.df.sort_values(by=coluna)
        plt.hist(ordenados[coluna], bins=8)
        plt.title(f"Histograma {coluna}")
        plt.show()
    
    def pizza(self):
        coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
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

    def escore_z(self, filtro, coluna):
        df_filtrado = self.filtrar_df(filtro)
        coluna_nova = df_filtrado.dropna(subset=[coluna])
        lista_df_filtrados = coluna_nova[coluna].tolist()
       
        z_escore = stats.zscore(lista_df_filtrados)
        
        print(f"{Fore.GREEN}z_escore {coluna} onde {filtro[0]} == {filtro[1]}: {z_escore} {Fore.RESET}\n\n")
        return z_escore

    def colunas_menu(self, texto):
        questions = [
                inquirer.List('option',
                    message=texto,
                    choices=self.df.keys().tolist(),
                ),
            ]
        answers = inquirer.prompt(questions)
        return answers['option']

    def atributo_menu(self, coluna):
        escolhas = self.df[coluna].unique().tolist()
        escolhas.append('*Sem condição*')
        questions = [
                inquirer.List('option',
                    message="Escolha um dado",
                    choices=escolhas
                ),
            ]
        answers = inquirer.prompt(questions)
        
        return True if answers['option'] == '*Sem condição*' else answers['option']