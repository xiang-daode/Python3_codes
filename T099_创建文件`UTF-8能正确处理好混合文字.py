# 在这里写上你的代码 :-)
text = 'UTF-8能正确处理好混合文字,如中文、にほんご、한국어'
with open('T099test.txt','w',encoding='utf-8') as f: # 建议保存为utf-8编码
    f.write(text)
