import math
import datetime

# [機能A]@アリス担当 #############


# [機能B]@ボブ担当 ###############
def func_B ():
  t1 = datetime.datetime.now() # 現在時刻
  t2 = datetime.datetime(2023,11,4,10,00,00) # 11/4 10:00
  diff = t2 - t1
  days = diff.days
  hours= diff.seconds // 3600
  print('高専祭まで、あと',end='')
  print(days,end='')
  print('日と',end='')
  print(hours,end='')
  print('時間')

# メイン処理 ####################
if __name__ == "__main__": 

  print("start.")

  ## 機能Aの実行

  ## 機能Bの実行
  func_B()

  print("end.")