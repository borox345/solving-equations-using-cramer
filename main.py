# USING CRAMER FORMULAS
def get_equations():
  print("First equation. (Format ax + by = c):")
  eq1 = input("1: ").split()
  print("Second equation. (Format ax + by = c):")
  eq2 = input("2: ").split()
  


  equ1 = (int(eq1[0][0]), int(eq1[2][0]), int(eq1[4]))
  equ2 = (int(eq2[0][0]), int(eq2[2][0]), int(eq2[4]))
  
  return equ1, equ2

def cramer_formulas(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
      return None  # parallel qquations, no unique solution
    
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    
    return int(x), int(y)

# Ex:
# equation1 = (5, 3, 9)  # 2x + 3y = 13
# equation2 = (7, 4, 29)  # 4x + 5y = 29

# solution = cramer_formulas(*equation1, *equation2)
# if solution:
#   print("x =", solution[0], ", y =", solution[1])
# else:
#   print("Equations are parallel.")

if __name__ == "__main__":
  option = input("Option 1/2: ")
  if option == 1:
    input = get_equations()
    solution = cramer_formulas(*input[0], *input[1])
    if solution:
      print("x =", solution[0], ", y =", solution[1])
    else:
      print("Equations are parallel.")
  elif option == 2:
    print("s")
