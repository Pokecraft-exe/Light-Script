# Light-Script

The light script language is a programmation language used in site making.

No need to get [LSpy.py](<https://github.com/Pokecraft-exe/Light-Script/blob/main/LSide.pyw>) when you have [LSide.py](https://github.com/Pokecraft-exe/Light-Script/blob/main/LSpy.py).

Use ```console
python LSpy.py [file] # for windows
python3 LSpy.py [file] # fro linux
``` to run your .ls code.

[To access the project wiki](https://github.com/Pokecraft-exe/Light-Script/wiki)

## LS IDE.pyw

The language is included in the package.

![image](https://user-images.githubusercontent.com/67156699/188330887-0ff13c9f-81d7-477b-b332-932430a63b6e.png)

```
###### Native ######
[Y/N] ...args
[N] preprocessor PPROC("truc", %truc%) # will replace all truc by %truc% in the program
[N] default argument def reax(%value% = 0)
[N] list managment [:1] [1:] [$]
[N] condition defining default execution @execution truc()
[N] function as variable lambda
[N] dict

###### Stdlib ######
[Stdsync] threads
[Stdsync] sync / async
[Stdsync] parallel lines parallel(2, 3) # will skip lines 2 and 3 and execute them in same time
[Stdgui] windows
```
