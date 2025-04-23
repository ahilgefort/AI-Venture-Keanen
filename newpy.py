import subprocess

with open("script.py","w") as f:
    f.write("""print("Hello world")
print("Ayo nahhh")""")
    
subprocess.run(["python", "script.py"])