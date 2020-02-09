import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://imgnews.naver.net/image/5301/2019/11/28/0000010729_001_20191128172202667.jpeg"
htmlURL ="http://google.com"

savePath1="C:/section2/pengsu.jpg"
savePath2="C:/section2/index.html"

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb')
saveFile1.write(f1)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print('다운로드 완료')
