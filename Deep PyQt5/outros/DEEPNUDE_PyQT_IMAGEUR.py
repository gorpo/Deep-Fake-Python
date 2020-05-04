
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QToolTip, QLabel,QLineEdit,QDialog,QFileDialog,QMessageBox,QWidget,QGridLayout
from PyQt5 import QtGui,QtCore
# coding=utf-8
import cv2
import sys
from run import process
from functools import partial
import qdarkstyle


#--inicio do codigo do deep nudes ---------------------------->>>
def main(inputpath):
    outputpath = 'renderizada.jpg'
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


#------inicio dos demais codigos, o deep nudes vai fica separado ali em cima pq ele é fodão!
if __name__ == '__main__':

    imagem_recebida = []
    def selecionarImagem():
        #app = QApplication(sys.argv)
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('Manicômio | Deep Nude')
        janela2.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        #janela.setStyleSheet('QWidget {background:#2d2e2d}')
        # setup stylesheet
        janela2.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela2.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        #QfileDialog, abre uma janela de dialogo e quando selecionado algo retorna ele basta dar um print em filename.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(janela2,"MANICOMIO | DEEP FAKE | Escolha sua imagem", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            #muda a imagem de entrada
            imagem.setPixmap(QtGui.QPixmap(fileName).scaled(300, 400, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            imagemloading.setPixmap(QtGui.QPixmap('images/processando.png').scaled(300, 400, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            #passa o nome da imagem para uma lista para depois recuperar ela
            imagem_recebida.append(fileName)

    def salvarImagem():
        janela4 = QWidget()
        janela4.resize(800, 600)
        janela4.move(100, 200)
        janela4.setWindowTitle('Manicômio | Deep Nude')
        janela4.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        #janela.setStyleSheet('QWidget {background:#2d2e2d}')
        # setup stylesheet
        janela4.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela4.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(janela4,"QFileDialog.getSaveFileName()","renderizada","JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            print(fileName)

    def deepNudes(imagem_recebida):
        #executa o deep nudes importado
        main(imagem_recebida[0])
        #muda a imagem na segunda label
        imagemloading.setPixmap(QtGui.QPixmap('renderizada.jpg').scaled(300, 400,QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)

    def caixa_mensagem():
        janela3 = QWidget()
        janela3.resize(800, 600)
        janela3.move(100, 200)
        janela3.setWindowTitle('Manicômio | Deep Nude')
        janela3.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        #janela3.setStyleSheet('QWidget {background:#2d2e2d}')
        # setup stylesheet
        janela3.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        janela3.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        Reply = QMessageBox.question(janela3,'MANICOMIO DEEP FAKE | AVISO | LEIA COM ATENÇÃO', "Este programa pode levar muito tempo processando os dados, mesmo que pareça travado ele ainda esta processando.Aconselhamos o uso de CUDA Core para acelerar o processamento. Não nos responsabilizamos pelo conteudo criado com este programa! Salientamos que este programa foi criado apenas com fins acadêmicos e para aprendizado de IA, Machine e Deep Learning.\n Clicando em Sim você concorda em rodar o programa.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if Reply == QMessageBox.Yes:
            deepNudes(imagem_recebida)
            salvarImagem()
        else:
            print('No clicked.')
        janela3.show()


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
    # label fixa na tela ------------------------------>>>
    label1 = QLabel(janela)
    label1.setText('Manicômio | Deep Nude')
    label1.move(300, 10)
    label1.setStyleSheet('QLabel {color:#ffffff; font: bold 20px arial }')
    label1.resize(450, 22)

    # botao 1 ----------->>>>------------------------------------------------------------------
    botao1 = QPushButton('imagem',janela)
    botao1.move(125, 70)
    botao1.resize(150, 30)
    botao1.setStyleSheet('QPushButton{background-color:#313332;color:#ffffff;font-style: None;font-weight: bold;font-size: 20px;font-family: arial}')  # css
    botao1.clicked.connect(selecionarImagem)

    # botao 2 ----------->>>>-------------------------------------------------------------------------
    botao2 = QPushButton('executar',janela)
    botao2.move(505, 70)
    botao2.resize(150, 30)
    botao2.setStyleSheet('QPushButton{background-color:#313332;color:#ffffff;font: bold 20px arial }')  # css melhorado
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
