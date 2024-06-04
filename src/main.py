from titanic import Titanic, inquirer

def main_menu():
        questions = [
            inquirer.List('option',
                message="Escolha uma opção",
                choices=[
                    'Calcular média', 
                    'Calcular mediana da idade dos que sobreviveram', 
                    'Calcular moda da idade dos que sobreviveram', 
                    'Calcular desvio padrão da idade dos que sobreviveram', 
                    'Gerar gráfico de dispersão com mapa de cores',
                    'Mostrar histograma da idade',
                    'Mostrar gráfico de pizza para classe',
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
            titanic.media([input("Coluna filtro: "), input("Valor filtro: ")], input("Atributo alvo: "))
        elif choice == 'Calcular mediana da idade dos que sobreviveram':
            titanic.mediana(['Survived', 1], 'Age')
        elif choice == 'Calcular moda da idade dos que sobreviveram':
            titanic.moda(['Survived', 1], 'Age')
        elif choice == 'Calcular desvio padrão da idade dos que sobreviveram':
            titanic.desvio_padrao(['Survived', 1], 'Age')
        elif choice == 'Gerar gráfico de dispersão com mapa de cores':
            titanic.mapa_cores('Pclass', 'Age', 'Survived')
        elif choice == 'Mostrar histograma da idade':
            titanic.histograma('Age')
        elif choice == 'Mostrar gráfico de pizza para classe':
            titanic.pizza('Pclass')
        elif choice == 'Sair':
            print("Saindo...")
            break
