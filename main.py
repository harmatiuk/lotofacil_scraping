import collections
import requests
import pandas as pd

from collections import defaultdict
from functions import checks, clean_text



modality = 'Lotofácil'
url_base = f"https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade={modality}"

request_response = requests.get(url_base, verify=False)

request_response_text = clean_text(request_response.text)

#Create dataframe and filter NAN values
df = pd.read_html(request_response_text)
df = df[0].copy()
df = df[df['Bola1'] == df['Bola1']]

#Select only "Bola" columns
columns_name_iterator = filter(lambda x: x.startswith('Bola'), list(df.columns)) 
columns = list(columns_name_iterator)
df = df[columns].copy()


combinations = []
count_winning_numbers_dict = defaultdict(int)

for index, row in df.iterrows():
    even_number = 0
    odd_number = 0
    prime_number = 0
    
    for column in columns:
        item = int(row[column])
        response = checks(item)

        #Count Winning Numbers
        count_winning_numbers_dict[item] += 1 

        #Combinations of even, odd and prime numbers
        even_number += response['even_number']
        odd_number += response['odd_number']
        prime_number += response['prime_number']

    combination = f"{even_number} EVEN_NUM - {odd_number} ODD_NUM - {prime_number} PRIME_NUM"
    combinations.append(combination)


#Create dataframe with count combinations
counter = collections.Counter(combinations)
result = pd.DataFrame(counter.items(), columns=['Combinations', 'Frequency'])
result['p_freq'] = (result['Frequency'] / result['Frequency'].sum()*100)*100/100
result = result.sort_values(by='p_freq')

#Order count_winning_numbers_dict by frequency desc
count_winning_numbers_dict_ordered = dict(sorted(count_winning_numbers_dict.items(), key=lambda x:x[1], reverse=True))
convert_dict_to_list = list(count_winning_numbers_dict_ordered)

print(f'''
The most frequent number is:  {convert_dict_to_list[0]}

The least frequent number is: {convert_dict_to_list[-1]}

The combinations of even, odd and prime numbers is: {result['Combinations'].values[-1]} with a frequency of: {int(result['p_freq'].values[-1])}%
'''
)
