import subprocess
import os
import re


def run_metaflow(command, user):

    # Set the environment variables for the subprocess
    env = {"USER": user}
    # You can also include the current environment variables
    env.update(os.environ)

    #Allows for asynchronous operation, meaning your Python script can continue running while the subprocess is executing
    process = subprocess.Popen(command, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
   
    pattern = r"Workflow starting \(run-id (\d+)\)" 
    
    run_id = 0
    while True:
        message = process.stdout.readline()
        error = process.stderr.readline()
        if error:
            print(error)
            break
        
        match = re.search(pattern, message.strip())
        if match is not None:
            run_id = match.group(1)
            break

    return run_id
