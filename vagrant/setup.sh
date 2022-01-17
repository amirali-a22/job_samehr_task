# Change the mirrors
sed -i 's|http://archive.|http://ir.archive.|g' /etc/apt/sources.list

# Set debian frontend
export DEBIAN_FRONTEND=noninteractive

# Update the packages
apt update
apt dist-upgrade -y

# Install python 3.9
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa -y
apt install python3.9-full -y