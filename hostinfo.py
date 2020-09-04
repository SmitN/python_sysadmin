import os
import platform
d='/sys/class/net'

# machine
print("Machine: " + platform.machine())
print("Node: " + platform.node())
# processor
print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)
# system
print("System: " + platform.system())
# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)
# Load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())
# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

#Network Related Info
for filename in os.listdir(d):
    if os.path.exists('/etc/sysconfig/network-scripts/ifcfg-' + filename):
        print("==========Network Interface Information for " + filename + "========" )
        f = open('/etc/sysconfig/network-scripts/ifcfg-' + filename, 'r')
        Lines=f.readlines()
        for line in Lines:
            print(line.strip())
        f.close()
        print("\n")
    if os.path.exists('/opt/cdp/output/' +filename):
        print("++++ LLDP-CDP Info ++++")
        C=open('/opt/cdp/output/' +filename)
        CL=C.readlines()
        for Clines in CL:
            print(Clines.strip())
        C.close()
        print("\n")
    if not filename.startswith("bond") and not filename.startswith("lo") :
        os.system("ethtool  %s" % filename)
