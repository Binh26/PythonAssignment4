import os, nbody
from time import perf_counter

iterations_list=[5000,500000,5000000,50000000]
python_filename_list=['python_5000.csv','python_500000.csv','python_5000000.csv','python_50000000.csv']
debug_filename_list=['c++_debug_5000.csv','c++_debug_500000.csv','c++_debug_5000000.csv','c++_debug_50000000.csv']
release_filename_list=['c++_release_5000.csv','c++_release_500000.csv','c++_release_5000000.csv','c++_release_50000000.csv']
out = 0 # 0: do not output the file; 1: output the file

with open('time.csv', 'a') as f:
    f.write('program_type,stimulation_time,running_time(ms)\n')

for i in range(4):
    print('stimulation times: {}'.format(iterations_list[i]))
    begin_python = perf_counter()
    os.system('nbody.py {} {} {}'.format(iterations_list[i],python_filename_list[i],out))
    finish_python = perf_counter()
    python_time = (finish_python - begin_python)*1000
    print('python running times: {:.2f}ms'.format(python_time))

    begin_debug = perf_counter()
    os.system('D:\\git_test\\assignment_final_new\\cmake-build-debug\\nbody.exe {} {} {}'.format(iterations_list[i],debug_filename_list[i],out)) #just change the filepath to that in your computer
    finish_debug = perf_counter()
    debug_time=(finish_debug - begin_debug) * 1000
    print('c++ debug running times: {:.2f}ms'.format(debug_time))

    begin_release = perf_counter()
    os.system('D:\\git_test\\assignment_final_new\\cmake-build-release\\nbody.exe {} {} {}'.format(iterations_list[i],release_filename_list[i],out))
    finish_release = perf_counter()
    release_time=(finish_release - begin_release) * 1000
    print('c++ release running times: {:.2f}ms\n'.format(release_time))

    with open('time.csv','a') as f:
        f.write('python,{},{}\n'.format(iterations_list[i],python_time))
        f.write('c++debug,{},{}\n'.format(iterations_list[i], debug_time))
        f.write('c++release,{},{}\n'.format(iterations_list[i], release_time))


