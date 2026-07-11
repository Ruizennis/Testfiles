# this is a file made to test TermuxC
try:
    from TermuxC import Copy
except:
    print("run pip install TermuxC first!")
import random
print('press Ctrl+C to stop')
while True:
    try:
        Copy(random.randint(1,15))
    except KeyboardInterrupt:
        print("Ctrl+C pressed, stopping")
        exit()
    except Exception as e:
        pass
