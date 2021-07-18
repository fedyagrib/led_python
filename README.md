# led_python
Visualzation of led strip in python

https://user-images.githubusercontent.com/36953311/126059218-82ec448a-77e2-42ff-ac15-8477d2acff45.mov

https://user-images.githubusercontent.com/36953311/126059223-19fbd463-fadf-46a9-9fab-0f570c5e3ea7.mov

<hr />
<br />

## Run

Init Led library:
```python
from Led import Led
led = Led(led_num = 20, pix_width = 40, pix_offset = 20)
```

Run one effect:
```python
from effects import ef1
for _ in ef2(led):
    pass
```
    
Run multiple effects:
```python
from effects import ef1, ef2
ef1_gen = ef1(led, delay)
ef2_gen = ef2(led, delay)
while True:
    ef1_gen.__next__()
    ef2_gen.__next__()
```

