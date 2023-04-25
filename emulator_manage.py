import subprocess

def fnGetCurrentInstancesNumber():
    output = subprocess.check_output(['memuc', 'listvms'])
    return output

def fnCreateNewInstance():
    output = subprocess.check_output(['memuc', 'create', '76'])
    return output

def fnRunInstance(index):
    output = subprocess.check_output(['memuc', 'start', '-i', index])
    return output