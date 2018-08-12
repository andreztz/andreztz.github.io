Libvlc é biblioteca por traz do VLC, ela uma biblioteca estável e funcional, disponível 
para praticamente todas as plataformas. Mais recentemente sua licença foi 
alterada da GPL para LGPL, permitindo o seu uso em projetos proprietários. Ao contrário de 
outras bibliotecas de reprodução de áudio, a libvlc está bem documentada, tornando-a 
particularmente boa para iniciantes. 

A cada release da libvlc, automaticamente é gerado "Python bindings". Estes bindings são baseados em 
ctypes o que permitem que eles sejam usados com pypy e outras implementações do python.


Do mesmo modo que a libvlc prove suporte para codecs e formatos ao tocador VLC, tambem simplifica 
o processo de reprodução de praticamente qualquer formato usando "python bindings"


O primeiro passo é instalar o python-vlc em nosso projeto.


Podemos então importar o vlc e começar a usá-lo.

.. code-block:: python

    import vlc

    instance = vlc.Instance()

    media = instance.media_new('teste.mp3')

    player.set_media(media)

    player.play()



http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

wget --output-document vlc.py "http://git.videolan.org/?p=vlc/bindings/python.git;a=blob_plain;f=generated/vlc.py;hb=HEAD"

http://git.videolan.org/?p=vlc/bindings/python.git;a=summary


