import math

input_angle = float(input('角度を入力してください（度）：'))
rad = math.radians(input_angle)
print("{}度->{}ラジアン".format(input_angle, rad))
print("sin({})=>{}".format(input_angle, math.sin(rad)))
