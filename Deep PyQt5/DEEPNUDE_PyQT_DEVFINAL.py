
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QToolTip, QLabel,QLineEdit,QDialog,QFileDialog,QMessageBox,QWidget,QGridLayout
from PyQt5 import QtGui,QtCore
# coding=utf-8
import cv2
import sys
from run import process
import qdarkstyle
import pyimgur


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
            imagem.setPixmap(QtGui.QPixmap(fileName).scaled(300, 400, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            imagemloading.setPixmap(QtGui.QPixmap('images/processando.png').scaled(300, 400, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            #passa o nome da imagem para uma lista para depois recuperar ela
            if fileName in imagem_recebida:
                imagem_recebida.clear()
            else:
                imagem_recebida.clear()
                imagem_recebida.append(fileName)

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
        texto_link1 = f"<a href=\"{link1}\"><font color=black>Click to Share!</font></a>"
        label_link.setText(texto_link1)
        uploaded_image_original = im.upload_image(PATH2, title="DEEP FAKE | Pyimageupload")
        link2 = uploaded_image_original.link

        texto = f'----->\nOriginal: {link2}\nNude: {link1}\n'
        escrever = open('links_salvos.txt', 'a')
        escrever.write(texto)
        escrever.close()


    def deepNudes(imagem_recebida):
        main(imagem_recebida[0])        #executa o deep nudes importado
        imagemloading.setPixmap(QtGui.QPixmap('images/renderizada.jpg').scaled(300, 400,QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
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



    #---inicio da janela com PyQt5 ---------------------------------------------------------------------------------------------->
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.resize(800, 600)
    janela.move(100,200)
    janela.setWindowTitle('Manicômio | Deep Nude')
    janela.setWindowIcon(QtGui.QIcon('images/icon.ico'))
    #janela.setStyleSheet('QWidget {background:#2d2e2d}')
    # setup stylesheet
    janela.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    janela.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    # label fixa na tela TOPO ------------------------------>>>
    label1 = QLabel(janela)
    label1.setText('Manicômio | Deep Nude')
    label1.move(275, 3)
    label1.resize(450, 60)
    label1.setPixmap(QtGui.QPixmap('images/logo.png'))
    #label1.setStyleSheet('QLabel {color:#ffffff; font: bold 20px arial }')


    # label link imageur ------------------------------>>>
    label_link = QLabel(janela)
    url = ''
    label_link.setText(url)
    label_link.move(340, 560)
    label_link.setStyleSheet('QLabel {color:#ffffff; font: bold 15px arial }')
    label_link.resize(450, 22)
    label_link.setOpenExternalLinks(True)
    # botao 1 ----------->>>>------------------------------------------------------------------
    botao1 = QPushButton('imagem',janela)
    botao1.move(125, 70)
    botao1.resize(150, 30)
    botao1.setStyleSheet('QPushButton{background-color:#313332;color:#19232d;font-style: None;font-weight: bold;font-size: 20px;font-family: arial}')  # css
    botao1.clicked.connect(selecionarImagem)

    # botao 2 ----------->>>>-------------------------------------------------------------------------
    botao2 = QPushButton('executar',janela)
    botao2.move(505, 70)
    botao2.resize(150, 30)
    botao2.setStyleSheet('QPushButton{background-color:#313332;color:#19232d;font: bold 20px arial }')  # css melhorado
    botao2.clicked.connect(caixa_mensagem)   #partial(função,parametro) #partial(deepNudes,imagem_recebida)

    # imagem de entrada
    imagem = QLabel(janela)
    imagem.move(57, 120)
    imagem.resize(300, 430)
    imagem.setPixmap(QtGui.QPixmap('images/bg1.png'))

    # imagem do final
    imagemloading = QLabel(janela)
    imagemloading.move(430, 120)
    imagemloading.resize(300, 430)
    imagemloading.setPixmap(QtGui.QPixmap('images/bg2.png'))




    #exibe a janela com as porcaria tudo dentro!!!
    janela.show()
    sys.exit(app.exec_())
