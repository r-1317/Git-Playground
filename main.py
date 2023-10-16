import math
import fractions

# [機能A]@アリス担当 #############
def func_A ():
  print('func_A called.')

# [機能B]@ボブ担当 ###############


# メイン処理 ####################
if __name__ == "__main__": 

  print("start.")

  ## 機能Aの実行
def func_A ():
  ans = fractions.Fraction(2,3)+fractions.Fraction(4,6)
  print(f'2/3 + 4/6 = {ans} (= {float(ans):.2f})')  
  
  ## 機能Bの実行

  print("end.")