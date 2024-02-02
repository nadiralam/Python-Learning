
# Write OOP classes to handle the following scenarios:

# ---------------------------QUESTIONS-------------------------------------------->

# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

class Point:

  def __init__(self,x,y):
    self.x_cod = x
    self.y_cod = y

  def __str__(self):
    return '<{},{}>'.format(self.x_cod,self.y_cod)

  def euclidean_distance(self,other):
    return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

  def distance_from_origin(self):
    return (self.x_cod**2 + self.y_cod**2)**0.5

p1 = Point(2,3)
p2 = Point(3,4)
print(p1)
print(p2)

p1.euclidean_distance(p2)
print(p1.euclidean_distance(p2))

p3 = Point(2,2)
print(p3)
p3.distance_from_origin()
print(p3.distance_from_origin())


class Line:

  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C

  def __str__(self):
    return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)

  def point_on_line(line,point):
    if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
      return "lies on the line"
    else:
      return "does not lie on the line"

  def shortest_distance(line,point):
    return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5
  
l1 = Line(2,3,4)
print(l1)

l2 = Line(1,1,-2)
print(l2)
p1 = Point(1,1)
print(p1)
l2.point_on_line(p1)
print(l2.point_on_line(p1))


l3 = Line(2,4,6)
print(l3)
p2 = Point(4,6)
print(p2)
l3.point_on_line(p2)
l3.shortest_distance(p2)
print(l3.shortest_distance(p2))

# How objects access attributes
class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.nameame)
    else:
      print('Hello',self.name)

p = Person("Nadir","India")
p.country
print(p.country)

p.name
print(p.name)

p.greet()

# what if i try to access non-existent attributes

p.Gender = "male"
print(p.Gender)


# Reference Variables

# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to an existing object does not create a new object

class Person:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'

p = Person()
q = p
print(id(p))
print(id(q))

print(p.name)
print(q.name)
q.name = 'ankit'
print(q.name)
print(p.name)

# Pass by reference

class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print('Hi my name is',person.name,'and I am a',person.gender)
  p1 = Person('ankit','male')
  return p1

p = Person('nitish','male')
x = greet(p)
print(x.name)
print(x.gender)

# or

class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function

def greet(person):
  print(id(person))
  person.name = 'ankit'
  print(person.name)

p = Person('nitish','male')
print(id(p))
greet(p)
print(p.name)

# Object ki mutability

class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  person.name = 'ankit'
  return person

p = Person('nitish','male')
print(id(p))
p1 = greet(p)
print(id(p1))