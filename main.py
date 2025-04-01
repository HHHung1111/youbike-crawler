import requests
import pandas as pd
from datetime import datetime

# 抓特定行政區的即時資料
target_areas = ["大安區", "松山區", "信義區", "中正區"]

url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
res = requests.get(url)
data = res.json()
df_all = pd.DataFrame(data)

target_stations = df_all[df_all["sarea"].isin(target_areas)]["sna"].unique().tolist()
df_filtered = df_all[df_all["sna"].isin(target_stations)].copy()

now = datetime.now()
df_filtered["record_time"] = now.strftime("%Y-%m-%d %H:%M:%S")

filename = f"youbike_{now.strftime('%Y%m%d_%H%M')}.csv"
df_filtered.to_csv(filename, index=False, encoding="utf-8-sig")

print(f"✅ 寫入完成：{filename}，共 {len(df_filtered)} 筆資料")
