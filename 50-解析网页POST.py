#coding = utf-8
import urllib.request
import urllib.parse


data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = data.encode('ascii')

with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:
    print(f.read().decode('utf-8'))