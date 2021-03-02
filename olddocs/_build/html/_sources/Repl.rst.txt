Using the Python repl
=====================

* From a command prompt type;
 
`> python`

* Try these commands:

.. code-block:: python

    1+2*3
    print 'Hello World!'
    print('Hello World!')
    name = 'Fred'
    print(name)
    greet = "Hello " + name + '!'
    print(greet)
    print(f'Hello {name.upper()}!')
    import this
    help()


* Code block indentation:

.. code-block:: python

    age = 17
    if age < 18:
        print('You cannot drink')
        
    if age < 18:
        print('You cannot drink')
        print('But maybe you can drive')
    else:
        print('You can drink')
        print('You can drive')
        print('But you must not drink and drive')


* To exit the repl on Windows type Ctrl-Z \<enter\> 
* Unix type Ctrl-D
* Or type "`exit()`"