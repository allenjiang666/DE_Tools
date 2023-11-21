import subprocess
import re


def run_metaflow(command):

    #Allows for asynchronous operation, meaning your Python script can continue running while the subprocess is executing
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
   
    pattern = r"Workflow starting \(run-id (\d+)\)" 
    
    output={}
    for i in range(10):
        message = process.stdout.readline()
        error = process.stderr.readline()
        match = re.search(pattern, message.strip())
        
        if match is not None:
            print(message)
            output['run_id'] = match.group(1)
            output['message'] = "Pipeline started successfully"
            break
        elif re.search(r"Traceback \(most recent call last\)", error.strip()):  
            output['run_id'] = 0
            output['message'] = "There is an python Error in your flow"       
            break     
        else:
            output['run_id'] = 0
            output['message'] = "There is an error with your flow setup" 
            print(error) 
    print('loop finished')
    return output

