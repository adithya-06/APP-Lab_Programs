from pyDatalog import pyDatalog
pyDatalog.create_terms('Bear,Elephant,Cat,Black,Gray,Brown,Big,small,size,color,X,Y,dark')
+size("Bear","Big")
+size("Elephant","Big")
+size("Cat","small")
+color("Bear","Brown")
+color("Cat","Black")
+color("Elephant","Gray")
dark(X) <= (color(X,"Black"))
dark(X) <= (color(X,"Brown"))


print(dark(X) & (size(X,'Big')))
