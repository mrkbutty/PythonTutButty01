Creating and running a script
=============================

* At command prompt create a script file::

    > mkdir \pytut
    > cd \pytut
    > Notepad hello.py


* Type into notepad being careful to use the same type of spacing 
  <Tab> or <Spaces> for each indent:

.. code-block:: python
   :linenos:

    def greet(name=None):
        if name==None:
            name = 'World'
        
        text = 'Hello ' + name + '!'
        print(text)
        
    print(greet)
    answer = input('What is your name? ')
    greet(answer)

* To run the script::

    > python hello.py

* Now try using and stepping through (F7) with Thonny!
