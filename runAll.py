import subprocess

subprocess.run(["python", "clean_data.py"])
subprocess.run(["python", "authors.py"])

subprocess.run(["python", "journ.py"])
subprocess.run(["python", "conf.py"])
subprocess.run(["python", "tags.py"])