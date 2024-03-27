# Promptilation

Just a future project idea I will do soon.

Using LLMs to compile a prompt-heavy programming language to something executable like python.


```
do this a random number of times between 1 and 10 (uniformly distributed)
    print "Hello, World!"
```

promptiles to

```python
import random
for i in range(random.randint(1,10)):
    print("Hello, World!")
```

You get the point.

How far can I push this paradigm?


## Usage

Execute `pcc` and supply an  input file of type `.promptpy`.

`python pcc --input-file <path to input file>`


e.g.
`python pcc --input-file input/prime.promptpy`


This will promptile the code from natural/prompted python down to python.

You should then be able to execute the file.

`python ./build/prime.py`
