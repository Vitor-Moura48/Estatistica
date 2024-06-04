from titanic import Titanic
import inquirer

# média dos que sobreviveram (V)
# mediana da idade dos que sobreviveram (V)
# moda da idade dos que sobreviveram (V)
# desvio padrão (V)
# gráfico
# distribuição normal

if __name__ == "__main__":
    
    titanic = Titanic()

    titanic.media(['Survived', 1], 'Age')
    titanic.media(['Survived', 0], 'Age')

    titanic.moda(['Survived', 1], 'Age')
    titanic.moda(['Survived', 0], 'Age')

    titanic.mediana(['Survived', 1], 'Age')
    titanic.mediana(['Survived', 0], 'Age')

    titanic.desvio_padrao(['Survived', 1], 'Age')
    titanic.desvio_padrao(['Survived', 0], 'Age')

    titanic.histograma('Age')

    titanic.pizza("Pclass")
   
def main_menu():
    questions = [
        inquirer.List('option',
            message="Escolha uma opção",
            choices=[
                'Calcular média dos que sobreviveram', 
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

def main():
    titanic = Titanic()
    while True:
        choice = main_menu()
        if choice == 'Calcular média dos que sobreviveram':
            titanic.media(['Survived', 1], 'Age')
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

if __name__ == "__main__":
    main()