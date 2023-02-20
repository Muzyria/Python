import subprocess

collection_path = 'C:\Git_Muzyria\Python\Python\My_Pixels_work\SyncWice_get_post\SyncWise_postman_collection.json'
environment_path = '/path/to/environment.json'

command = f'newman run {collection_path} -e {environment_path}'

process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

if error:
    print(f'Error running Newman: {error}')
else:
    print(f'Newman output: {output.decode()}')