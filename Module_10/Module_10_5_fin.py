import multiprocessing
import time
import multiprocessing as mp
def read_info(name):
    all_data = []
    with open('Files/'+name, 'r') as file:
        all_data = file.readlines()
    # return all_data

# print(read_info('file1.txt')[:10])
if __name__ == '__main__':
    # begin = time.time()
    all_files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    for file_name in all_files:
        read_info(file_name)
    end = time.time()
    print(f'Прошло времени {round(end-begin, 3)} без процессов')

    with multiprocessing.Pool(processes=4) as pool:
        for file_name in all_files:
            begin = time.time()
            pool.map(read_info, all_files)
    end = time.time()
    print(f'Прошло времени {round(end-begin, 3)} с запуском процессов')

