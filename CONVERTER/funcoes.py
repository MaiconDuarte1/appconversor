from CONVERTER import frontend
import moviepy.editor as mp
import pytube
import os
import winotify

def botaodiretorio():
    local = frontend.filedialog.askdirectory()
    frontend.label_direscolhido.configure(text=local)


def change_appearance_mode_event(new_appearance_mode: str):
    frontend.ct.set_appearance_mode(new_appearance_mode)


def mp4paramp3():
    arquivo = frontend.filedialog.askopenfilename()
    arquivo_mp4 = arquivo
    arquivo_mp3 = f"{arquivo}.mp3"

    videoclipe = mp.VideoFileClip(arquivo_mp4)
    videofinal = videoclipe.audio
    videofinal.write_audiofile(arquivo_mp3)
    videofinal.close()
    videoclipe.close()


    notificacao = winotify.Notification(
        app_id="APP CONVERSOR 1.0",
        title="NOTIFICAÇÃO",
        msg="Conversão Concluída Com Sucesso!!!",
        duration="long",
        icon=os.path.dirname(os.path.abspath(__file__))+"/convertok.ico"
    )
    notificacao.set_audio(winotify.audio.Default, loop=False)
    notificacao.show()



def youtubeparamp4():
    link = frontend.caixa_texto.get()
    pasta = frontend.label_direscolhido.cget("text")
    pytube.YouTube(link).streams.get_highest_resolution().download(pasta)


    
    notificacao = winotify.Notification(
        app_id="APP CONVERSOR 1.0",
        title="NOTIFICAÇÃO",
        msg="Download Concluído Com Sucesso!!!",
        duration="long",
        icon=os.path.dirname(os.path.abspath(__file__))+"/downloadicon.ico"
    )
    notificacao.set_audio(winotify.audio.Default, loop=False)
    notificacao.show()



def youtubeparamp3():
    link = frontend.caixa_texto.get()
    caminho = frontend.label_direscolhido.cget("text")
    yt = pytube.YouTube(link)
    yt = yt.streams.filter(only_audio=True).first().download(caminho)
    novo_nome = os.path.splitext(yt)
    os.rename(yt, novo_nome[0]+'.mp3')


    notificacao = winotify.Notification(
        app_id="APP CONVERSOR 1.0",
        title="NOTIFICAÇÃO",
        msg="Download Concluído Com Sucesso!!!",
        duration="long",
        icon=os.path.dirname(os.path.abspath(__file__))+"/downloadicon.ico"
    )
    notificacao.set_audio(winotify.audio.Default, loop=False)
    notificacao.show()