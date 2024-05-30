# def printer(num):
#   hang_man = """
#         _______
#        |/      |
#        |      (_)
#        |      \\|/
#        |       |
#        |      / \\
#        |
#   _____|______
#   """
#   if num == 1:
#       print(hang_man[0:20])
#       return hang_man[0:20]
#   elif num == 2:
#       print(hang_man[0:30])
#       return hang_man[0:30]
#   elif num == 3:
#       print(hang_man[0:40])
#       return hang_man[0:40]
#   elif num == 4:
#       print(hang_man[0:50])
#       return hang_man[0:50]
#   elif num == 5:
#       print(hang_man[0:60])
#       return hang_man[0:60]
#   elif num == 6:
#       print(hang_man[0:70])
#       return hang_man[0:70]
#   elif num == 7:
#       print(hang_man[0:80])
#       return hang_man[0:80]
#   elif num == 8:
#       print(hang_man[0:90])
#       return hang_man[0:90]
#   elif num == 9:
#       print(hang_man)
#       return hang_man


# 1. Index 20
# 2. Index 30
# 3. Index 40
# 4. Index 50
# 5. Index 60
# 6. Index 70
# 7. Index 80
# 8. Index 90

def printer(num):
  hang_man = """
        ███████
        ██  ████
        ██  ████
     █████████████
   ██░░░██  ██  ██
   ██  ░░░░██  ██
     ██░░░██  ██
      ██████████
          ██  ██
          ██  ██
          ██  ██
  """
  if num == 1:
      print(hang_man[0:18])
      return hang_man[0:18]
  elif num == 2:
      print(hang_man[0:36])
      return hang_man[0:36]
  elif num == 3:
      print(hang_man[0:54])
      return hang_man[0:54]
  elif num == 4:
      print(hang_man[0:72])
      return hang_man[0:72]
  elif num == 5:
      print(hang_man[0:90])
      return hang_man[0:90]
  elif num == 6:
      print(hang_man[0:108])
      return hang_man[0:108]
  elif num == 7:
      print(hang_man[0:126])
      return hang_man[0:126]
  elif num == 8:
      print(hang_man[0:144])
      return hang_man[0:144]
  elif num == 9:
      print(hang_man)
      return hang_man


# # 1. Index 18
# # 2. Index 36
# # 3. Index 54
# # 4. Index 72
# # 5. Index 90
# # 6. Index 108
# # 7. Index 126
# # 8. Index 144
