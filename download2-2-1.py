import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="http://imgnews.naver.net/image/5301/2019/11/28/0000010729_001_20191128172202667.jpeg"
htmlURL ="http://google.com"

savePath1="C:/section2/pengsu.jpg"
savePath2="C:/section2/index.html"

urllib.request.urlretrieve(imgUrl,savePath1)
urllib.request.urlretrieve(imgUrl,savePath2)


print('다운로드 완료')
