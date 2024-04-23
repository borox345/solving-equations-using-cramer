# USING CRAMER FORMULAS
def get_equations():
  print("First equation. (Format ax + by = c):")
  eq1 = input("1: ").replace("x", " ").replace("y", " ").split()
  print("Second equation. (Format ax + by = c):")
  eq2 = input("2: ").replace("x", " ").replace("y", " ").split()

  print(eq1)
  print(eq2)

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
  print("Give numbers for X:")
  print("FORMAT: x = A*x + B*y = c")
  x_input_a1 = int(input("A number: "))
  x_input_b1 = int(input("B number: "))
  x_input_c1 = int(input("C number: "))
  x_nums = (x_input_a1, x_input_b1, x_input_c1)

  print("Give numbers for Y:")
  print("FORMAT: y= A*x + B*y = c")
  y_input_a1 = int(input("A number: "))
  y_input_b1 = int(input("B number: "))
  y_input_c1 = int(input("C number: "))
  y_nums = (y_input_a1, y_input_b1, y_input_c1)
  
  sol = cramer_formulas(*x_nums, *y_nums)
  if sol:
      print("x =", sol[0], ", y =", sol[1])
  else:
      print("Equations are parallel.")
