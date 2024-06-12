import sys
import os
import pandas as pd
import inquirer
import seaborn as sns
from scipy.stats import norm
from scipy import stats
from colorama import Fore

import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # adiciona as pastas fora de src no caminho python

class Titanic:
    def __init__(self):
        self.df = pd.read_csv("recursos/titanic.csv")
        self.df = self.df.dropna(how='any') 

    def filtrar_df2(self, filtro):
        if type(filtro[1]) == str:
            filtro[1] = int(filtro[1]) if filtro[1].isdigit() else filtro[1]
        return self.df.loc[self.df[filtro[0]] == filtro[1]]

    def obter_filtro(self):
        coluna_filtro = self.colunas_menu("Escolha uma coluna de filtro")
        valor_filtro = self.atributo_menu(coluna_filtro) 
        return coluna_filtro, valor_filtro
    
    def filtrar_df(self, coluna, valor):
        if type(valor) == str:
            valor = int(valor) if valor.isdigit() else valor
        df_filtrado = self.df.loc[self.df[coluna] == valor]
        return df_filtrado
    
    def media(self):
        try:
            coluna_filtro, valor_filtro = self.obter_filtro()
            df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
            coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
            media = round(df_filtrado[coluna].mean(), 2)
            print(f"{Fore.GREEN}média {coluna} onde {coluna_filtro} == {valor_filtro}: {media} {Fore.RESET}\n\n")
            return media
        except Exception as e:
            print(f"{Fore.RED}Erro ao calcular a média: {e}{Fore.RESET}\n\n")
    
    def moda(self):
        try:
            coluna_filtro, valor_filtro = self.obter_filtro()
            df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
            coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
            moda = df_filtrado[coluna].mode().values[0]
            print(f"{Fore.GREEN}moda {coluna} onde {coluna_filtro} == {valor_filtro}: {moda} {Fore.RESET}\n\n")
            return moda
        except Exception as e:
            print(f"{Fore.RED}Erro ao calcular a moda: {e}{Fore.RESET}\n\n")
    
    def mediana(self):
        try:
            coluna_filtro, valor_filtro = self.obter_filtro()
            df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
            coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
            mediana = round(df_filtrado[coluna].median(), 2)
            print(f"{Fore.GREEN}mediana {coluna} onde {coluna_filtro} == {valor_filtro}: {mediana} {Fore.RESET}\n\n")
            return mediana
        except Exception as e:
            print(f"{Fore.RED}Erro ao calcular a mediana: {e}{Fore.RESET}\n\n")

    def desvio_padrao(self):
        try:
            coluna_filtro, valor_filtro = self.obter_filtro()
            df_filtrado = self.filtrar_df(coluna_filtro, valor_filtro)
            coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
            desvio_padrao = df_filtrado[coluna].std().round(3)
            print(f"{Fore.GREEN}desvio_padrao {coluna} onde {coluna_filtro} == {valor_filtro}: {desvio_padrao} {Fore.RESET}\n\n")
            return desvio_padrao
        except Exception as e:
            print(f"{Fore.RED}Erro ao calcular o desvio padrão: {e}{Fore.RESET}\n\n")

    def histograma(self):
        try:
            coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
            ordenados = self.df.sort_values(by=coluna)
            plt.hist(ordenados[coluna], bins=8)
            plt.title(f"Histograma {coluna}")
            plt.show()
        except Exception as e:
            print(f"{Fore.RED}Erro ao gerar o histograma: {e}{Fore.RESET}\n\n")
    
    def pizza(self):
        try:
            df = pd.read_csv("recursos/titanic.csv")
            coluna = self.colunas_menu("Escolha a coluna que deseja analizar")
            contagem = df[coluna].value_counts().to_dict()
            plt.pie(contagem.values(), labels=contagem.keys(), shadow=True, startangle=90, autopct='%1.1f%%')
            plt.axis('equal')
            plt.title(f"Proporções {coluna}")
            plt.show()
        except Exception as e:
            print(f"{Fore.RED}Erro ao gerar o gráfico de pizza: {e}{Fore.RESET}\n\n")

    def mapa_cores(self, x_col, y_col, color_col, cmap='viridis'):
        try:
            x = self.df[x_col]
            y = self.df[y_col]
            colors = self.df[color_col]
            plt.scatter(x, y, c=colors, cmap=cmap)
            plt.colorbar()
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f'Dispersão de {x_col} vs {y_col} com mapa de cores de {color_col}')
            plt.show()
        except Exception as e:
            print(f"{Fore.RED}Erro ao gerar o mapa de cores: {e}{Fore.RESET}\n\n")

    def pontos_proporcionais(self, x_col='Age', y_col='Fare', size_col='Fare', color_col='Survived', scale_factor=2, cmap='viridis'):
        try:
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
        except Exception as e:
            print(f"{Fore.RED}Erro ao gerar o gráfico de pontos proporcionais: {e}{Fore.RESET}\n\n")

    def escore_z(self, filtro, coluna):
        try:
            df_filtrado = self.filtrar_df2(filtro)
            coluna_nova = df_filtrado.dropna(subset=[coluna])
            lista_df_filtrados = coluna_nova[coluna].tolist()
           
            z_escore = stats.zscore(lista_df_filtrados)
            
            print(f"{Fore.GREEN}z_escore {coluna} onde {filtro[0]} == {filtro[1]}: {z_escore} {Fore.RESET}\n\n")
            return z_escore
        except Exception as e:
            print(f"{Fore.RED}Erro ao calcular o escore z: {e}{Fore.RESET}\n\n")

    def correlacao_entre_sobrevivencia_e_idade(self):
        try:
            df_filtrado = self.df.dropna(subset=['Age'])  
            df_filtrado = df_filtrado[['Survived', 'Age']] 

            correlacao = df_filtrado['Survived'].corr(df_filtrado['Age'])

            plt.figure(figsize=(10, 8))
            sns.regplot(data=df_filtrado, x='Age', y='Survived')
            plt.title(f'Correlação de Pearson entre Survived e Age: {correlacao:.2f}')
            plt.xlabel('Age')
            plt.ylabel('Survived')
            plt.show()

            return correlacao
        except Exception as e:
            print(f"{Fore.RED}Erro ao calcular a correlação: {e}{Fore.RESET}\n\n")

    def comparar_graficos(self):
        while True:
            try:
                questions = [
                    inquirer.List(
                        'choice',
                        message="Escolha o gráfico que deseja visualizar",
                        choices=[
                            ('Mapa de Cores (Pclass, Age, Survived)', '1'),
                            ('Pontos Proporcionais (Age, Fare, Fare, Survived)', '2'),
                            ('Correlação entre Sobrevivência e Idade', '3'),
                            ('Histograma', '4'),
                            ('Gráfico de Pizza', '5'),
                            ('Sair', '0')
                        ],
                    )
                ]
                
                answers = inquirer.prompt(questions)
                choice = answers['choice']

                if choice == '1':
                    self.mapa_cores('Pclass', 'Age', 'Survived')
                elif choice == '2':
                    self.pontos_proporcionais('Age', 'Fare', 'Fare', 'Survived', 2, 'viridis')
                elif choice == '3':
                    self.correlacao_entre_sobrevivencia_e_idade()
                elif choice == '4':
                    self.histograma()
                elif choice == '5':
                    self.pizza()
                elif choice == '0':
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Por favor, escolha um número válido.")
            except Exception as e:
                print(f"{Fore.RED}Erro ao comparar gráficos: {e}{Fore.RESET}\n\n")

    def colunas_menu(self, texto):
        try:
            questions = [
                    inquirer.List('option',
                        message=texto,
                        choices=self.df.keys().tolist(),
                    ),
                ]
            answers = inquirer.prompt(questions)
            return answers['option']
        except Exception as e:
            print(f"{Fore.RED}Erro ao exibir o menu de colunas: {e}{Fore.RESET}\n\n")

    def atributo_menu(self, coluna):
        try:
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
        except Exception as e:
            print(f"{Fore.RED}Erro ao exibir o menu de atributos: {e}{Fore.RESET}\n\n")
