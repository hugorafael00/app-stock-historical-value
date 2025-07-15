import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.DataFrame({
    'idade': [20 , 23, 45, 31],
    'nome'  : ['joao', 'maria', 'jose', 'ferreira' ]
})

plt.hist(tabela['idade'])