import os
import time

print("hello world!")
os.mkdir("/folder")
f = open("/hello.sh", "w")
f.write('echo "hello world!"')
f.close()
time.sleep(100)
