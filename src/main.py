from titanic import Titanic

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
   