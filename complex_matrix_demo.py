import complex_matrix
import sympy

# complex_matrix1 = ComplexMatrix(3, 3)
# complex_matrix1[0, 0] = 3 + 2j
# complex_matrix1[1, 0] = 0j
# complex_matrix1[2, 0] = 5 - 6j

# complex_matrix1[0, 1] = 1 + 0j
# complex_matrix1[1, 1] = 4 + 2j
# complex_matrix1[2, 1] = 1j

# complex_matrix1[0, 2] = 4 - 1j
# complex_matrix1[1, 2] = 0j
# complex_matrix1[2, 2] = 4 + 0j


# complex_matrix2 = ComplexMatrix(3, 3)
# complex_matrix2[0, 0] = 5 + 0j
# complex_matrix2[1, 0] = 2 - 1j
# complex_matrix2[2, 0] = 6 - 4j

# complex_matrix2[0, 1] = 0j
# complex_matrix2[1, 1] = 4 + 5j
# complex_matrix2[2, 1] = 2 + 0j

# complex_matrix2[0, 2] = 7 - 4j
# complex_matrix2[1, 2] = 2 + 7j
# complex_matrix2[2, 2] = 0j


# print(complex_matrix1)
# print("*")
# print(complex_matrix2)
# print("=")
# print(ComplexMatrix.matrixMultiply(complex_matrix1, complex_matrix2))

# print(complex_matrix3)
# print("AFTER transpose")
# print(ComplexMatrix.transpose(complex_matrix3))

# print(complex_matrix1)
# print("inner product with")
# print(complex_matrix2)
# print("=")
# print(ComplexMatrix.inner_product(complex_matrix1, complex_matrix2))

# hermitian_matrix = complex_matrix.ComplexMatrix(3, 3)
# hermitian_matrix[0, 0] = 5 + 0j
# hermitian_matrix[1, 0] = 4 + 5j
# hermitian_matrix[2, 0] = 6 - 16j

# hermitian_matrix[0, 1] = 4 - 5j
# hermitian_matrix[1, 1] = 13 + 0j
# hermitian_matrix[2, 1] = 7 + 0j

# hermitian_matrix[0, 2] = 6 + 16j
# hermitian_matrix[1, 2] = 7 + 0j
# hermitian_matrix[2, 2] = -2.1 + 0j

# diagonal_matrix = complex_matrix.ComplexMatrix(3, 3)
# diagonal_matrix[0, 0] = 5 + 0j
# diagonal_matrix[1, 0] = 0j
# diagonal_matrix[2, 0] = 0j

# diagonal_matrix[0, 1] = 0j
# diagonal_matrix[1, 1] = 13 + 0j
# diagonal_matrix[2, 1] = 0j

# diagonal_matrix[0, 2] = 0j
# diagonal_matrix[1, 2] = 0j
# diagonal_matrix[2, 2] = -2.1 + 0j


# print(diagonal_matrix)
# print("is diagonal matrix: ")
# print(diagonal_matrix.is_diagonal())

unitary_matrix = complex_matrix.ComplexMatrix(3, 3)
unitary_matrix[0, 0] = (1 + 1j)/2
unitary_matrix[1, 0] = (1j)/(sympy.sqrt(3))
unitary_matrix[2, 0] = (3 + 1j)/2*(sympy.sqrt(15))

unitary_matrix[0, 1] = -1/2 + 0j
unitary_matrix[1, 1] = (1/3)*sympy.sqrt(2) + 0j
unitary_matrix[2, 1] = (4 + 3j)/2*sympy.sqrt(15)

unitary_matrix[0, 2] = 1/2 + 0j
unitary_matrix[1, 2] = -1j/sympy.sqrt(3)
unitary_matrix[2, 2] = 5j/2*sympy.sqrt(15)

# unitary_matrix = complex_matrix.ComplexMatrix(2, 2)
# unitary_matrix[0, 0] = 0j
# unitary_matrix[1, 0] = -1j
# unitary_matrix[0, 1] = 1j
# unitary_matrix[1, 1] = 0j


# print(unitary_matrix)
# print("is unitary matrix: ")
print(unitary_matrix.is_unitary())