import fnmatch
import os
from datetime import datetime, timedelta


# function to loop and search patterns and rm files.
def find_files(dir_to_clean, patterns, days_deletion):
    file_list = []
    days_ago = datetime.now() - timedelta(days=days_deletion)
    for root, dirs, files in os.walk(dir_to_clean):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                file_list.append(os.path.join(root, filename))
                file_list.sort()

    for file in file_list:
        file_time = datetime.fromtimestamp(os.path.getctime(file))
        if file_time < days_ago and os.path.isfile(file):
            try:
                print("Removing file :[{0}]".format(file))
                os.remove(file)
            except OSError as e:
                print('File Clean Up Failed: [{0}]'.format(e))
