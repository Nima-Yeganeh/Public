sudo apt-get update -y --no-install-recommends
sudo apt-get upgrade -y --no-install-recommends
sudo apt-get install build-essential -y --no-install-recommends
gcc --version
g++ --version
sudo apt-get install nodejs -y --no-install-recommends
node -v
sudo apt-get install npm -y --no-install-recommends
npm -v
sudo apt-get install python3 -y --no-install-recommends
python3 --version
sudo apt-get update -y --no-install-recommends
sudo apt-get install net-tools -y --no-install-recommends
sudo apt-get install iotop iftop -y --no-install-recommends
sudo apt-get install golang -y --no-install-recommends
go version
export GOPATH=$HOME/go
export GOROOT=/usr/lib/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
source ~/.bashrc
