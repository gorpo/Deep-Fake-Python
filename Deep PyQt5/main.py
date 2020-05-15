# coding=utf-8
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QToolTip, QLabel,QLineEdit,QDialog,QFileDialog,QMessageBox,QWidget,QGridLayout
from PyQt5 import QtGui,QtCore
import cv2
import sys
from run import process
import qdarkstyle
import pyimgur
import os
import psutil
from functools import partial
import subprocess
import time
from pyngrok import ngrok

#--inicio do codigo do deep nudes ---------------------------->>>
def main(inputpath):
    outputpath = 'images/renderizada.jpg'
    if isinstance(inputpath, list):
        for item in inputpath:
            watermark = deep_nude_process(item)
            cv2.imwrite("output_" + item, watermark)
    else:
        watermark = deep_nude_process(inputpath)
        cv2.imwrite(outputpath, watermark)

def deep_nude_process(item):
    print('Processing {}'.format(item))
    dress = cv2.imread(item)
    h = dress.shape[0]
    w = dress.shape[1]
    dress = cv2.resize(dress, (512, 512), interpolation=cv2.INTER_CUBIC)
    watermark = process(dress)
    watermark = cv2.resize(watermark, (w, h), interpolation=cv2.INTER_CUBIC)
    return watermark



#------inicio dos demais codigos, o deep nudes vai fica separado ali em cima pq ele é fodão!-----------------------------------------
if __name__ == '__main__':
    imagem_recebida = []
    #robo = None
    def selecionarImagem():
        #app = QApplication(sys.argv)
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('Manicômio | Deep Nude')
        janela2.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        janela2.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela2.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2,"MANICOMIO | DEEP FAKE | Escolha sua imagem", "","All Files (*);;JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            imagem.setPixmap(QtGui.QPixmap(fileName).scaled(800, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            imagemloading.setPixmap(QtGui.QPixmap('images/processando.png').scaled(300, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            #passa o nome da imagem para uma lista para depois recuperar ela
            if fileName in imagem_recebida:
                imagem_recebida.clear()
            else:
                imagem_recebida.clear()
                imagem_recebida.append(fileName)
        caixa_texto_flask.setText('                         Inicie o Processo Deep Nude')  # seta o texto da variavel
        caixa_texto.setText('                      Insira aqui a API do Bot Telegram')

    def salvarImagem():
        janela4 = QWidget()
        janela4.resize(800, 600)
        janela4.move(100, 200)
        janela4.setWindowTitle('Manicômio | Deep Nude')
        janela4.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        #janela.setStyleSheet('QWidget {background:#2d2e2d}')
        janela4.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela4.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(janela4,"MANICOMIO | DEEP FAKE | Salvar sua imagem","renderizada","JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            print(fileName)

    def imageur():
        CLIENT_ID = "ebfc2558bda96e5"
        PATH1 = 'images/renderizada.jpg'
        PATH2 = imagem_recebida[0]
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH1, title="DEEP FAKE | Pyimageupload")
        link1 = uploaded_image.link
        #texto_link1 = f"<a href=\"{link1}\"><font color=black>Click to Share!</font></a>"
        #label_link.setText(texto_link1)
        caixa_texto_flask.setText(link1)  # seta o texto da variavel
        uploaded_image_original = im.upload_image(PATH2, title="DEEP FAKE | Pyimageupload")
        link2 = uploaded_image_original.link
        texto = f'----->\nOriginal: {link2}\nNude: {link1}\n'
        escrever = open('links_salvos.txt', 'a')
        escrever.write(texto)
        escrever.close()

    def deepNudes(imagem_recebida):
        #caixa_texto_flask.setText('                         Processo Deep Nude Finalizado.')  # seta o texto da variavel
        caixa_texto.setText('                      Insira aqui a API do Bot Telegram')
        main(imagem_recebida[0])        #executa o deep nudes importado
        imagemloading.setPixmap(QtGui.QPixmap('images/renderizada.jpg').scaled(800, 450,QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
        imageur()

    def caixa_mensagem():
        janela3 = QWidget()
        janela3.resize(800, 600)
        janela3.move(100, 200)
        janela3.setWindowTitle('Manicômio | Deep Nude')
        janela3.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        janela3.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela3.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        Reply = QMessageBox.question(janela3,'MANICOMIO DEEP FAKE | AVISO | LEIA COM ATENÇÃO', "Este programa pode levar muito tempo processando os dados, mesmo que pareça travado ele ainda esta processando.Aconselhamos o uso de CUDA Core para acelerar o processamento. Não nos responsabilizamos pelo conteudo criado com este programa! Salientamos que este programa foi criado apenas com fins acadêmicos e para aprendizado de IA, Machine e Deep Learning.\n Clicando em Sim você concorda em rodar o programa.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if Reply == QMessageBox.Yes:
            deepNudes(imagem_recebida)
            caixa_mensagem2()
        else:
            print('No clicked.')
        janela3.show()

    def caixa_mensagem2():
        janela3a = QWidget()
        janela3a.resize(800, 600)
        janela3a.move(100, 200)
        janela3a.setWindowTitle('Manicômio | Deep Nude')
        janela3a.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        janela3a.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela3a.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        Reply = QMessageBox.question(janela3a,'MANICOMIO DEEP FAKE | SALVAR | PROSSEGUIR', "Foi gerado um link de sua imagem!\nPara salvar sua imagem clique em SIM ou clique em Não para prosseguir", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if Reply == QMessageBox.Yes:
            salvarImagem()
        else:
            print('No clicked.')
        janela3a.show()

    def ativaBot():
        if caixa_texto.text() == '':
            api = 'sua_api'
            caixa_texto.setText('                       Bot Ativado, confira o Telegram.')
            caixa_texto_flask.setText('                     Para parar o Bot feche o programa.')  # seta o texto da variavel
            imagemloading.setPixmap(QtGui.QPixmap('images/telegram.png').scaled(300, 450,QtCore.Qt.KeepAspectRatio))
            ler = open('opencv_transform/base_bot.txt', 'r')
            lido = ler.read()
            trocar = 'replace'
            gravacao = lido.replace(trocar,api)
            gravar = open('opencv_transform/bot.py', 'w')
            gravar.write(gravacao)
            ler.close()
            gravar.close()
            time.sleep(3)
            #abre o bot
            subprocess.Popen('python opencv_transform/bot.py', stdout=subprocess.PIPE)
        else:
            api = caixa_texto.text()  # le oque foi escrito na caixa de texto
            api_stripada = api.strip()
            caixa_texto.setText('                       Bot Ativado, confira o Telegram.')
            caixa_texto_flask.setText('      Para parar o Bot ou caso de erro feche o programa.')  # seta o texto da variavel
            imagemloading.setPixmap(QtGui.QPixmap('images/telegram.png').scaled(300, 450, QtCore.Qt.KeepAspectRatio))
            # pega os dados em um documento de texto e cria o bot com a API
            ler = open('opencv_transform/base_bot.txt', 'r')
            lido = ler.read()
            trocar = 'replace'
            gravacao = lido.replace(trocar, api_stripada)
            gravar = open('opencv_transform/bot.py', 'w')
            gravar.write(gravacao)
            ler.close()
            gravar.close()
            time.sleep(3)
            # abre o bot
            subprocess.Popen('python opencv_transform/bot.py', stdout=subprocess.PIPE)


    def serverFlask():
        imagemloading.setPixmap(QtGui.QPixmap('images/flask.png').scaled(300, 450, QtCore.Qt.KeepAspectRatio))
        caixa_texto_flask.setText('             Servidor iniciado:    http://127.0.0.1:5000/')  # seta o texto da variavel

        subprocess.Popen('python ../deepnude_flask/deepnude_flask.py', stdout=subprocess.PIPE)
        link_ngrok = ngrok.connect(80)
        print(f'Link compartilhavel: {link_ngrok}')
        caixa_texto.setText(f'           Link externo:    {link_ngrok}')




    #--------------------------inicio da janela com PyQt5 ---------------------------------------------------------------------------------------------->
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setFixedSize(800,600)
    janela.move(100,200)
    janela.setWindowTitle('Manicômio | Deep Nude')
    janela.setWindowIcon(QtGui.QIcon('images/icon.ico'))
    janela.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    janela.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    # label fixa na tela TOPO ------------------------------>>>
    label1 = QLabel(janela)
    label1.setText('Manicômio | Deep Nude')
    label1.move(275, 10)
    label1.resize(450, 60)
    label1.setPixmap(QtGui.QPixmap('images/logo.png'))
    #label1.setStyleSheet('QLabel {color:#ffffff; font: bold 20px arial }')




    # imagem de entrada
    imagem = QLabel(janela)
    imagem.move(57, 110)
    imagem.resize(300, 430)
    imagem.setPixmap(QtGui.QPixmap('images/bg1.png'))


    # imagem do final
    imagemloading = QLabel(janela)
    imagemloading.move(430, 110)
    imagemloading.resize(300, 430)
    imagemloading.setPixmap(QtGui.QPixmap('images/bg2.png'))

    # botao 1 ----------->>>>------------------------------------------------------------------
    botao1 = QPushButton('imagem',janela)
    botao1.move(57, 90)
    botao1.resize(300, 30)
    botao1.setStyleSheet('QPushButton{background-color:#313332;color:#19232d;font-style: None;font-weight: bold;font-size: 20px;font-family: arial}')  # css
    botao1.clicked.connect(selecionarImagem)
    botao1.setToolTip('Clique no botão imagem para carregar sua foto\nCarregue apenas fotos de pessoas com bikini ou roupas intimas\nDepois clique no botão Deep Nude para iniciar o processo de codificação\nTodo processo de Deep Learning será automatizado e entregue assim que pronto.')

    # botao 2 ----------->>>>-------------------------------------------------------------------------
    botao2 = QPushButton('deep nude',janela)
    botao2.move(430, 90)
    botao2.resize(300, 30)
    botao2.setStyleSheet('QPushButton{background-color:#313332;color:#19232d;font: bold 20px arial }')  # css melhorado
    botao2.clicked.connect(caixa_mensagem)   #partial(função,parametro) #partial(deepNudes,imagem_recebida)
    botao2.setToolTip('Após carregar sua imagem basta clicar em deep nude\n e esperar o processo de deep learning ser concluído.')
    # caixa de texto
    caixa_texto = QLineEdit(janela)
    #caixa_texto.setText('')
    caixa_texto.setText('                      Insira aqui a API do Bot Telegram')
    caixa_texto.move(57, 565)
    caixa_texto.resize(300, 30)
    caixa_texto.setStyleSheet('QLineEdit{ text-align: center;}')#margin-left: 400px; margin-right: 1px;
    caixa_texto.setToolTip('Insira o Token do seu Bot do Telegram na coluna\nClique no botão telegram para ativar o bot\nCaso use o Servidor Flask esta coluna irá te retornar\num endereço do Ngrok com um link externo compartilhavel!')



    # botao 3 ----------->>>>-------------------------------------------------------------------------
    botao3 = QPushButton(janela)
    botao3.setText('telegram')
    botao3.move(57, 530)
    botao3.resize(300, 30)
    botao3.setStyleSheet('QPushButton{background-color:#313332;color:#19232d;font: bold 20px arial }')  # css melhorado
    botao3.clicked.connect(ativaBot)  # partial(função,parametro) #partial(deepNudes,imagem_recebida)
    botao3.setToolTip('Primeiro insira o seu Token do Bot do Telegram na coluna abaixo\nDepois clique neste botão para ativar o bot, confira no privado do bot se ele se encontra ativo!')

    # caixa de texto
    caixa_texto_flask = QLineEdit(janela)
    caixa_texto_flask.setText('Suba uma imagem, ative o flask ou troque a API Telegram.')
    caixa_texto_flask.move(430, 565)
    caixa_texto_flask.resize(300, 30)
    caixa_texto_flask.setStyleSheet('QLineEdit{ text-align: center;}')  # margin-left: 400px; margin-right: 1px;
    caixa_texto_flask.text()  # le oque foi escrito na caixa de texto
    caixa_texto_flask.setToolTip('Esta caixa de texto irá retornar dados de IP e Porta do Servidor Flask e outras informações.')

    # botao 4 ----------->>>>-------------------------------------------------------------------------
    botao4 = QPushButton('server flask', janela)
    botao4.move(430, 530)
    botao4.resize(300, 30)
    botao4.setStyleSheet('QPushButton{background-color:#313332;color:#19232d;font: bold 20px arial }')  # css melhorado
    botao4.clicked.connect(serverFlask)  # partial(função,parametro) #partial(deepNudes,imagem_recebida)
    botao4.setToolTip('Clicando neste botão o Servidor Flask é ativado\nO servidor irá retornar dois endereços e portas\nUm endereço local e porta será retornado para navegação interna mais rápida\nUm endereço do Ngrok com link temporario para compartilhamento externo!')



    #exibe a janela com as porcaria tudo dentro!!!
    janela.show()
    sys.exit(app.exec_())
