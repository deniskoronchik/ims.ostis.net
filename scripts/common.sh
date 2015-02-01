red="\e[1;31m" # Red B
blue="\e[1;34m" # Blue B
green="\e[0;32m"

bwhite="\e[47m" # white background

rst="\e[0m" # Text reset

stage()
{
	echo -en "\n$green[***] "$blue"$1...$rst\n"
}

substage()
{
	echo -en "\n$green[*] $1$rst\n"
}

clone_project()
{
	if [ ! -d "../$2" ]; then
		echo -en $green"Clone $2$rst\n"
		git clone $1 ../$2
		cd ../$2
		git checkout $3
		cd -
	else
		echo -en "You can update "$green"$2"$rst" manualy$rst\n"
	fi
}
