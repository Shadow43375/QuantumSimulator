import complex_matrix

class ComplexVector(complex_matrix.ComplexMatrix):
  def __init__(self, dimensions):
    super().__init__(1, dimensions)

  def __getitem__(self, element_coordinate):
    # conditional allows for vector object to be compatible with the tuple style addressing of its parent matrix class
    if not(isinstance((1, 2), tuple)):
      return self.list[0][element_coordinate]
    elif(isinstance((1, 2), tuple)):
      return self.list[element_coordinate[0]][element_coordinate[1]]

  def __setitem__(self, element_coordinate, data):
    self.list[0][element_coordinate] = data

  @classmethod
  def convertToVector(cls, matrix):
    if not(matrix.x == 1 or matrix.y == 1):
      return False
    
    new_vector = cls(matrix.y)
    for y in range(matrix.y):
      new_vector[y] = matrix[0, y]

    return new_vector

  @classmethod
  def transpose(cls, vector):
    return cls.convertToVector(complex_matrix.ComplexMatrix.transpose(vector))

  @classmethod
  def transform_vector(cls, matrix, vector):
    return cls.convertToVector(complex_matrix.ComplexMatrix.matrix_multiply(matrix, vector))

  @classmethod
  def inner_product(cls, vector1, vector2):
    return complex_matrix.ComplexMatrix.matrix_multiply(complex_matrix.ComplexMatrix.transpose(vector1), vector2)[0, 0]

  @classmethod
  def norm(cls, vector1):
    return (cls.inner_product(vector1, vector1))**(1/2)

  @classmethod
  def distance_between(cls, vector1, vector2):
    return cls.norm(complex_matrix.ComplexMatrix.subtract(vector1, vector2))

complex_vector1 = ComplexVector(3)
complex_vector1[0] = 3
complex_vector1[1] = 1
complex_vector1[2] = 2

complex_vector2 = ComplexVector(3)
complex_vector2[0] = 2
complex_vector2[1] = 2
complex_vector2[2] = -1

# complex_vector3 = ComplexVector(3)
# complex_vector3[0] = 3
# complex_vector3[1] = -6
# complex_vector3[2] = -2


# print(complex_vector1)
# print("inner product with")
# print(complex_vector2)
# print("=")
# print(ComplexVector.inner_product(complex_vector1, complex_vector2))

# print(complex_vector3)
# print("norm = ")
# print(ComplexVector.norm(complex_vector3))

print(complex_vector1)
print("distance between")
print(complex_vector2)
print("=")
print(ComplexVector.distance_between(complex_vector1, complex_vector2))