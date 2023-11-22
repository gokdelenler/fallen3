# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from FallenMusic import BOT_NAME

PM_START_TEXT = """
merhaba {0}, 🥀
๏ benim adım** {1} !

➻ hızlı ve güçlü bir müzik çalar botu.
"""

START_TEXT = """
**merhaba** {0}, 🥀
  {1} artık şarkıları çalabilirim {2}.

──────────────────
➻ hakımda yardım almak için veya soru sormak için destek sohbetime [katılabilirsiniz]({3}).
"""

HELP_TEXT = f"""
<u>❄ **kulanıcılar için kulanılabilen komutlar {BOT_NAME} :**</u>

๏ /play : müziği oynatmaya yarar.
๏ /duraklat : oynatmayı duraklatın.
๏ /devam : duraklamayı devam etir.
๏ /atla : devam eden müziği bir sonrakine atlayın.
๏ /dur : müziği durdurur.
๏ /ping : botun sistem istatistiklerini görmek içindir.
๏ /adminlist : botun admin listesini gösterir.

๏ /indir : istenilen şarkıyı indirir.
๏ /ara : istediğiniz şarkıyı YouTube de aramak içindir.
"""

HELP_SUDO = f"""
<u>✨ **admin komutları {BOT_NAME} :**</u>

๏ /activevc : aktif olan sesli sohbetlerin listesini gösterir.
๏ /eval or /sh : verilen codu botun terminalinde çalıştırır.
๏ /speedtest : botun sunucu istatistiklerini verir.
๏ /sysstats : botun sistem istatistiklerini verir.

๏ /setname [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ɴᴀᴍᴇ.
๏ /setbio [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙɪᴏ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /setpfp [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /delpfp : ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
"""

HELP_DEV = f"""
<u>✨ **sahip komutları {BOT_NAME} :**</u>

๏ /config : botun tüm yapılandırma değişkenlerini almak içindir.
๏ /broadcast : reklam komutu
๏ /rmdownloads : botun sunucusuna indirilen ön bellek dosyalarını temizler.
๏ /leaveall : asistan hesabına tüm sesli sohbetleri bırakmasını emreder.
๏ /addsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ᴀᴅᴅ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
๏ /rmsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʀᴇᴍᴏᴠᴇ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
"""
