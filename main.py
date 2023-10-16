import math
import datetime
import fractions

# [機能A]@アリス担当 #############
def func_A ():
  print('func_A called.')

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
def func_A ():
  f = fractions.Fraction
  t1 = f(2,3)
  t2 = f(4,6)
  ans = t1 + t2
  print(f'{t1} + {t2} = {ans} (= {float(ans):.2f})')
  
  ## 機能Bの実行
  func_B()

  print("end.")