echo -n "Базовая инвентаризация узла: "
uname -n
#
echo =====================================
dmidecode | sed -n '/System Information/,+2p' | sed 's/\x09//'
dmesg | grep Hypervisor	
dmidecode | grep "Serial Number" | grep -v "Not Specified" | grep -v None
#
echo =====================================
echo "Сведения об ОС:"
uname -o -r
if [ -f /etc/redhat-release ]; then
    echo -n " "
    cat /etc/redhat-release
fi
if [ -f /etc/issue ]; then
    cat /etc/issue
fi
echo =====================================
echo "Сведения об IP: "
ip ad | grep inet | grep -v "127.0.0.1" | grep -v "::1/128" | tr -s " " | cut -d " " -f 3
# используйте эти строки в старых версиях Linux
# ifconfig | grep "inet" | grep -v "127.0.0.1" | grep -v "::1/128" | tr -s " " |
cut -d " " -f 3
#
echo =====================================
echo "Сведения о CPU: "
cat /proc/cpuinfo | grep "model name\|MH\|vendor_id" | sort -r | uniq
echo -n "Количество сокетов: "
cat /proc/cpuinfo | grep processor | wc -l
echo -n "Количество ядер (общее): "
cat /proc/cpuinfo | grep cores | cut -d ":" -f 2 | awk '{sum+=$1} END {print sum}'
#
echo =====================================
echo "Сведения о памяти: "
grep MemTotal /proc/meminfo | awk '{print $2,$3}'
#
echo =====================================
echo "Сведения о дисках: "
fdisk -l | grep Disk | grep dev
