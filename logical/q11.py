from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y')
print(X.in_(range(101)) & Y.in_(range(11)) & (X==Y*Y))