import os
import json
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))
path = dir_path + "/json_files_folder"

shutil.rmtree(dir_path + '/final', ignore_errors=True)
os.mkdir(dir_path + '/final')

def collect_all_files(path):
    files = []
    for i, j, k in os.walk(path):
        for file in k:
            if '.json' in file:
                files.append(file)
    return files

# print(collect_all_files(path))

def full_path(larr):
    arr = []
    for i in range(len(larr)):
        arr.append(path + "/" + larr[i])
    return arr
# print(full_path(collect_all_files(path)))

def collect_all_data(arr):
    arr_fin = []
    for i in range(len(arr)):
        with open(arr[i], encoding='utf-8') as f:
            data = json.loads(f.read())
            data = [data]
            arr_fin.append(data)
    return arr_fin
# print(collect_all_data(full_path()))

#
# with open(dir_path + '/final/final_data.json', 'w', encoding='utf8') as json_f:
#     json.dump(collect_all_data(full_path(collect_all_files(path))), json_f, ensure_ascii=False)

