import requests_html, requests, telebot, re, json
import random
import string
import string
from random import *
from time import sleep

bot = telebot.TeleBot("1569295230:AAGXCswZR9diSERdg66WXQTDZDYckfur5CM")

PRIVADO = []

###################################

GRUPO = []

###################################

EXCEPT = []


@bot.message_handler(commands=['start'])
def boavinda(message1):
    ide = message1.chat.id
    liste = PRIVADO + GRUPO + EXCEPT
    if ide in liste:

        bot.reply_to(message1, '<b>' '😎 OBA, VOCÊ TEM ACESSO! 😎' '</b>', parse_mode='HTML')
        bot.send_message(ide, '✅ ' '<b>' 'use ' '</b>''<code>' '/menu' '</code>''<b>' ' e veja os comandos' '</b>' ' ✅', parse_mode='HTML')
    
    else:
        bot.reply_to(message1, '<b>' + '🚫 ' + '@'+message1.chat.username + ' VOCÊ NÃO TEM ACESSO! 🚫' '</b>', parse_mode='HTML')
        bot.send_message(ide, '<b>' '✅ Adquira acesso com meu pai @DKZINNBR ✅' '</b>', parse_mode='HTML')
                		
################################################

session = requests_html.HTMLSession()

################################################

# CONSULTA DE BIN #

@bot.message_handler(commands=['bin'] + ['BIN'])
def lbz(men):
            notbin = []
            bid = men.chat.id
            cp = men.text
            if bid in notbin:
                bot.reply_to(men, '⚠ 𝙘𝙤𝙣𝙨𝙪𝙡𝙩𝙖 𝙙𝙚 𝙗𝙞𝙣 𝙙𝙚𝙨𝙖𝙩𝙞𝙫𝙖𝙙𝙖 𝙥𝙖𝙧𝙖 𝙚𝙨𝙩𝙚 𝙜𝙧𝙪𝙥𝙤 ⚠')
            else:
                try:
                    bn = re.sub('[^0-9]', '', cp)
                    response = requests.get('https://binlist.io/lookup/{}'.format(bn))
                    res = response.content
                    r = json.loads(res)
                    if str(r['success']) == str('True'):

                        bot.reply_to(men, '\n         ㅤ   ㅤ<b>🔍 DADOS BIN 🔎</b>\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n<b>• BIN</b>: ' + '<code>' + str(
                            r['number']['iin']) + '</code>' + '\n' +
                                     '<b>• BANDEIRA</b>: ' + '<code>' + str(r['scheme']) + '</code>' + '\n' +
                                     '<b>• TIPO</b>: ' + '<code>' + str(r['type']) + '</code>' + '\n' +
                                     '<b>• NÍVEL</b>: ' + '<code>' + str(r['category']) + '</code>' + '\n' +
                                     '<b>• BANCO</b>: ' + '<code>' + str(r['bank']['name']) + '</code>' + '\n' +
                                     '<b>• TEL BANCO</b>: ' + '<code>' + str(r['bank']['phone']) + '</code>' + '\n' +
                                     '<b>• URL</b>: ' + str(r['bank']['url']) + '\n' +
                                     '<b>• PAÍS</b>: ' + '<code>' + str(r['country']['name']) + '</code>' + '\n' +
                                     '<b>• ID</b>: ' + '<code>' + str(r['country']['alpha3']) + '</code>' + '\n' +
                                     '<b>• SIGLA</b>: ' + '<code>' + str(r['country'][
                                                               'alpha2']) + '</code>' + '\n' +  '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n<b>• GRUPO: @dkbuscas' + '\n' + '• GRUPO²: @dkbuscas3' + '\n' + '• CANAL: @dkzrefe' + '</b>', parse_mode='HTML')
                    else:
                        bot.reply_to(men, '<b>VEJA O EXEMPLO</b>: "' + '<code>' + '/bin 651652' + '</code>' + '"', parse_mode='HTML')
                except:
                    bot.reply_to(men, '<b>⚠ DIGITE UMA BIN VIADO ⚠</b>', parse_mode='HTML')

################################################

# CONSULTA DE CEP #

@bot.message_handler(commands=['cep'] + ['CEP'])
def bno(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/cep':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CEP ⚠' + '</b>', parse_mode='HTML')
    if men.text == '/CEP':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CEP ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ipp = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cep/search/' + ipp + '?token=4f8d9149be4858c837b8b38f5c0d194a')
        	reqi = url.json
        	bot.reply_to(men, '<b>' 'ㅤ🔍 CONSULTA DE CEP 🔎' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• CEP: ' '</b>' '<code>' + ipp + '</code>' '\n' + '<b>' '• UF: ' '</b>' '<code>' + reqi()['data']['state'] + '</code>' '\n' + '<b>' '• ESTADO: ' '</b>' '<code>' + reqi()['data']['state_name'] + '</code>' '\n' + '<b>' '• CIDADE: ' '</b>' '<code>' + reqi()['data']['city'] + '</code>' '\n\n' + '<b>' '• LOGRADOURO: ' '</b>' '<code>' + reqi()['data']['address'] + '</code>' '\n' + '<b>' '• BAIRRO: ' '</b>' '<code>' + reqi()['data']['district'] + '</code>' '\n' + '<b>' '• NAME: ' '</b>' '<code>' + reqi()['data']['address_name'] + '</code>' '\n' + '<b>' '• IBGE: ' '</b>' '<code>' + reqi()['data']['city_code'] + '</code>' '\n' + '<b>' '• STATUS: ' '</b>' '<code>' + reqi()['data']['status'] + '</code>' '\n' + '<b>' '• MENSAGEM: ' '</b>' '<code>' + reqi()['data']['message'] + '</code>' '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• GRUPO: @dkbuscas' + '\n' + '• GRUPO²: @dkbuscas2' + '\n' + '• CANAL: @dkzrefe' + '</b>', parse_mode='HTML')
        except:
                   bot.reply_to(men, '<b>' + 'OPS, TA ERRADO ;(' + '</b>', parse_mode='HTML')

################################################

# MENU DO BOT #

@bot.message_handler(commands=['menu'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠ ERRADO SEU VIADO ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	bot.reply_to(men, '<b>' '🔍 MENU DO BOT 🔎' '</b>' + '\n\n' + '<b>' '[+] CEP:</b><code> /cep 89874000' '</code>' + '\n' + '<b>' '[+] BIN:</b><code> /bin 545323' + '</code>' '\n' + '<b>' '[+] CNPJ:</b><code> /cnpj 27865757000102' + '</code>' '\n' + '<b>' '[+] CPF: ' '</b>''<code>' '/cpf 29993559806' '</code>' + '\n' + '<b>' '[+] TRABALHOS: ' '</b>''<code>' '/trabalhos 29993559806' '</code>' + '\n' + '<b>' '[+] TELEFONE: ' '</b>' '<code>' + '/tel 49991059058' + '</code>' + '\n' + '<b>' '[+] NOME: ' '</b>' '<code>' + '/nome Jhonny Carvalho' + '</code>' + '\n' + '<b>' '[+] VIZINHOS: ' '</b>' '<code>' + '/vizinhos 03493217528' + '</code>' + '\n' + '<b>' '[+] CEP V2: ' '</b>' '<code>' + '/cepe 89874970' + '</code>' + '\n' + '<b>' '[+] CPF V2: ' '</b>' '<code>' + '/master 29993559806' + '</code>' + '\n' + '<b>' '[+] EMAIL: ' '</b>' '<code>' + '/email alexandre.akl@ig.com.br' + '</code>' + '\n' + '<b>' '[+] PARENTES: ' '</b>' '<code>' + '/parentes 03655915993' + '</code>' + '\n' + '<b>' '[+] IP: ' '</b>' '<code>' + '/ip 204.152.203.157' + '</code>' + '\n' + '<b>' '[+] PLACA: ' '</b>' + '<code>' '/placa GTJ6699' '</code>' + '\n\n' + '<b>' '[+] CHK CC: </b><code>/chkcc 6509079001042420' '</code>' '\n\n' + '<b>' '[+] GERAR CPF:</b><code> /gencpf' '</code>' + '\n' + '<b>' '[+] GERAR EMAIL:</b><code> /genemail' + '</code>' + '\n' + '<b>' '[+] GERAR CNPJ:</b><code> /gencnpj' + '</code>' '\n\n' + '<b>' '[+] VALIDAR CPF:</b><code> /validar 03655915993' + '</code>' + '\n\n' + '<b>' '[+] ID: ' '</b>' '<code>' + '/id' + '</code>' + '\n\n' + '<b>🔛 BY: @dkbuscasbot</b>' , parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + '.' + '</b>', parse_mode='HTML')

################################################

# VALIDADOR DE CPF #

@bot.message_handler(commands=['validar'] + ['VALIDAR'])
def bnio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CPF ⚠' + '</b>', parse_mode='HTML')
    if men.text == '/VALIDAR':
        bot.reply_to(men, '<b>' + '⚠ DIGITE UM CPF ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	urrl = requests.get("http://geradorapp.com/api/v1/cpf/validate/" + ip + "?token=4f8d9149be4858c837b8b38f5c0d194a")
        	reeq = urrl.json
        	bot.reply_to(men, '<b>' 'ㅤ🔍 VALIDAR CPF 🔎' + '</b>' +'\n▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' + '• CPF: ' + '</b>' + '<code>' + reeq()['data']['number_formatted'] + '</code>' + '\n' + '<b>' + '• NOME: ' + '</b>' + '<code>' + 'N/A' + '</code>' + '\n' + '<b>' + '• SITUAÇÃO: ' + '</b>' + '<code>' + reeq()['data']['message'] + '</code>' + '\n\n▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' + '• GRUPO: @dkbuscas' + '\n' + '• GRUPO²: @dkbuscas2' + '\n' + '• CANAL: @dkzrefe' + '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '<b>' + 'OPS, CPF INVÁLIDO OU NÃO ENCONTRADO! :(' + '</b>', parse_mode='HTML')

################################################

# CONSULTA DE CNPJ #

@bot.message_handler(commands=['cnpj'] + ['CNPJ'])
def bnioo(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/cnpj':
        bot.reply_to(men, '⚠ 𝘿𝙄𝙂𝙄𝙏𝙀 𝙐𝙈 𝘾𝙉𝙋𝙅, 𝙄𝘿𝙄𝙊𝙏𝘼 ⚠')
    if men.text == '/CNPJ':
        bot.reply_to(men, '⚠ 𝘿𝙄𝙂𝙄𝙏𝙀 𝙐𝙈 𝘾𝙉𝙋𝙅, 𝙄𝘿𝙄𝙊𝙏𝘼 ⚠')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	
        	header = {"Authorization": "Bearer NU.FRdMla45531d4c68b1e837fde9d4c401dc56c56875e8a560595081f2d06ba8068d7e4"}
        	
        	url = requests.get('https://api.nudata.com.br/receita/{}'.format(ip), headers=header)
        	o = url.text
        	req = json.loads(o)
        
        	bot.reply_to(men, 'ㅤㅤㅤㅤㅤ🔍 𝘿𝘼𝘿𝙊𝙎 𝘾𝙉𝙋𝙅 🔎' +
'▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝘾𝙉𝙋𝙅: ' '<code>' + str(req['result']['cnpj']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙏𝙄𝙋𝙊: ' '<code>' + str(req['result']['tipo']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙉𝙊𝙈𝙀: ' '<code>' + str(req['result']['nome']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙏𝙀𝙇𝙀𝙁𝙊𝙉𝙀𝙎: ' '<code>' + str(req['result']['telefone']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙀𝙈𝘼𝙄𝙇: ' '<code>' + str(req['result']['email']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙎𝙄𝙏𝙐𝘼𝘾̧𝘼̃𝙊: ' '<code>' + str(req['result']['situacao']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙇𝙊𝙂𝙍𝘼𝘿𝙊𝙐𝙍𝙊: ' '<code>' + str(req['result']['logradouro']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘽𝘼𝙄𝙍𝙍𝙊: ' '<code>' + str(req['result']['bairro']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙉𝙐́𝙈𝙀𝙍𝙊: ' '<code>' + str(req['result']['numero']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝘾𝙀𝙋: ' '<code>' + str(req['result']['cep']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + 
                     '𝙈𝙐𝙉𝙄𝘾𝙄́𝙋𝙄𝙊: ' '<code>' + str(req['result']['cidade']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'
                     '𝙋𝙊𝙍𝙏𝙀: ' '<code>' + str(req['result']['porte']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘼𝘽𝙀𝙍𝙏𝙐𝙍𝘼: ' '<code>' + str(req['result']['dataAbertura']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙁𝘼𝙉𝙏𝘼𝙎𝙄𝘼: ' '<code>' + str(req['result']['nomeFantasia']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝙎𝙏𝘼𝙏𝙐𝙎: ' '<code>' + str(req['status']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘾𝘼𝙋𝙄𝙏𝘼𝙇: ' '<code>' + str(req['result']['capitalSocial']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'
                     '𝘼𝙏𝙄𝙑𝙄𝘿𝘼𝘿𝙀 𝙋𝙍𝙄𝙉𝘾𝙄𝙋𝘼𝙇: ' '<code>' + str(req['result']['atividadePrimaria']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘼𝙏𝙄𝙑𝙄𝘿𝘼𝘿𝙀 𝙎𝙀𝘾𝙐𝙉𝘿𝘼́𝙍𝙄𝘼: ' '<code>' + str(req['result']['atividadeSecundaria']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                     '𝘿𝘼𝙏𝘼 𝙎𝙄𝙏𝙐𝘼𝘾̧𝘼̃𝙊: ' '<code>' + str(req['result']['dataSituacao']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '𝙐𝙁: ' '<code>' + str(req['result']['estado']) + '</code>' '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '𝘿𝙊𝙉𝙊𝙎: ' '<code>' + str(req['result']['qsa']) + '</code>'  '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙂𝙍𝙐𝙋𝙊:  @dkbuscas\n𝘾𝘼𝙉𝘼𝙇:  @dkzrefe', parse_mode='HTML')
        except:
                     	bot.reply_to(men, '𝙊𝙋𝙎, 𝘾𝙉𝙋𝙅 𝙉𝘼̃𝙊 𝙀𝙉𝘾𝙊𝙉𝙏𝙍𝘼𝘿𝙊 𝙂𝘼𝘿𝙊 🐂')

################################################

# CHECKER DE CC #

@bot.message_handler(commands=['chkcc'])
def zion(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + EXCEPT
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ipo = re.sub('[^0-9|]', '', msg)
                    url = requests.get('https://lookup.binlist.net/' + ipo)
                    req = url.json
                    bot.reply_to(nome, '<b>' 'ㅤㅤㅤ✅ CC CHECKER ✅' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• APROVADO ' + ' ✅' + '\n\n' + '• BANDEIRA: ' '</b>' '<code>' + req()['scheme'] + '</code>' '\n' + '<b>' '• TIPO: ' '</b>' '<code>' + req()['type'] + '</code>' '\n' + '<b>' '• PAÍS: ' '</b>' '<code>' + str(req()['country']['name']) + '</code>' '\n' + '<b>' '• BANCO: ' '</b>' '<code>' + req()['bank']['name'] + '</code>' '\n\n' + '<b>' '• CC: ' '</b>' '<code>' + ipo + '</code>' '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' '• CHK BY: @dkbuscasbot' '</b>', parse_mode='HTML')
                except:
                	bot.reply_to(nome, '<b>' '#Reproved ' + ipo + ' ❌' '</b>', parse_mode='HTML')
            else:
                		bot.reply_to(nome, '<b>' '✅ Compre acesso com meu pai @DKZINNBR ✅' '</b>', parse_mode='HTML')

################################################

# GERADOR DE CPF #

@bot.message_handler(commands=['gencpf'])
def lbx(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + '⚠ ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	resposta = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	cpff = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzinn = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbx = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lb = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbzinn = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkz = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	andrei = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	pc = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	gamer = respostaa()['data']['number_formatted']
        	bot.reply_to(men, '<b>' 'ㅤ⚙ GERADOR DE CPF ⚙' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• CPF: ' '</b>''<code>' + resposta + '</code>' + '\n' + '<b>' '• CPF: ' '</b>' '<code>' + cpff + '</code>' + '\n' + '<b>' + '• CPF: ' + '</b>' '<code>' + dkzinn + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + lbx + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + lb + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + lbzinn + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + dkz + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + andrei + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + pc + '</code>' + '\n' + '<b>' '• CPF: ' '</b>''<code>' + gamer + '</code>' + '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' + '• GRUPO: @dkbuscas' + '\n' + '• GRUPO²: @dkbuscas2' + '\n' + '• CANAL: @dkzrefe' + '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '.')

################################################

# GERADOR DE CNPJ #

@bot.message_handler(commands=['gencnpj'])
def lbxk(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/validar':
        bot.reply_to(men, '<b>' + '⚠ ⚠' + '</b>', parse_mode='HTML')
    else:
        try:
        	ip = re.sub('[^0-9]', '', mensagem)
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	respostak = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	cpffk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzinnk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbxk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	lbzinnk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	dkzk = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	andreik = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	pck = respostaa()['data']['number_formatted']
        	url = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        	respostaa = url.json
        	gamerk = respostaa()['data']['number_formatted']
        	bot.reply_to(men, '<b>' 'ㅤ⚙ GERADOR DE CNPJ ⚙' '</b>' + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n\n' + '<b>' '• CNPJ: ' '</b>''<code>' + respostak + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>' '<code>' + cpffk + '</code>' + '\n' + '<b>' + '• CNPJ: ' + '</b>' '<code>' + dkzinnk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + lbxk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + lbk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + lbzinnk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + dkzk + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + andreik + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + pck + '</code>' + '\n' + '<b>' '• CNPJ: ' '</b>''<code>' + gamerk + '</code>' + '\n\n▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n' + '<b>' + '• GRUPO: @dkbuscas' + '\n' + '• GRUPO²: @dkbuscas2' + '\n' + '• CANAL: @dkzrefe' + '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '.')

################################################

# GERADOR DE EMAIL #

@bot.message_handler(commands=['genemail'])
def ipoop(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/chkcc':
        bot.reply_to(men, '<b>' '⚠' '</b>', parse_mode='HTML')
    else:
        try:
        	ipo = re.sub('[^A-Z]', '', mensagem)
        	url = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        	url2 = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        	url3 = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        	req = url.text
        	req2 = url2.text
        	req3 = url3.text
        	bot.reply_to(men, '<b>' '📧 EMAIL FAKE 📧' '</b>' + '\n\n' + '<code>' + req + '</code>' + '\n' + '<code>' + req2 + '</code>' + '\n' + '<code>' + req3 + '</code>' + '\n\n' + '<b>' '• GRUPO: @dkbuscas\n• GRUPO²: @dkbuscas2\n• CANAL: @dkzrefe' '</b>', parse_mode='HTML')
        except:
                    bot.reply_to(men, '', parse_mode='HTML')

################################################

# VER ID #

@bot.message_handler(commands=['id'])
def boavinnda(message1):
    bot.reply_to(message1, '<b>' '• SEU ID: ' '</b>''<code>' + str(message1.chat.id) + '</code>' '\n'+ '<b>' '• NOME: ' '</b>' '<code>'+ message1.chat.first_name + '</code>' '\n' + '<b>''• USERNAME: '+'@'+message1.chat.username + '</b>' , parse_mode='HTML')

################################################

# CONSULTA DE VIZINHOS #

@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, '<b>' 'DIGITE UM CPF, ANIMAL!' '</b>' ,
                                 parse_mode='HTML')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' '🔍 CONSULTA REALIZADA 🔎' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• GRUPO: @dkbuscas\n• GRUPO²: @dkbuscas3\n• CANAL: @dkzrefe' '</b>' , parse_mode='HTML')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' '🔍 CONSULTA REALIZADA 🔎' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• GRUPO: @dkbuscas\n• GRUPO²: @dkbuscas3\n• CANAL: @dkzrefe' '</b>',
                                             parse_mode='HTML')
                            except:
                                bot.reply_to(men, '<b>NENHUM VIZINHO ENCONTRADO</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>OPS, NENHUM VIZINHO ENCONTRADO </b>', parse_mode="HTML")

            else:
                bot.reply_to(men, '<b>✅ Compre acesso com meu pai @DKZINNBR ✅</b>',
                             parse_mode='HTML')

################################################

# CONSULTA DE IP #

@bot.message_handler(commands=['ip', 'IP'])
def bxniy(men):
            liberadoip = PRIVADO + GRUPO + EXCEPT
            bid = men.chat.id
            if bid in liberadoip:
                mensagem = men.text
                if men.text == '/ip':
                    bot.reply_to(men, '<b>' 'DIGITE UM IP, ANIMAL!' '</b>', parse_mode='HTML')
                elif men.text == '/IP':
                    bot.reply_to(men, '<b>' 'DIGITE UM IP, ANIMAL!' '</b>', parse_mode='HTML')
                else:
                    try:
                        ip = re.sub('[^0-9.]', '', mensagem)
                        url = requests.get(
                            'https://king.host/wiki/wp-content/themes/kinghost-wiki/includes/ip-api.php?ip={}'.format(ip))
                        req = json.loads(url.text)
                        bot.reply_to(men,
                                     '▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙄𝙋: ' + req['query'] + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙋𝘼𝙄́𝙎: ' + req[
                                         'country'] + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙎𝙄𝙂𝙇𝘼 𝙋𝘼𝙄́𝙎: ' + str(req['countryCode']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙍𝙀𝙂𝙄𝘼̃𝙊: ' + str(req['region']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙍𝙀𝙂𝙄𝘼̃𝙊 𝙉𝘼𝙈𝙀: ' + str(req['regionName']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝘾𝙄𝘿𝘼𝘿𝙀: ' + str(req['city']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝘾𝙀𝙋: ' + str(req['zip']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙇𝘼𝙏𝙄𝙏𝙐𝘿𝙀: ' + str(req['lat']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙇𝙊𝙉𝙂𝙄𝙏𝙐𝘿𝙀: ' + str(req['lon']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n' +
                                     '𝙋𝙍𝙊𝙑𝙀𝘿𝙊𝙍: ' + str(req[
                                                                    'org']) + '\n▱▱▱▱▱▱▱▱▱▱▱▱▱\n𝙂𝙍𝙐𝙋𝙊:  @dkbuscas')
                    except:
                        bot.reply_to(men, '<b>IP NÃO ENCONTRADO</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>✅ Compre acesso com meu pai @DKZINNBR ✅</b>', parse_mode='HTML')

################################################

# CONSULTA DE TRABALHOS ( CPF ) #

@bot.message_handler(commands=['cpf'] + ['CPF'])
def bunda(message1):
            ideee = message1.chat.id
            text = message1.text
            lib = PRIVADO + EXCEPT
            if ideee in lib:
                if message1.text == '/cpf':
                    help1 = bot.reply_to(message1,
                                         '<b>DIGITE UM CPF, ANIMAL!</b>', parse_mode='HTML' )
                    sleep(10)
                    bot.delete_message(ideee, help1.message_id)
                    bot.delete_message(ideee, message1.message_id)
                elif message1.text == '/CPF':
                    help2 = bot.reply_to(message1,
                                         '<b>DIGITE UM CPF, ANIMAL!</b>', parse_mode='HTML')
                    sleep(10)
                    bot.delete_message(ideee, help2.message_id)
                    bot.delete_message(ideee, message1.message_id)
                else:
                    try:

                        filtr = re.sub('[^0-9]', '', text)
                        url = requests.get(
                            'https://fscenter.tech/cpf.php?key=mVj9L3s5&cpf={}'.format(
                                filtr)).content
                        resp = json.loads(url)

                        ##########################################
                        try:
                            ende = ('<b>TIPO LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['tipoLogradouro']) + '</code>\n'
                                                                                                           '<b>LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['logradouro']) + '</code>\n'
                                                                                                       '<b>NUMERO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['numero']) + '</code>\n'
                                                                                                   '<b>COMPLEMENTO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['complemento']) + '</code>\n'
                                                                                                        '<b>BAIRRO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['bairro']) + '</code>\n'

                                                                                                   '<b>CIDADE: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['cidade']) + '</code>\n'
                                                                                                   '<b>UF: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0]['uf']) + '</code>\n'
                                                                                               '<b>CEP: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][0][
                                    'cep']) + '</code>\n\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['tipoLogradouro']) + '</code>\n'
                                                                                                           '<b>LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['logradouro']) + '</code>\n'
                                                                                                       '<b>NUMERO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['numero']) + '</code>\n'
                                                                                                   '<b>COMPLEMENTO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['complemento']) + '</code>\n'
                                                                                                        '<b>BAIRRO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['bairro']) + '</code>\n'
                                                                                                   '<b>CIDADE: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1]['cidade']) + '</code>\n'
                                                                                                   '<b>UF: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][1][
                                    'uf']) + '</code>\n\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'tipoLogradouro']) + '</code>\n' + '<b>LOGRADOURO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'logradouro']) + '</code>\n' + '<b>NUMERO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'numero']) + '</code>\n' + '<b>COMPLEMENTO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'complemento']) + '</code>\n' + '<b>BAIRRO: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'bairro']) + '</code>\n' + '<b>CIDADE: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'cidade']) + '</code>\n' + '<b>UF: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2][
                                    'uf']) + '</code>\n' + '<b>CEP: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['endereco'][2]['cep']) + '</code>\n\n')
                            # TRATAMENTO ENDEREÇO
                        except:
                            try:
                                ende = ('<b>TIPO LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0][
                                        'tipoLogradouro']) + '</code>\n'
                                                             '<b>LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['logradouro']) + '</code>\n'
                                                                                                           '<b>NUMERO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['numero']) + '</code>\n'
                                                                                                       '<b>COMPLEMENTO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['complemento']) + '</code>\n'
                                                                                                            '<b>BAIRRO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['bairro']) + '</code>\n'

                                                                                                       '<b>CIDADE: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['cidade']) + '</code>\n'
                                                                                                       '<b>UF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0]['uf']) + '</code>\n'
                                                                                                   '<b>CEP: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][0][
                                        'cep']) + '</code>\n\n' + '<b>TIPO LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1][
                                        'tipoLogradouro']) + '</code>\n'
                                                             '<b>LOGRADOURO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['logradouro']) + '</code>\n'
                                                                                                           '<b>NUMERO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['numero']) + '</code>\n'
                                                                                                       '<b>COMPLEMENTO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['complemento']) + '</code>\n'
                                                                                                            '<b>BAIRRO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['bairro']) + '</code>\n'
                                                                                                       '<b>CIDADE: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['cidade']) + '</code>\n'
                                                                                                       '<b>UF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['endereco'][1]['uf']) + '</code>\n\n')
                            except:
                                try:
                                    ende = ('<b>TIPO LOGRADOURO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0][
                                            'tipoLogradouro']) + '</code>\n'
                                                                 '<b>LOGRADOURO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0][
                                            'logradouro']) + '</code>\n'
                                                             '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['numero']) + '</code>\n'
                                                                                                           '<b>COMPLEMENTO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0][
                                            'complemento']) + '</code>\n'
                                                              '<b>BAIRRO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['bairro']) + '</code>\n'

                                                                                                           '<b>CIDADE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['cidade']) + '</code>\n'
                                                                                                           '<b>UF: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['uf']) + '</code>\n'
                                                                                                       '<b>CEP: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['endereco'][0]['cep']) + '</code>\n\n')
                                except:
                                    ende = 'ENDEREÇO NÃO ENCONTRADO'
                        ##############################
                        try:
                            parent = ('<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][0]['nomeCompleto']) + '</code>\n'
                                                                                                           '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                    'cpf']) + '</code>\n' + '<b>GRAU DE PARENTESCO: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                    'grauDeParentesco']) + '</code>\n\n' + '<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][1]['nomeCompleto']) + '</code>\n'
                                                                                                           '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][1][
                                    'cpf']) + '</code>\n' + '<b>GRAU DE PARENTESCO: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['parentesco'][1][
                                    'grauDeParentesco']) + '</code>\n\n')
                            # TRATAMENTO PARENTESCO
                        except:
                            try:
                                parent = ('<b>NOME: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                        'nomeCompleto']) + '</code>\n'
                                                           '<b>CPF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                        'cpf']) + '</code>\n' + '<b>GRAU DE PARENTESCO: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['parentesco'][0][
                                        'grauDeParentesco']) + '</code>\n\n')
                            except:
                                parent = 'PARENTES NÃO ENCONTRADOS'
                        #################################
                        try:
                            viz = ('<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'nomePrimeiro']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'nomeMeio']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                    'cpf']) + ' </code>\n\n' + '<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomePrimeiro']) + ' ' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomeMeio']) + ' ' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                    'nomeUltimo']) + '</code>\n<b>CPF: </b>' + '<code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                    'cpf']) + '</code>\n\n' + '<b>NOME: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'nomePrimeiro']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'nomeMeio']) + ' </code><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                resp['result'][0]['pessoa']['vinculo']['vizinho'][2][
                                    'cpf']) + ' </code>\n\n')
                            # TRATAMENTO VIZINHOS
                        except:
                            try:
                                viz = ('<b>NOME: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'nomePrimeiro']) + ' </code><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'nomeMeio']) + ' </code><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                        'cpf']) + ' </code>\n\n' + '<b>NOME: </b><code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomePrimeiro']) + ' ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1]['nomeMeio']) + ' ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                        'nomeUltimo']) + '</code>\n<b>CPF: </b>' + '<code>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['vizinho'][1][
                                        'cpf']) + '</code>\n\n')
                            except:
                                try:
                                    viz = ('<b>NOME: </b><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'nomePrimeiro']) + ' </code><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'nomeMeio']) + ' </code><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'nomeUltimo']) + ' </code>\n' + '<b>CPF: </b><code>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['vizinho'][0][
                                            'cpf']) + ' </code>\n\n')
                                except:
                                    viz = 'SEM VIZINHOS'
                        ################################
                        try:
                            emai = (str(resp['result'][0]['pessoa']['contato']['email'][0]['email']) + '\n' + str(
                                resp['result'][0]['pessoa']['contato']['email'][1]['email']) + '\n' + str(
                                resp['result'][0]['pessoa']['contato']['email'][2]['email']) + '\n')
                            # TRATAMENTO EMAILS
                        except:
                            try:
                                emai = (str(resp['result'][0]['pessoa']['contato']['email'][0]['email']) + '\n' + str(
                                    resp['result'][0]['pessoa']['contato']['email'][1]['email']) + '\n')
                            except:
                                try:
                                    emai = (str(resp['result'][0]['pessoa']['contato']['email'][0]['email']) + '\n')
                                except:
                                    emai = 'SEM EMAIL'
                        ##############################
                        try:
                            tel = ('<b>DDD: </b><code>' + str(
                                resp['result'][0]['pessoa']['contato']['telefone'][0]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0]['numero']) + '</code>\n' +
                                   '<b>OPERADORA: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0][
                                            'operadora']) + '</code>\n' +
                                   '<b>TIPO TELEFONE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0][
                                            'tipoTelefone']) + '</code>\n\n' +
                                   '<b>DDD:</b><code> ' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1]['numero']) + '</code>\n' +
                                   '<b>OPERADORA: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1][
                                            'operadora']) + '</code>\n' +
                                   '<b>TIPO TELEFONE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][1][
                                            'tipoTelefone']) + '</code>\n\n' +
                                   '<b>DDD:</b><code> ' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2]['ddd']) + '</code>\n' +
                                   '<b>NUMERO: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2]['numero']) + '</code>\n' +
                                   '<b>OPERADORA: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2][
                                            'operadora']) + '</code>\n' +
                                   '<b>TIPO TELEFONE: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][2][
                                            'tipoTelefone']) + '</code>\n\n')
                            # TRATAMENTO TELEFONES
                            # TELEFONES
                        except:
                            try:
                                tel = ('<b>DDD: </b><code>' + str(
                                    resp['result'][0]['pessoa']['contato']['telefone'][0]['ddd']) + '</code>\n' +
                                       '<b>NUMERO: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                'numero']) + '</code>\n' +
                                       '<b>OPERADORA: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                'operadora']) + '</code>\n' +
                                       '<b>TIPO TELEFONE: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                'tipoTelefone']) + '</code>\n\n' +
                                       '<b>DDD: </b><code>' + str(resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                                      'ddd']) + '</code>\n' +
                                       '<b>NUMERO: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                'numero']) + '</code>\n' +
                                       '<b>OPERADORA: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                'operadora']) + '</code>\n' +
                                       '<b>TIPO TELEFONE: </b><code>' + str(
                                            resp['result'][0]['pessoa']['contato']['telefone'][1][
                                                'tipoTelefone']) + '</code>\n\n')
                            except:
                                try:
                                    tel = ('<b>DDD: </b><code>' + str(
                                        resp['result'][0]['pessoa']['contato']['telefone'][0]['ddd']) + '</code>\n' +
                                           '<b>NUMERO: </b><code>' + str(
                                                resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                    'numero']) + '</code>\n' +
                                           '<b>OPERADORA: </b><code>' + str(
                                                resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                    'operadora']) + '</code>\n' +
                                           '<b>TIPO TELEFONE: </b><code>' + str(
                                                resp['result'][0]['pessoa']['contato']['telefone'][0][
                                                    'tipoTelefone']) + '</code>\n\n')
                                except:
                                    tel = 'TELEFONE NÃO ENCONTRADO'
                        ###################################
                        try:
                            psocietaria = ('<b>CNPJ: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0]['nr_cnpj']) + '\n'
                                                                                                                  '<b>RAZÃO SOCIAL: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                    'razaoSocial']) + '\n'
                                                      '<b>PARTICIPAÇÃO: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                    'participacao']) + '\n'
                                                       '<b>QUALIFICAÇÃO: </b>' + str(
                                resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                    'qualificacao']) + '\n\n' +
                                           '<b>CNPJ: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'nr_cnpj']) + '\n'
                                                          '<b>RAZÃO SOCIAL: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'razaoSocial']) + '\n'
                                                              '<b>PARTICIPAÇÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'participacao']) + '\n'
                                                               '<b>QUALIFICAÇÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                            'qualificacao']) + '\n\n' +
                                           '<b>CNPJ: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'nr_cnpj']) + '\n'
                                                          '<b>RAZÃO SOCIAL: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'razaoSocial']) + '\n'
                                                              '<b>PARTICIPAÇÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'participacao']) + '\n'
                                                               '<b>QUALIFICAÇÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][2][
                                            'qualificacao']) + '\n\n')
                            # TRATAMENTO PARTICIPAÇÕES SOCIETARIAS
                        except:
                            try:
                                psocietaria = ('<b>CNPJ: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'nr_cnpj']) + '\n'
                                                      '<b>RAZÃO SOCIAL: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'razaoSocial']) + '\n'
                                                          '<b>PARTICIPAÇÃO: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'participacao']) + '\n'
                                                           '<b>QUALIFICAÇÃO: </b>' + str(
                                    resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                        'qualificacao']) + '\n\n' +
                                               '<b>CNPJ: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'nr_cnpj']) + '\n'
                                                              '<b>RAZÃO SOCIAL: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'razaoSocial']) + '\n'
                                                                  '<b>PARTICIPAÇÃO: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'participacao']) + '\n'
                                                                   '<b>QUALIFICAÇÃO: </b>' + str(
                                            resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][1][
                                                'qualificacao']) + '\n\n')
                            except:
                                try:
                                    psocietaria = ('<b>CNPJ: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'nr_cnpj']) + '\n'
                                                          '<b>RAZÃO SOCIAL: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'razaoSocial']) + '\n'
                                                              '<b>PARTICIPAÇÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'participacao']) + '\n'
                                                               '<b>QUALIFICAÇÃO: </b>' + str(
                                        resp['result'][0]['pessoa']['vinculo']['participacaoSocietaria'][0][
                                            'qualificacao']) + '\n\n')
                                except:
                                    psocietaria = 'SEM PARTICIPAÇÕES SOCIETARIAS'
                        ####################################
                        try:
                            empregador = ('CNPJ: ' + str(
                                resp['result'][0]['pessoa']['vinculo']['empregador'][0]['cnpj']) + '\n'
                                                                                                   'RAZAO SOCIAL: ' + str(
                                resp['result'][0]['pessoa']['vinculo']['empregador'][0]['razaoSocial']) + '\n'
                                                                                                          'ADMISSÃO: ' + str(
                                resp['result'][0]['pessoa']['vinculo']['empregador'][0]['dataAdmissao']) + '\n\n' +
                                          'CNPJ: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][1]['cnpj']) + '\n'
                                                                                                           'RAZAO SOCIAL: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][1]['razaoSocial']) + '\n'
                                                                                                                  'ADMISSÃO: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][1][
                                            'dataAdmissao']) + '\n\n' +
                                          'CNPJ: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][2]['cnpj']) + '\n'
                                                                                                           'RAZAO SOCIAL: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][2]['razaoSocial']) + '\n'
                                                                                                                  'ADMISSÃO: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][2]['dataAdmissao']) + '\n')
                            # TRATAMENTO EMPREGADOR
                        except:
                            try:
                                empregador = ('CNPJ: ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['empregador'][0]['cnpj']) + '\n'
                                                                                                       'RAZAO SOCIAL: ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['empregador'][0]['razaoSocial']) + '\n'
                                                                                                              'ADMISSÃO: ' + str(
                                    resp['result'][0]['pessoa']['vinculo']['empregador'][0]['dataAdmissao']) + '\n\n' +
                                              'CNPJ: ' + str(
                                            resp['result'][0]['pessoa']['vinculo']['empregador'][1]['cnpj']) + '\n'
                                                                                                               'RAZAO SOCIAL: ' + str(
                                            resp['result'][0]['pessoa']['vinculo']['empregador'][1][
                                                'razaoSocial']) + '\n'
                                                                  'ADMISSÃO: ' + str(
                                            resp['result'][0]['pessoa']['vinculo']['empregador'][1][
                                                'dataAdmissao']) + '\n')
                            except:
                                try:
                                    empregador = ('CNPJ: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][0]['cnpj']) + '\n'
                                                                                                           'RAZAO SOCIAL: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][0]['razaoSocial']) + '\n'
                                                                                                                  'ADMISSÃO: ' + str(
                                        resp['result'][0]['pessoa']['vinculo']['empregador'][0]['dataAdmissao']) + '\n')
                                except:
                                    empregador = 'NULL'
                        #####################################
                        try:
                            veiculo = ('MARCA: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                    'MODELO: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['modelo']) + '\n'
                                                                                                     'ANO: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['ano']) + '\n'
                                                                                                  'CATEGORIA: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                    'CLASSIFICAÇÃO: ' + str(
                                resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['classificacao']) + '\n\n' +
                                       'MARCA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                            'MODELO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['modelo']) + '\n'
                                                                                                             'ANO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['ano']) + '\n'
                                                                                                          'CATEGORIA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                            'CLASSIFICAÇÃO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][1][
                                            'classificacao']) + '\n\n' +
                                       'MARCA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['marca']) + '\n'
                                                                                                            'MODELO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['modelo']) + '\n'
                                                                                                             'ANO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['ano']) + '\n'
                                                                                                          'CATEGORIA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2]['marca']) + '\n'
                                                                                                            'CLASSIFICAÇÃO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][2][
                                            'classificacao']) + '\n\n')
                            # TRATAMENTO VEICULO
                        except:
                            try:
                                veiculo = ('MARCA: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                        'MODELO: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['modelo']) + '\n'
                                                                                                         'ANO: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['ano']) + '\n'
                                                                                                      'CATEGORIA: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                        'CLASSIFICAÇÃO: ' + str(
                                    resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['classificacao']) + '\n\n' +
                                           'MARCA: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                                'MODELO: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['modelo']) + '\n'
                                                                                                                 'ANO: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['ano']) + '\n'
                                                                                                              'CATEGORIA: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1]['marca']) + '\n'
                                                                                                                'CLASSIFICAÇÃO: ' + str(
                                            resp['result'][0]['pessoa']['patrimonio']['veiculo'][1][
                                                'classificacao']) + '\n\n')
                            except:
                                try:
                                    veiculo = ('MARCA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                            'MODELO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['modelo']) + '\n'
                                                                                                             'ANO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['ano']) + '\n'
                                                                                                          'CATEGORIA: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0]['marca']) + '\n'
                                                                                                            'CLASSIFICAÇÃO: ' + str(
                                        resp['result'][0]['pessoa']['patrimonio']['veiculo'][0][
                                            'classificacao']) + '\n\n')
                                except:
                                    veiculo = 'NULL'
                        ################################
                        bot.reply_to(message1,
                                     '<b>CPF: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['CPF']) + '</code>\n' +

                                     '<b>NOME: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['nomePrimeiro']) + ' ' +
                                     str(resp['result'][0]['pessoa']['cadastral']['nomeMeio']) + ' ' + str(
                                         resp['result'][0]['pessoa']['cadastral']['nomeUltimo']) + '</code>\n' +

                                     '<b>SEXO: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['sexo']) + '</code>\n' +
                                     '<b>DATA NASC: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['dataNascimento']) + '</code>\n' +
                                     '<b>STATUS RECEITA FEDERAL: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral'][
                                             'statusReceitaFederal']) + '</code>\n\n' +
                                     '<b>RG: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['rgNumero']) + '</code>\n' +
                                     '<b>ORGÃO EMISSOR: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['rgOrgaoEmissor']) + '</code>\n' +
                                     '<b>UF RG: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['rgUf']) + '</code>\n\n' +
                                     '<b>TITULO ELEITORAL: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['tituloEleitoral']) + '</code>\n' +
                                     '<b>NACIONALIDADE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['nacionalidade']) + '</code>\n' +
                                     '<b>ESTADO CIVIL: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['estadoCivil']) + '</code>\n\n' +

                                     '<b>NOME MÃE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral'][
                                             'maeNomePrimeiro']) + ' </code><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral'][
                                             'maeNomeMeio']) + ' </code><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['maeNomeUltimo']) + '</code>\n' +
                                     '<b>CPF MÃE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['maeCPF']) + '</code>\n' +
                                     '<b>ESCOLARIDADE: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['escolaridade']) + '</code>\n' +
                                     '<b>CNS: </b><code>' + str(
                                         resp['result'][0]['pessoa']['cadastral']['cns']) + '</code>\n\n' +
                                     '<b>BOLSA FAMILIA: </b><code>' + str(
                                         resp['result'][0]['pessoa']['beneficiarioProgramaSocial'][
                                             'bolsaFamilia']) + '</code>\n\n' +
                                     '<b>ENDEREÇO: </b>\n' + ende +
                                     '\n\n<b>PARENTESCO: </b>\n\n' + parent +
                                     '\n\n<b>VIZINHOS: </b>\n\n' + viz + '<b>' + '\n\nEMAIL:\n' + '</b>' + str(emai) +
                                     '<b>' + '\nTELEFONES:\n\n' + '</b>' + str(tel) + '<b>' +
                                     'CONJUGE:\n'
                                     'NOME: ' + '</b>' + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['nomePrimeiro']) + ' ' + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['nomeMeio']) + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['nomeUltimo']) + '\n' + '<b>' +
                                                                                                            'PARENTESCO: ' + '</b>' + str(
                                         resp['result'][0]['pessoa']['vinculo']['conjuge']['parentesco']) + '\n\n'
                                                                                                            '𝙋𝘼𝙍𝙏𝙄𝘾𝙄𝙋𝘼𝘾̧𝘼̃𝙊 𝙎𝙊𝘾𝙄𝙀𝙏𝘼𝙍𝙄𝘼:\n\n' + psocietaria +
                                     '\n\n𝙀𝙈𝙋𝙍𝙀𝙂𝘼𝘿𝙊𝙍:\n' + empregador +
                                     '\n\n𝙑𝙀𝙄𝘾𝙐𝙇𝙊𝙎: \n' + veiculo +
                                     '\n\n𝙋𝙍𝙊𝙁𝙄𝙎𝙎𝘼̃𝙊: ' + str(
                                         resp['result'][0]['pessoa']['socioDemografico']['profissao']) +
                                     '\n𝙍𝙀𝙉𝘿𝘼 𝙋𝙍𝙀𝙎𝙐𝙈𝙄𝘿𝘼:: ' + str(
                                         resp['result'][0]['pessoa']['socioDemografico'][
                                             'rendaPresumida']) + '<b>' + '\n\nGRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe' + '</b>',
                                     parse_mode='HTML')
                    except:
                        bot.reply_to(message1, '<b>' + 'ERRO, VERIFIQUE O CPF' + '</b>', parse_mode='HTML')

            else:
                bot.reply_to(message1,
                             '<b>' + '✅ Adquira acesso com meu pai @DKZINNBR ✅' + '</b>',
                             parse_mode='HTML')
################################################

# CONSULTA DE TELEFONE #

@bot.message_handler(commands=['tel'] + ['TEL'])
def beroi(men):
            idee = men.chat.id
            permitidos = PRIVADO + EXCEPT
            if int(idee) in permitidos:
                session = requests_html.HTMLSession()

                if men.text == '/tel':
                    bot.reply_to(men, '<b>DIGITE UM NÚMERO, ANIMAL!</b>',
                                 parse_mode='HTML')
                elif men.text == '/TEL':
                    bot.reply_to(men, '<b>DIGITE UM NÚMERO, ANIMAL!</b>',
                                 parse_mode='HTML')
                else:

                    num = re.sub('[^0-9]', '', men.text)
                    r = session.get(
                        'http://fscenter.tech/telefone.php?token=kClyOIbp&telefone={}'.format(num))
                    ar = r.html.find("td")
                    ar1 = r.html.find('tr')
                    try:
                        txt = ar[0].html
                        cpf = re.sub('[^0-9]', '', txt)
                        dados = str(ar1[1].text)

                        txt2 = ar[5].html
                        cpf2 = re.sub('[^0-9]', '', txt2)
                        dados2 = str(ar1[2].text)

                        txt3 = ar[10].html
                        cpf3 = re.sub('[^0-9]', '', txt3)
                        dados3 = str(ar1[3].text)

                        bot.reply_to(men,
                                     dados + '\n<b>CPF: </b>' + cpf + '\n\n' + dados2 + '\n<b>CPF: </b>' + cpf2 + '\n\n' + dados3 + '\n<b>CPF: </b>' + cpf3 + '\n\n<b>• GRUPO: @dkbuscas\n• GRUPO²: @dkbuscas3\n• CANAL: @dkzrefe</b>',
                                     parse_mode='HTML')
                    except:
                        try:
                            txt = ar[0].html
                            cpf = re.sub('[^0-9]', '', txt)
                            dados = str(ar1[1].text)

                            txt2 = ar[1].html
                            cpf2 = re.sub('[^0-9]', '', txt2)
                            dados2 = str(ar1[2].text)

                            bot.reply_to(men,
                                         dados + '\n<b>CPF: </b>' + cpf + '\n\n' + dados2 + '\n<b>CPF: </b>' + cpf2 + '\n\n<b>• GRUPO: @dkbuscas\n• GRUPO²: @dkbuscas3\n• CANAL: @dkzrefe</b>',
                                         parse_mode='HTML')
                        except:
                            try:
                                txt = ar[0].html
                                cpf = re.sub('[^0-9]', '', txt)
                                dados = str(ar1[1].text)
                                bot.reply_to(men, '<b>' '🔍 CONSULTA REALIZADA 🔎' '</b>' + '\n\n' + '<code>' +
                                             dados + '</code>' + '\n<b>CPF: </b>' '<code>' + cpf + '</code>' + '\n\n<b>• GRUPO: @dkbuscas\n• GRUPO²: @dkbuscas3\n• CANAL: @dkzrefe</b>',
                                             parse_mode='HTML')
                            except:
                                bot.reply_to(men, '<b>NÃO ENCONTRADO</b>', parse_mode='HTML')




            else:
                bot.reply_to(men, '<b>' '✅ Compre acesso com meu pai @DKZINNBR ✅' '</b>', parse_mode='HTML')

#######

@bot.message_handler(commands=['email'] + ['EMAIL'])
def bqpwi(men):
            idee = men.chat.id
            permitidos = PRIVADO + GRUPO + EXCEPT
            if int(idee) in permitidos:
                session = requests_html.HTMLSession()
                mensagem = men.text
                oi = str(mensagem[7:])

                if men.text == '/email':
                    bot.reply_to(men, '<b>' 'DIGITE UM EMAIL, ANIMAL' '</b>',
                                 parse_mode='HTML')
                elif men.text == '/EMAIL':
                    bot.reply_to(men, '<b>' 'DIGITE UM EMAIL, ANIMAL' '</b>',
                                 parse_mode='HTML')
                else:

                    r = session.get(
                        'http://fscenter.tech/email.php?token=uXsSuz3e&email={}'.format(oi))
                    ar = r.html.find("td")
                    ar1 = r.html.find('tr')
                    try:
                        txt = ar[0].html
                        cpf = re.sub('[^0-9]', '', txt)
                        dados = str(ar1[1].text)

                        txt2 = ar[5].html
                        cpf2 = re.sub('[^0-9]', '', txt2)
                        dados2 = str(ar1[2].text)

                        txt3 = ar[10].html
                        cpf3 = re.sub('[^0-9]', '', txt3)
                        dados3 = str(ar1[3].text)

                        bot.reply_to(men, '<b>' '🔍 CONSULTA REALIZADA 🔎' '</b>' + '\n\n' +
                                    '<code>' + dados + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf + '</code>' + '\n\n' + '<code>' + dados2 + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf2 + '</code>' + '\n\n' + '<code>' + dados3 + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf3 + '</code>' + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                     parse_mode='HTML')
                    except:
                        try:
                            txt = ar[0].html
                            cpf = re.sub('[^0-9]', '', txt)
                            dados = str(ar1[1].text)

                            txt2 = ar[1].html
                            cpf2 = re.sub('[^0-9]', '', txt2)
                            dados2 = str(ar1[2].text)

                            bot.reply_to(men, '<b>' '🔍 CONSULTA REALIZADA 🔎' '</b>' + '\n\n' +
                                        '<code>' + dados + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf + '</code>' + '\n\n' + '<code>' + dados2 + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf2 + '</code>' + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                         parse_mode='HTML')
                        except:
                            try:
                                txt = ar[0].html
                                cpf = re.sub('[^0-9]', '', txt)
                                dados = str(ar1[1].text)
                                bot.reply_to(men, '<b>' '🔍 CONSULTA REALIZADA 🔎' '</b>' + '\n\n' +
                                            '<code>' + dados + '</code>' + '\n<b>CPF: </b>' + '<code>' + cpf + '</code>' + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                             parse_mode='HTML')
                            except:
                                N = bot.reply_to(men, '<b>OPS, EMAIL NÃO ECONTRADO!</b>', parse_mode='HTML')
            else:
                bot.reply_to(men, '<b>' '✅ Compre acesso com meu pai @DKZINNBR ✅' '</b>',
                             parse_mode='HTML')
######

@bot.message_handler(commands=['nome'] + ['NOME'])
def sjjsn(nome):
            id1 = nome.chat.id
            men = nome.text
            oi = str(men[6:])
            ltnome = EXCEPT + PRIVADO
            if id1 in ltnome:

                session = requests_html.HTMLSession()
                if men == '/nome':
                    bot.reply_to(nome, '<b>DIGITE UM NOME, ANIMAL!</b>',
                                 parse_mode='HTML')
                elif men == '/NOME':
                    bot.reply_to(nome, '<b>DIGITE UM NOME, ANIMAL!</b>',
                                 parse_mode='HTML')
                else:
                    try:
                        bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')

                        r = session.get(
                            'http://fscenter.tech/nome.php?token=LyTHY70e&nome={}'.format(oi))
                        ar = r.html.find("td")
                        ar1 = r.html.find('tr')
                        try:
                            bot.reply_to(nome,
                                         str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[0].html) + '\n\n' +
                                         str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[5].html) + '\n\n' +
                                         str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[10].html) + '\n\n' +
                                         str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[15].html) + '\n\n' +
                                         str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[20].html) + '\n\n' +
                                         str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[25].html) + '\n\n' +
                                         str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[30].html) + '\n\n' +
                                         str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[35].html) + '\n\n' +
                                         str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                    ar[40].html) + '\n\n' +
                                         str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[45].html) + '\n\n' +
                                         str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[50].html) + '\n\n' +
                                         str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[55].html) + '\n\n' +
                                         str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[60].html) + '\n\n' +
                                         str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[65].html) + '\n\n' +
                                         str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[70].html) + '\n\n' +
                                         str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[75].html) + '\n\n' +
                                         str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[80].html) + '\n\n' +
                                         str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[85].html) + '\n\n' +
                                         str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[90].html) + '\n\n' +
                                         str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[95].html) + '\n\n' +
                                         str(ar1[21].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[100].html) + '\n\n' +
                                         str(ar1[22].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[105].html) + '\n\n' +
                                         str(ar1[23].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[110].html) + '\n\n' +
                                         str(ar1[24].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[115].html) + '\n\n' +
                                         str(ar1[25].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[120].html) + '\n\n' +
                                         str(ar1[26].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[125].html) + '\n\n' +
                                         str(ar1[27].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[130].html) + '\n\n' +
                                         str(ar1[28].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[135].html) + '\n\n' +
                                         str(ar1[29].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[140].html) + '\n\n' +
                                         str(ar1[30].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[145].html) + '\n\n' +
                                         str(ar1[31].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[150].html) + '\n\n' +
                                         str(ar1[32].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[155].html) + '\n\n' +
                                         str(ar1[33].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[160].html) + '\n\n' +
                                         str(ar1[34].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[165].html) + '\n\n' +
                                         str(ar1[35].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[170].html) + '\n\n' +
                                         str(ar1[36].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[175].html) + '\n\n' +
                                         str(ar1[37].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[180].html) + '\n\n' +
                                         str(ar1[38].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[185].html) + '\n\n' +
                                         str(ar1[39].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[190].html) + '\n\n' +
                                         str(ar1[40].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[195].html) + '\n\n' +
                                         str(ar1[41].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[200].html) + '\n\n' +
                                         str(ar1[42].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[205].html) + '\n\n' +
                                         str(ar1[43].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[210].html) + '\n\n' +
                                         str(ar1[44].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[215].html) + '\n\n' +
                                         str(ar1[45].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[220].html) + '\n\n' +
                                         str(ar1[46].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[225].html) + '\n\n' +
                                         str(ar1[47].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[230].html) + '\n\n' +
                                         str(ar1[48].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[235].html) + '\n\n' +
                                         str(ar1[49].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                     ar[240].html) + '\n\n' +
                                         str(ar1[50].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                             245].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>', parse_mode='HTML')
                        except:
                            try:
                                bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                              ar[0].html) + '\n\n' +
                                             str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[5].html) + '\n\n' +
                                             str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[10].html) + '\n\n' +
                                             str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[15].html) + '\n\n' +
                                             str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[20].html) + '\n\n' +
                                             str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[25].html) + '\n\n' +
                                             str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[30].html) + '\n\n' +
                                             str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[35].html) + '\n\n' +
                                             str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                        ar[40].html) + '\n\n' +
                                             str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[45].html) + '\n\n' +
                                             str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[50].html) + '\n\n' +
                                             str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[55].html) + '\n\n' +
                                             str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[60].html) + '\n\n' +
                                             str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[65].html) + '\n\n' +
                                             str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[70].html) + '\n\n' +
                                             str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[75].html) + '\n\n' +
                                             str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[80].html) + '\n\n' +
                                             str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[85].html) + '\n\n' +
                                             str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[90].html) + '\n\n' +
                                             str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[95].html) + '\n\n' +
                                             str(ar1[21].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[100].html) + '\n\n' +
                                             str(ar1[22].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[105].html) + '\n\n' +
                                             str(ar1[23].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[110].html) + '\n\n' +
                                             str(ar1[24].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[115].html) + '\n\n' +
                                             str(ar1[25].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[120].html) + '\n\n' +
                                             str(ar1[26].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[125].html) + '\n\n' +
                                             str(ar1[27].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[130].html) + '\n\n' +
                                             str(ar1[28].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[135].html) + '\n\n' +
                                             str(ar1[29].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[140].html) + '\n\n' +
                                             str(ar1[30].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[145].html) + '\n\n' +
                                             str(ar1[31].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[150].html) + '\n\n' +
                                             str(ar1[32].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[155].html) + '\n\n' +
                                             str(ar1[33].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[160].html) + '\n\n' +
                                             str(ar1[34].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[165].html) + '\n\n' +
                                             str(ar1[35].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[170].html) + '\n\n' +
                                             str(ar1[36].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[175].html) + '\n\n' +
                                             str(ar1[37].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[180].html) + '\n\n' +
                                             str(ar1[38].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[185].html) + '\n\n' +
                                             str(ar1[39].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                         ar[190].html) + '\n\n' +
                                             str(ar1[40].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                    195].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>', parse_mode='HTML')
                            except:
                                try:
                                    bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                  ar[0].html) + '\n\n' +
                                                 str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[5].html) + '\n\n' +
                                                 str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[10].html) + '\n\n' +
                                                 str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[15].html) + '\n\n' +
                                                 str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[20].html) + '\n\n' +
                                                 str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[25].html) + '\n\n' +
                                                 str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[30].html) + '\n\n' +
                                                 str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[35].html) + '\n\n' +
                                                 str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                            ar[40].html) + '\n\n' +
                                                 str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[45].html) + '\n\n' +
                                                 str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[50].html) + '\n\n' +
                                                 str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[55].html) + '\n\n' +
                                                 str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[60].html) + '\n\n' +
                                                 str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[65].html) + '\n\n' +
                                                 str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[70].html) + '\n\n' +
                                                 str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[75].html) + '\n\n' +
                                                 str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[80].html) + '\n\n' +
                                                 str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[85].html) + '\n\n' +
                                                 str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[90].html) + '\n\n' +
                                                 str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[95].html) + '\n\n' +
                                                 str(ar1[21].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[100].html) + '\n\n' +
                                                 str(ar1[22].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[105].html) + '\n\n' +
                                                 str(ar1[23].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[110].html) + '\n\n' +
                                                 str(ar1[24].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[115].html) + '\n\n' +
                                                 str(ar1[25].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[120].html) + '\n\n' +
                                                 str(ar1[26].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[125].html) + '\n\n' +
                                                 str(ar1[27].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[130].html) + '\n\n' +
                                                 str(ar1[28].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[135].html) + '\n\n' +
                                                 str(ar1[29].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[140].html) + '\n\n' +
                                                 str(ar1[30].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                             ar[145].html) + '\n\n')
                                except:
                                    try:
                                        bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                            0].html) + '\n\n' +
                                                     str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[5].html) + '\n\n' +
                                                     str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[10].html) + '\n\n' +
                                                     str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[15].html) + '\n\n' +
                                                     str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[20].html) + '\n\n' +
                                                     str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[25].html) + '\n\n' +
                                                     str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[30].html) + '\n\n' +
                                                     str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[35].html) + '\n\n' +
                                                     str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                ar[40].html) + '\n\n' +
                                                     str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[45].html) + '\n\n' +
                                                     str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[50].html) + '\n\n' +
                                                     str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[55].html) + '\n\n' +
                                                     str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[60].html) + '\n\n' +
                                                     str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[65].html) + '\n\n' +
                                                     str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[70].html) + '\n\n' +
                                                     str(ar1[16].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[75].html) + '\n\n' +
                                                     str(ar1[17].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[80].html) + '\n\n' +
                                                     str(ar1[18].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[85].html) + '\n\n' +
                                                     str(ar1[19].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                 ar[90].html) + '\n\n' +
                                                     str(ar1[20].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                            95].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>', parse_mode='HTML')
                                    except:
                                        try:
                                            bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                          ar[
                                                                                                              0].html) + '\n\n' +
                                                         str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                5].html) + '\n\n' +
                                                         str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                10].html) + '\n\n' +
                                                         str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                15].html) + '\n\n' +
                                                         str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                20].html) + '\n\n' +
                                                         str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                25].html) + '\n\n' +
                                                         str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                30].html) + '\n\n' +
                                                         str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                35].html) + '\n\n' +
                                                         str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                40].html) + '\n\n' +
                                                         str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                45].html) + '\n\n' +
                                                         str(ar1[11].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                50].html) + '\n\n' +
                                                         str(ar1[12].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                55].html) + '\n\n' +
                                                         str(ar1[13].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                60].html) + '\n\n' +
                                                         str(ar1[14].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                65].html) + '\n\n' +
                                                         str(ar1[15].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '', ar[
                                                70].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>', parse_mode='HTML')
                                        except:
                                            try:
                                                bot.reply_to(nome,
                                                             str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            0].html) + '\n\n' +
                                                             str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            5].html) + '\n\n' +
                                                             str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            10].html) + '\n\n' +
                                                             str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            15].html) + '\n\n' +
                                                             str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            20].html) + '\n\n' +
                                                             str(ar1[6].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            25].html) + '\n\n' +
                                                             str(ar1[7].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            30].html) + '\n\n' +
                                                             str(ar1[8].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            35].html) + '\n\n' +
                                                             str(ar1[9].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                        ar[
                                                                                                            40].html) + '\n\n' +
                                                             str(ar1[10].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]', '',
                                                                                                         ar[
                                                                                                             45].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                                             parse_mode='HTML')
                                            except:
                                                try:
                                                    bot.reply_to(nome,
                                                                 str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                0].html) + '\n\n' +
                                                                 str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                5].html) + '\n\n' +
                                                                 str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                10].html) + '\n\n' +
                                                                 str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                15].html) + '\n\n' +
                                                                 str(ar1[5].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                            '', ar[
                                                                                                                20].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                                                 parse_mode='HTML')
                                                except:
                                                    try:
                                                        bot.reply_to(nome, str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '', ar[0].html) + '\n\n' +
                                                                     str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '', ar[5].html) + '\n\n' +
                                                                     str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '', ar[10].html) + '\n\n' +
                                                                     str(ar1[4].text) + '\nCPF/CNPJ: ' + re.sub(
                                                            '[^0-9]', '',
                                                            ar[15].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                                                     parse_mode='HTML')
                                                    except:
                                                        try:
                                                            bot.reply_to(nome,
                                                                         str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                             '[^0-9]', '', ar[0].html) + '\n\n' +
                                                                         str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                             '[^0-9]', '', ar[5].html) + '\n\n' +
                                                                         str(ar1[3].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                             '[^0-9]', '', ar[
                                                                                 10].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                                                         parse_mode='HTML')
                                                        except:
                                                            try:
                                                                bot.reply_to(nome,
                                                                             str(ar1[1].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                                 '[^0-9]', '',
                                                                                 ar[0].html) + '\n\n' +
                                                                             str(ar1[2].text) + '\nCPF/CNPJ: ' + re.sub(
                                                                                 '[^0-9]', '',
                                                                                 ar[
                                                                                     5].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                                                             parse_mode='HTML')
                                                            except:
                                                                try:
                                                                    bot.reply_to(nome, str(
                                                                        ar1[1].text) + '\nCPF/CNPJ: ' + re.sub('[^0-9]',
                                                                                                               '',
                                                                                                               ar[
                                                                                                                   0].html) + '\n\n<b>GRUPO: @dkbuscas\nGRUPO²: @dkbuscas3\nCANAL: @dkzrefe</b>',
                                                                                 parse_mode='HTML')
                                                                except:
                                                                    bot.reply_to(nome, '<b>OPS, SEM RESULTADOS!</b>',
                                                                                 parse_mode='HTML')
                    except:
                        bot.reply_to(nome, '<b>ALGO DEU ERRADO :(</b>', parse_mode='HTML')
            else:
                bot.reply_to(nome, '<b>✅ Compre acesso com meu pai @DKZINNBR ✅</b>',
                             parse_mode='HTML')

bot.polling()
