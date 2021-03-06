#!/bin/bin/env python
"""
USAGE:

apache_log_parser_split.py some_log_file

This script takes one command line argument: the name of a log file to parse. If then parses log file and generates a report which associates remote hosts with number of bytes transferred to them.
"""

import sys

def dictify_logfile(line):
    ''' return a dictionary of the pertinent pieces of an apache comnbined log file
    Currently, the only fields we are interested in tare remote host and bytes sent,
    but we are putting status in there just for good meausure.
    '''

    split_line = line.split()
    return {'remote_host': split_line[0],
            'status': split_line[8],
            'bytes_sent': split_line[9],
    }

def generate_log_report(logfile):
    ''' return dictionary of format remote_host=>[list of bytes sent]
    This function takes a file object, iterates through all the likes in the file,
    and generates a report of the number of bytes transferred to each remote host
    for each hit on the webserver.
    '''

    report_dict ={}
    for line in logfile:
        line_dict = dictify_logfile(line)
        print line_dict
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            ##totaly disregard anything we dont understand
            continue
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
    return report_dict

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print __doc__
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print "You must specify a valid file to parse"
        print __doc__
        sys.exit(1)
    log_report = generate_log_report(infile)
    print log_report
    infile.close()
