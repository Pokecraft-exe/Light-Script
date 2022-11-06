import("html") # import internal lib html
# no lists into lists into lists ex [[0, 3, [5, 6]], 0, 3]

def start(global %args%):
  # html.getTagByID("ID")["property"] = "new value"

  # test list definition, return test in custom functions
  %list% = [returntest(2), "hello", 3]
  print(%list%)
  
  %truc% = 1
  free(%truc%)
  print(%truc%)

  # test global and locol variables
  global %global_var% = 3; # ; stop the line
  %local_var% = 3 # a return stops the line too
  testGlobal()

  %truccc% = [[0, 3, [5, 6]], 0, 3]
  print(%truccc%)

  print("test key binding")

  # test input()
  print(input("hello: "))

  # test inline
  print("line 1");print("line 2")
  # this line become the 30th for the interpreter !!!

  # test multiline
  print("HELLO "+| # continues line
"WORLD") # print("HELLO WORLD")

  # test len()
  print(len(%list%))

  # test pointer
  %list% -> %pointer%
  1 -> %pointer%
  print(%list%)
  [3, 3] -> %pointer%
  print(%list%)

  # test type convertion
  %convert% = 1
  print(%convert%)
  print(type(%convert%))

  float %convert% = %convert%
  print(%convert%)
  print(type(%convert%))

  int %convert% = %convert%
  str %convert% = %convert%
  print(%convert%)
  print(type(%convert%))

  int %convert% = %convert%
  print(%convert%)
  print(type(%convert%))

  bin %convert% = %convert%
  print(%convert%)
  print(type(%convert%))

  int %convert% = 1
  hex %convert% = %convert%
  print(%convert%)
  print(type(%convert%))

  # test read file
  %variable% = os.file.read("test.txt")

  %list% = [returntest(2), "hello", 3]
  # test modify list
  print(%list%)
  %list%[0] **= 2
  print(%list%)
  %list%[0] *= 2
  print(%list%)
  %list%[0] += 2
  print(%list%)
  %list%[0] -= 2
  print(%list%)
  %list%[0] /= 2
  print(%list%)
  %list%[0] %= 2
  print(%list%)
  %list%[0] = 2
  print(%list%)

  # test while loop
  %i% = 0
  $while$ = %i% != 3
  label("while")
  $while$ print(%i%)
  $while$ %i% += 1
  $while$ goto("while")
  print("while end")

  label("test")

  # test condition 2, file write
  $1$ = %variable% == "path" #initialise une condition
  $1$ print("True")
  $1$ os.file.write("test.txt", "text") 
  # os.file.writeByte("path", %bytes%)
  $!1$ print("False")
  $!1$ os.file.write("test.txt", "path"))

  # test condition 3 defining default execution
  # $2$ = %variable% == path @execution goto("test")
  # $2$

  # test sin(), cos(), tan(), pi()
  print(sin(%pi%))
  print(cos(%pi%))
  print(tan(%pi%))
  print(%pi%)

  coolFnunc() # not found but the code continues
  coolFunc() # execute coolFunc()
  print("it continues")
end def

def coolFunc():
  print("entering coolFunc()")
end def

def testGlobal():
  print(%global_var%)
  print(%local_var%)
end def

def returntest(%int%):
  return(%int%)
end def




