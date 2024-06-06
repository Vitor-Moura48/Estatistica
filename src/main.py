from titanic import Titanic, inquirer

def main_menu():
        questions = [
            inquirer.List('option',
                message="Escolha uma opção",
                choices=[
                    'Calcular média', 
                    'Calcular mediana', 
                    'Calcular moda', 
                    'Calcular desvio padrão',
                    'Calcular escore z',
                    'Gráfico de dispersão com mapa de cores',
                    'Histograma',
                    'Gráfico de pizza',
                    'Gráfico dos pontos proporcionais',
                    'Gráfico de correlação entre sobrevivência e idade',
                    'Comparar Gráficos',
                    'Sair'
                ],
            ),
        ]
        answers = inquirer.prompt(questions)
        return answers['option']

if __name__ == "__main__":
    
    titanic = Titanic()
    
    while True:
        choice = main_menu()
        if choice == 'Calcular média':
            titanic.media()

        elif choice == 'Calcular mediana':
            titanic.mediana()

        elif choice == 'Calcular moda':
            titanic.moda()

        elif choice == 'Calcular desvio padrão':
            titanic.desvio_padrao()

        elif choice == 'Gráfico de dispersão com mapa de cores':
            titanic.mapa_cores('Pclass', 'Age', 'Survived')

        elif choice == 'Histograma':
            titanic.histograma()

        elif choice == 'Gráfico de pizza':
            titanic.pizza()

        elif choice == 'Calcular escore z':
            titanic.escore_z([input("Coluna filtro: "), input("Valor filtro: ")], input("Dado: "))

        elif choice == 'Gráfico dos pontos proporcionais':
            titanic.pontos_proporcionais('Age', 'Fare', 'Fare', 'Survived', 2, 'viridis')

        elif choice == 'Gráfico de correlação entre sobrevivência e idade':
            titanic.correlacao_entre_sobrevivencia_e_idade()

        elif choice == 'Comparar Gráficos':
            titanic.comparar_graficos()
            
        elif choice == 'Sair':
            print("Saindo...")
            break
        
