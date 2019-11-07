#!/bin/bash

function install_python
{
	PATH='/Users/yharkati/sgoinfre/miniconda3.sh'
	echo 'dans la fonction install'
	$(/usr/bin/curl -s -o "$PATH" https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh && 
			/bin/chmod 777 "$PATH")
	if  [ 0 -eq $? ] 
	then
		echo 'fichier telecharger'
		# bash /miniconda.sh -b -p $HOME/miniconda
		$("$PATH" /Users/yharkati/sgoinfre/miniconda)

	else
		echo 'fichier non telecharger'
	fi
}


CMD='which python'
CMD1='python -V'
if [ "$1" = "install-python" ] 
then
	if $CMD | grep -q '/Users/yharkati/sgoinfre/miniconda/bin/python' ;  then
		if $CMD1 | grep -q 'Python 3.7.*' ; then
			echo 'python already installed, do you want to reinstall it ? '
			read -p " [yes | no] "
			if [ $REPLY != 'yes' ] 
			then
				echo "response yes"
				# install_python
			else
				echo "exit."
			fi
		else
			echo 'python not installed'
			# install_python
		fi
	else
		echo 'python not installed'		
		# install_python
	fi
else
	echo 'exit'
fi