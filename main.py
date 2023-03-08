from selenium import webdriver as opcoes_Selenium
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options # Para não ficar fechando
import pandas as pd
import time

'''PARA NÂO FECHAR'''
options = Options()
options.add_experimental_option("detach", True)
'''FIM'''


navegador = opcoes_Selenium.Chrome(options=options)

# Abrindo o site di RPA
navegador.get('https://rpachallengeocr.azurewebsites.net')

time.sleep(2)

elemento_tabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elemento_tabela.find_elements(By.TAG_NAME, 'tr')

colunas = elemento_tabela.find_elements(By.TAG_NAME, 'td')

dataFrameLista = []

linha = 1

for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)

    linha = linha + 1


dataFrame = pd.DataFrame(dataFrameLista, columns=['Dados'])

arquivo_excel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivo_excel, sheet_name='Sheet1', index=True)

arquivo_excel.save()

print('CHEGOU NO FINal')