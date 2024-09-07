# multi threadding

import time, threading

# def task(name):
#     print(f"stated {name} task")
#     time.sleep(2)
#     print(f"{name} task Completed")


# threads = []

# for i in range(3):
#     thread = threading.Thread(target=task,args=(f"Thread-{i+1}",))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()


# print("all thread are ended")


# multi process


# import multiprocessing
# import time

# def task(name):
#     print(f"stated {name} task")
#     result = 0
#     for i in range(100000):
#         result+=i
#     print(f"{name} task Completed")


# # create multiple processes


# if __name__ == "__main__":
#     processes =[]

#     for i in range(3):
#         process = multiprocessing.Process(target=task,args=(f"Process-{i+1}",))
#         processes.append(process)
#         process.start()

#     # Wait for all processes to complete
#     for process in processes:
#         process.join()

#     print("all processes are ended")


# import threading, multiprocessing


# def task(name):
#     print(f"start {name} task")
#     time.sleep(2)
#     print(f"{name} task Completed")


# if __name__ == "__main__":
#     threads = []
#     for i in range(3):
#         thread = threading.Thread(target=task, args=(f"task-{i+1}",))
#         threads.append(thread)
#         thread.start()
#     # wait for all thead to complate
#     for thead in threads:
#         thead.join()
#     print("all thread are ended")
