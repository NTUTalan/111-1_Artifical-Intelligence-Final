# 路徑規劃
## 資料夾說明
ai_map: 存地圖的地方  
solutions: 存結果的地方，有Astar跟Greedy
## 各個Python檔使用說明
- readmap.py  
`py readmap.py 地圖名稱`

- Astar-loop.py 用Astar演算法尋找路徑  
`py Astar-loop.py 地圖名稱`, 結果會存在 solutions/Astar/  
Ex: `py Astar-loop.py small-easy`

- Greedy-loop.py 用Greedy演算法尋找路徑  
`py Greedy-loop.py 地圖名稱`, 結果會存在 solutions/Greedy/  
Ex: `py Greedy-loop.py small-medium`

- convert.py 將結果.csv轉成.png  
`py convert.py /使用演算法/地圖名稱`  
Ex: `py convert.py /Astar/big-easy`