# c_function_generator

Use python to generate source and header files of c language.
When I set up a new c project, I have to copy a lot of function description texts and do a lot formatting works. 
Now I write this python tool to do these works automaticlly. 
You just need to input function relative info into ./input/function.csv, then run ./src/cFileGenerator.py. You will get c source file and header file in ./output/.
C function formate is defined in .src/cFunctionBody.
C function description formate is defined in .src/cFunctionDescription
C header formate is defined in .src/cFunctionHeader
