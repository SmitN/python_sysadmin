import filecmp
import os
import os.path
import sys
import difflib
import subprocess
def diff(basepath, path1, path2):
    # STEP 1: iterate on all path1 paths (directories and filenames) and compare with path2
    # - report if path2 does not exist
    # - when path is a file, report if path1 differ from path2
    common_paths = []
    for path in os.listdir(path1):
        abs1 = os.path.join(path1, path)
        abs2 = os.path.join(path2, path)
        relative = abs1[len(basepath)+1:]
        if not os.path.exists(abs2):
            print '\033[1;44mFile is Only in %s: %s\033[1;m'  % (os.path.dirname(abs1), path)
            continue
        common_paths.append(relative)

        if os.path.isfile(abs1):
            r = filecmp.cmp(abs1, abs2)
            if not r:
                print "Files %s and %s differ" % (abs1, abs2)
                subprocess.call(["sdiff", abs1, abs2])
            elif os.path.isdir(abs1):
                paths = diff(basepath, abs1, abs2)
                common_paths.extend(paths)

    # STEP 2: the other way: iterate on all path2 paths and
    # - report if path in path2 does not exist in path1
    for path in os.listdir(path2):
        abs1 = os.path.join(path1, path)
        abs2 = os.path.join(path2, path)
        relative = abs2[len(basepath)+1:]
        if not os.path.exists(abs1):
            print "\033[1;43mOnly in %s: %s\033[1;m" % (os.path.dirname(abs2), path)

    return common_paths


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: diff_report.py {path1} {path2}"
        sys.exit()

    paths = sys.argv[1:]
