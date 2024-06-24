
## Using relative import

c call a, a call b. 

### individually run "a.py" in the module
```
python3 -m math.a
python3 -m server.math.a
```

### run "c.py" to call "a.py". a will be called as module
```
python3 server/c.py 
```

