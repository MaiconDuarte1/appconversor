#INCLUSÃO DE BIBLIOTECAS
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import customtkinter as ct
import os
from CONVERTER import funcoes as f

resolucoes = ["144p", "240p", "360p", "480p", "720p", "1080p"]


# CONFIGURAÇÕES INICIAIS
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
janela = ct.CTk()
janela.title("APP CONVERSOR 1.5")
janela.resizable(False, False)
janela.geometry("640x480")
janela.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/converter.ico")

tabview = ct.CTkTabview(janela, width=640, height=440)
tabview.grid()
tabview.add("YOUTUBE")
tabview.add("MP4 PARA MP3")
tabview.add("OPÇÕES")
tabview.tab("YOUTUBE")
tabview.tab("MP4 PARA MP3")
tabview.tab("OPÇÕES")

#CONFIGURAÇÃO DA JANELA PRINCIPAL

label_textomensagem = ct.CTkLabel(tabview.tab("YOUTUBE"), text="INSIRA O LINK DO YOUTUBE:", font=("Impact", 22))
label_textomensagem.place(x=197, y=15)

caixa_texto = ct.CTkEntry(tabview.tab("YOUTUBE"), width=325, height=27)
caixa_texto.place(x=150, y=50)

label_textores = ct.CTkLabel(tabview.tab("YOUTUBE"), text="SELECIONE A RESOLUÇÃO DESEJADA:", font=("Impact", 17))
label_textores.place(x=195, y=85)

combobox_res = ct.CTkComboBox(tabview.tab("YOUTUBE"), values=resolucoes, width=325, height=27)
combobox_res.place(x=150, y=120)

label_localsalvar = ct.CTkLabel(tabview.tab("YOUTUBE"), text="SALVAR EM:", font=("Impact", 17))
label_localsalvar.place(x=275, y=155)

botao_localsalvar = ct.CTkButton(tabview.tab("YOUTUBE"), text="DIRETÓRIO", command=f.botaodiretorio, width=325, height=27)
botao_localsalvar.place(x=150, y=190)

meu_dir = ''
label_direscolhido = ct.CTkLabel(tabview.tab("YOUTUBE"), text=meu_dir)
label_direscolhido.place(x=225, y=225)


botao_paramp3 = ct.CTkButton(tabview.tab("YOUTUBE"), text="CONVERTER PARA MP3", command=f.youtubeparamp3, width=250, height=27)
botao_paramp3.place(x=50, y=255)

botao_paramp4 = ct.CTkButton(tabview.tab("YOUTUBE"), text="CONVERTER PARA MP4", command=f.youtubeparamp4, width=250, height=27)
botao_paramp4.place(x=315, y=255)


#CONFIGURAÇÃO DA JANELA DE CONVERSÃO DE MP4 PARA MP3

label_selectarquivo = ct.CTkLabel(tabview.tab("MP4 PARA MP3"), text="SELECIONE O ARQUIVO PARA CONVERSÃO:", font=("Impact", 22))
label_selectarquivo.place(x=145, y=25)


botao_selectarquivo = ct.CTkButton(tabview.tab("MP4 PARA MP3"), text="SELECIONAR ARQUIVO", width=325, height=27, command=f.mp4paramp3)
botao_selectarquivo.place(x=155, y=75)


#CONFIGURAÇÃO DA JANELA DE OPÇÕES

label_textmensagemOP = ct.CTkLabel(tabview.tab("OPÇÕES"), text="MODO DE APARENCIA", font=("Impact", 22))
label_textmensagemOP.place(x=225, y=15)

menu_opcoes = ct.CTkOptionMenu(tabview.tab("OPÇÕES"), values=["Dark", "Light", "System"], width=325, height=27, command=f.change_appearance_mode_event)
menu_opcoes.place(x=150, y=50)

label_textsobreOP = ct.CTkLabel(tabview.tab("OPÇÕES"), text="Aplicativo Desenvolvido Por Python Júnior", font=("Impact", 22))
label_textsobreOP.place(x=130, y=85)

label_textsobreOP2 = ct.CTkLabel(tabview.tab("OPÇÕES"), text="Versão Alpha 1.5", font=("Impact", 22))
label_textsobreOP2.place(x=235, y=120)
