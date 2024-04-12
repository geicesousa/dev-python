import requests # para fazer uma req
import json 

# Sua chave previsao_do_tempo 763f2190 
# "str" \
# + "str" # para strings muito longas podemos dar Enter após a barra que concatena
print('Teste ' \
      + 'de concatenação')

### fazer verificações com try e except
### desafio: perguntar se o usuário deseja ver a previsão de outros dias


def get_coordinates(): 
    ''' pega as coordenadas de acordo 
    com a localização do ip'''
    
    geoplugin = requests.get('http://www.geoplugin.net/json.gp')

    response = json.loads(geoplugin.text) # converte o json da resposta em um dicionário

    if response['geoplugin_status'] != 200:
        return 'Não foi possível acessar a sua localização. Tente novamente em alguns instantes.'
    else: 
        number_ip = response['geoplugin_request']
        print(number_ip)
        return number_ip

def get_city_name():
    ''' pede a pessoa para digitar uma cidade,estado 
    e retorna o valor'''

    city_name = input('digite o nome da cidade e estado que deseja saber a previsão (Salvador,BA): ')
    return str(city_name)

def verify_forecast(id):
    ''' pede um id para verificar a cidade escolhida
     comentado abaixo tem outras possibilidades de conseguir 
      a previsão '''
    # hg_weather = requests.get(f'https://api.hgbrasil.com/weather?woeid={id}') # para pegar as informações climáticas de acordo com o identificador fornecido pelo site
    # hg_weather_ip = requests.get(f'https://api.hgbrasil.com/weather?key={key}&user_ip={id}') # para pegar as informações climáticas de acordo com a localização

    hg_weather_city = requests.get(f'https://api.hgbrasil.com/weather?key=763f2190&city_name={id}')

    response = json.loads(hg_weather_city.text)

    city_chosen = response['results']['city']
    forecast_today = response['results']['forecast'][0]

    return f''' Você escolheu a cidade {city_chosen}, a previsão para hoje - dia {forecast_today['date']}, {forecast_today['weekday']} - é de {forecast_today['description']}, temperatura MAX: {forecast_today['max']}ºC/MIN: {forecast_today['min']}ºC
    '''

#início da execução

coordinates = get_coordinates()
city = get_city_name()
key = '763f2190'
id_woeid = 455826

print()
print(verify_forecast(city))

def verify_forecast_week(id):

    hg_weather_city = requests.get(f'https://api.hgbrasil.com/weather?key=763f2190&city_name={id}')

    response = json.loads(hg_weather_city.text)

    city_chosen = response['results']['city']
    forecast_today = response['results']['forecast']

    print(f'Previsão para {city_chosen}: ')

    for i in range(len(forecast_today)):

        print( f'''Data: {forecast_today[i]['date']},
    Dia: {forecast_today[i]['weekday']}
    Condição climática: {forecast_today[i]['description']}, 
    Temperatura MAX: {forecast_today[i]['max']}ºC
    Temperatura MIN: {forecast_today[i]['min']}ºC
    ''')

print()
verify_forecast_week(city)
