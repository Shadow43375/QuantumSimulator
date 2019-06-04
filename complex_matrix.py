class ComplexMatrix:
  def __init__(self, n, m):
    self.list = []
    self.x = n
    self.y = m
    for each_column in range(n):
      self.list.append([0 + 0j]*m)


  def __getitem__(self, element_coordinates):
    return self.list[element_coordinates[0]][element_coordinates[1]]


  def __setitem__(self, element_coordinates, data):
    self.list[element_coordinates[0]][element_coordinates[1]] = data


  def is_square(self):
    if(self.x == self.y):
      return True
    else:
      return False


  def is_diagonal(self):
    if not(self.is_square()):
      return False

    for x in range(self.x):
      for y in range(self.y):
        if((x != y) and (self[x, y] != 0 or self[x, y] != 0j)):
          return False
      
    return True


  def is_hermitian(self):
    if not(self.is_square()):
      return False
    
    adjoint_matrix = self.adjoint(self)
    for x in range(self.x):
      for y in range(self.y):
        if not(adjoint_matrix[x, y] == self[x, y]):
          return False

    return True

  
  def is_unitary(self):
    matrix1 = self.matrix_multiply(self, self.adjoint(self))
    matrix2 = self.matrix_multiply(self.adjoint(self), self)

    print(self)
    print(self.adjoint(self))
    print(self.matrix_multiply(self, self.adjoint(self)))

    for x in range(self.x):
      for y in range(self.y):
        if not(matrix1[x, y] == matrix2[x, y]):
          return False
    
    return True


  # find the complex number taking up the most space and store as map from column to white spaces needed
  def get_padding_amount(self):
    column_padding = {}

    for x in range(self.x):
      greatest_yet = 0
      for y in range(self.y):
        if(len(str(self.list[x][y])) > greatest_yet):
          greatest_yet = len(str(self.list[x][y]))
      column_padding[x] = greatest_yet + 1
    
    return column_padding


 # a utility function for generating white spaces from printing out matrix as string
  def create_whitespace(self, number_of_spaces):
    white_space = ""
    for spaces in range(number_of_spaces):
      white_space += " "

    return white_space


  def __str__(self):

    str_padding = self.get_padding_amount()
    str_output = ""
    for y in range(self.y):
      str_output += "|"
      for x in range(self.x):
        str_output += self.create_whitespace(str_padding[x] - len(str(self.list[x][y])))
        str_output += str(self.list[x][y])
        if not(x == (self.x - 1)):
          str_output += ","


      str_output += "|"
      str_output += "\n"

    return str_output

    
  @classmethod
  def add(cls, matrix1, matrix2):
    # need to check that the matrices are of the same dimensions
    if not(matrix1.y == matrix2.y and matrix1.x == matrix2.x):
      return False
    new_matrix = cls(matrix1.x, matrix2.y)
    for x in range(matrix1.x):
      for y in range(matrix1.y):
        new_matrix[x, y] = matrix1[x, y] + matrix2[x, y]
    return new_matrix


  @classmethod
  def subtract(cls, matrix1, matrix2):
    # need to check that the matrices are of the same dimensions
    if not(matrix1.y == matrix2.y and matrix1.x == matrix2.x):
      return False
    new_matrix = cls(matrix1.x, matrix2.y)
    for x in range(matrix1.x):
      for y in range(matrix1.y):
        new_matrix[x, y] = matrix1[x, y] - matrix2[x, y]
    return new_matrix


  @classmethod
  def inverse(cls, matrix):
    
    new_matrix = cls(matrix.x, matrix.y)
    for x in range(matrix.x):
      for y in range(matrix.y):
        if not(matrix[x, y] == 0 + 0j or matrix[x, y] == -0 - 0j or matrix[x, y] == -0 + 0j or matrix[x, y] == 0 - 0j):
          new_matrix[x, y] = matrix[x, y]*(-1)

    return new_matrix


  @classmethod
  def transpose(cls, matrix):
    new_matrix = cls(matrix.y, matrix.x)
    for x in range(new_matrix.x):
      for y in range(new_matrix.y):
        new_matrix[x, y] = matrix[y, x]

    return new_matrix


  @classmethod
  def adjoint(cls, matrix):
    new_matrix = cls(matrix.y, matrix.x)
    for x in range(new_matrix.x):
      for y in range(new_matrix.y):
        new_matrix[x, y] = complex.conjugate(matrix[y, x])

    return new_matrix


  @classmethod
  def complex_conjugate(cls, matrix):
    new_matrix = cls(matrix.x, matrix.y)
    for x in range(new_matrix.x):
      for y in range(new_matrix.y):
        new_matrix[x, y] = complex.conjugate(matrix[x, y])

    return new_matrix


  @classmethod
  def scalar_multiply(cls, matrix, scalar):
    
    new_matrix = cls(matrix.x, matrix.y)
    for x in range(matrix.x):
      for y in range(matrix.y):
        if not(matrix[x, y] == 0 + 0j or matrix[x, y] == -0 - 0j or matrix[x, y] == -0 + 0j or matrix[x, y] == 0 - 0j):
          new_matrix[x, y] = matrix[x, y]*scalar

    return new_matrix


  @classmethod
  def matrix_multiply(cls, matrix1, matrix2):

    # need to check if the x dimensions of matrix1 are equal to the y dimensions of matrix2
    if not(matrix1.x == matrix2.y):
      return False

    new_matrix = cls(matrix2.x, matrix1.y)
    for x in range(new_matrix.x):
      for y in range(new_matrix.y):
        sum_result = 0
        for i in range(matrix1.x):
          sum_result += matrix1[i, y]*matrix2[x, i]
        new_matrix[x, y] = sum_result
    
    return new_matrix


  @classmethod
  def inner_product(cls, matrix1, matrix2):
    if not(matrix1.is_square() and matrix2.is_square()):
      return False
    else:
      return cls.trace(cls.matrix_multiply(cls.adjoint(matrix1), matrix2))    

  @classmethod
  def trace(cls, matrix):
    if not(matrix.x == matrix.y):
      return False
    
    total_sum = 0
    for i in range(matrix.x):
      total_sum += matrix[i, i]

    return total_sum

