import math
import datetime

# [機能A]@アリス担当 #############


# [機能B]@ボブ担当 ###############
def func_B ():
  t = datetime.datetime(2023,11,4,10,00,00) # 11/4 10:00
  diff = t - datetime.datetime.now()
  days = diff.days
  hours= diff.seconds // 3600
  print(f'高専祭まで、あと{days}日と{hours}時間')

# メイン処理 ####################
if __name__ == "__main__": 

  print("start.")

  ## 機能Aの実行

  ## 機能Bの実行
  func_B()

  print("end.")