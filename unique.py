uniq_lines = set(open('large_combined.txt').readlines())

new_file = open('large_directories.txt', "w").writelines(uniq_lines)

new_file.close()


