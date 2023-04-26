#INCLUSÃO DE BIBLIOTECAS
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import customtkinter as ct
import os
from CONVERTER import funcoes as f


# CONFIGURAÇÕES INICIAIS
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
janela = ct.CTk()
janela.title("APP CONVERSOR 1.0")
janela.resizable(False, False)
janela.geometry("315x350")
janela.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/converter.ico")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

tabview = ct.CTkTabview(janela, width=307, height=310)
tabview.grid()
tabview.add("YOUTUBE")
tabview.add("MP4 PARA MP3")
tabview.add("OPÇÕES")
tabview.tab("YOUTUBE").grid_columnconfigure(0, weight=1)
tabview.tab("MP4 PARA MP3").grid_columnconfigure(0, weight=1)
tabview.tab("OPÇÕES").grid_columnconfigure(0, weight=1)

#CONFIGURAÇÃO DA JANELA PRINCIPAL

label_textomensagem = ct.CTkLabel(tabview.tab("YOUTUBE"), text="INSIRA O LINK DO YOUTUBE:")
label_textomensagem.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

caixa_texto = ct.CTkEntry(tabview.tab("YOUTUBE"))
caixa_texto.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

label_localsalvar = ct.CTkLabel(tabview.tab("YOUTUBE"), text="SALVAR EM:")
label_localsalvar.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

botao_localsalvar = ct.CTkButton(tabview.tab("YOUTUBE"), text="DIRETÓRIO", command=f.botaodiretorio)
botao_localsalvar.grid(row=3, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

meu_dir = ''
label_direscolhido = ct.CTkLabel(tabview.tab("YOUTUBE"), text=meu_dir)
label_direscolhido.grid(row=4, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

botao_paramp3 = ct.CTkButton(tabview.tab("YOUTUBE"), text="CONVERTER PARA MP3", command=f.youtubeparamp3)
botao_paramp3.grid(row=5, column=0, sticky='nsew')

botao_paramp4 = ct.CTkButton(tabview.tab("YOUTUBE"), text="CONVERTER PARA MP4", command=f.youtubeparamp4)
botao_paramp4.grid(row=5, column=1, sticky='nsew')

#CONFIGURAÇÃO DA JANELA DE CONVERSÃO DE MP4 PARA MP3

label_selectarquivo = ct.CTkLabel(tabview.tab("MP4 PARA MP3"), text="SELECIONE O ARQUIVO PARA CONVERSÃO:")
label_selectarquivo.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

botao_selectarquivo = ct.CTkButton(tabview.tab("MP4 PARA MP3"), text="SELECIONAR ARQUIVO", command=f.mp4paramp3)
botao_selectarquivo.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

#CONFIGURAÇÃO DA JANELA DE OPÇÕES

label_textmensagemOP = ct.CTkLabel(tabview.tab("OPÇÕES"), text="MODO DE APARENCIA")
label_textmensagemOP.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

menu_opcoes = ct.CTkOptionMenu(tabview.tab("OPÇÕES"), values=["Dark", "Light", "System"], command=f.change_appearance_mode_event)
menu_opcoes.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

label_textsobreOP = ct.CTkLabel(tabview.tab("OPÇÕES"), text="Aplicativo Desenvolvido Por Python Júnior")
label_textsobreOP.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

label_textsobreOP2 = ct.CTkLabel(tabview.tab("OPÇÕES"), text="Versão Beta 1.0")
label_textsobreOP2.grid(row=3, column=0, padx=10, pady=10, columnspan=3)