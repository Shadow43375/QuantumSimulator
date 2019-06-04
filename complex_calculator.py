import math
import matplotlib.pyplot as plt


class ComplexCalculator:
  
  @staticmethod
  def modulus(complex_number):
    return math.sqrt(complex_number.real ** 2 + complex_number.imag ** 2)

  @staticmethod
  def build_cartesian_plane(max_quadrant_range):
      l = []
      zeros = []
      ax = plt.axes()
      head_width = float(0.05) * max_quadrant_range
      head_length = float(0.1) * max_quadrant_range
      ax.arrow(0, 0, max_quadrant_range, 0, head_width=head_width, head_length=head_length, fc='k', ec='k',zorder=100)
      ax.arrow(0, 0, -max_quadrant_range, 0, head_width=head_width, head_length=head_length, fc='k', ec='k', zorder=100)
      ax.arrow(0, 0, 0, max_quadrant_range, head_width=head_width, head_length=head_length, fc='k', ec='k', zorder=100)
      ax.arrow(0, 0, 0, -max_quadrant_range, head_width=head_width, head_length=head_length, fc='k', ec='k', zorder=100)
      counter_dash_width = max_quadrant_range * 0.02
      dividers = [0,.1,.2,.3,.4, .5, .6, .7, .8, .9, 1]
      for i in dividers:
          plt.plot([-counter_dash_width, counter_dash_width], [i*max_quadrant_range, i*max_quadrant_range], color='k')
          plt.plot([i * max_quadrant_range, i*max_quadrant_range], [-counter_dash_width, counter_dash_width], color='k')
          plt.plot([-counter_dash_width, counter_dash_width], [-i * max_quadrant_range, -i * max_quadrant_range], color='k')
          plt.plot([-i * max_quadrant_range, -i * max_quadrant_range], [-counter_dash_width, counter_dash_width], color='k')
          l.append(i * max_quadrant_range)
          l.append(-i * max_quadrant_range)
          zeros.append(0)
          zeros.append(0)    
      
      return ax
  
  # should make sure to add in named parameter options for such things as visualzing angle and also graphing multiple complex numbers. Could require multiple function calls or single (need to research)
  @classmethod
  def graph_number(cls, complex_numbers):
    # fig, ax = plt.subplots()
    ax = cls.build_cartesian_plane(10)
    print(type(ax))

    # x_pos[0] is x coordinate of first vector and x_pos[1] is the x coordinate of the second vector and so on...
    x_pos = []
    for each_number in complex_numbers:
      x_pos.append(0)
    # y_pos[0] is y coordinate of first vector and y_pos[1] is the y coordinate of the second vector and so on...
    y_pos = []
    for each_number in complex_numbers:
      y_pos.append(0)
    # x_direct[0] is the x component of the first vector and x_direct[1] is the x_component of the second vector and so on...
    x_direct = []
    for each_number in complex_numbers:
      x_direct.append(each_number.real)
    # y_direct[0] is the y component of the first vector and y_direct[1] is the y_component of the second vector and so on...
    y_direct = []
    for each_number in complex_numbers:
      y_direct.append(each_number.imag)
    # color[0] is the color of the first vector and color[1] is the color of the second vector and so on...
    # color = []
    # for each_number in complex_numbers:
    #   color.append("#42f46b")

    axis_size = 10
    ax.quiver(x_pos, y_pos, x_direct, y_direct, color = ["#42f46b"], angles='xy', scale_units='xy', scale=1)
    ax.axis([-axis_size,axis_size, -axis_size, axis_size])

    plt.show()

  @classmethod
  def get_polar_form(cls, complex_number):
    magnitude = cls.modulus(complex_number)
    # zero vector
    if(complex_number.real == 0 and complex_number.imag == 0):
      return [magnitude, 0]
    # vector at 90 degrees (straight up)
    elif(complex_number.real == 0 and complex_number.imag > 0):
      return [magnitude, math.pi/2]
    # vector at 270 degrees (straight down)
    elif(complex_number.real == 0 and complex_number.imag < 0):
      return [magnitude, 3*math.pi/2] 
    # vector in first quadrant
    elif(complex_number.real > 0 and complex_number.imag >= 0):
      theta = math.atan(complex_number.imag/complex_number.real)
      return [magnitude, theta]
    # vector in second quadrant
    elif(complex_number.real < 0 and complex_number.imag > 0):
      theta = math.pi/2 + abs(math.atan(complex_number.imag/complex_number.real))
      return [magnitude, theta]
    # vector in third quadrant
    elif(complex_number.real < 0 and complex_number.imag <= 0):
      theta = math.pi + abs(math.atan(complex_number.imag/complex_number.real))
      return [magnitude, theta]
    # vector in fourth quadrant
    elif(complex_number.real > 0 and complex_number.imag < 0):
      theta = 3*math.pi/2 + abs(math.atan(complex_number.imag/complex_number.real))
      return [magnitude, theta]


  @staticmethod
  def get_component_form(complex_number):
    theta = complex_number[1]%(2*math.pi)
    real_component = complex_number[0]*math.cos(theta)
    imaginary_component = complex_number[0]*math.sin(theta)

    return complex(real_component, imaginary_component)

  @staticmethod
  def polar_form_multiply(complex_number1, complex_number2):
    return [complex_number1[0]*complex_number2[0], complex_number1[1] + complex_number2[1]]

  @classmethod
  def get_nth_roots(cls, original_complex_number, n):
    roots = []
    original_complex_number = cls.get_polar_form(original_complex_number)
    complex_number = original_complex_number
    for k in range(n):
      complex_number = [original_complex_number[0]**(1/n), (original_complex_number[1] + k*2*math.pi)/n]
      roots.append(complex_number)
    
    print(roots)
    return list(map(cls.get_component_form, roots))




complex_number1 = 10 + 4j
# ComplexCalculator.graph_number(ComplexCalculator.get_nth_roots(complex_number1, 3))
ComplexCalculator.graph_number([complex_number1])