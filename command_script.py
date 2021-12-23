from subprocess import run, PIPE

result = run(['ls'],
    stdout=PIPE, stderr=PIPE, check=True,
    universal_newlines=True)
version = result.stdout.split("versionName='")[1].split("'")[0]