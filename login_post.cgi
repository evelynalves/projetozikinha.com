#!/bin/bash
read login
falhou(){
echo "<h2> O nome de usuário e/ou senha inserido não pertence a um usuário. Verifique seu nome de usuário e/ou senha e tente novamente. </h2>"
}
administrador(){
cat 'pgnadm.html'
exit 0
}
tecnico(){
cat 'pgntec.html'
exit 0
}
usuario(){
cat 'pgnusr.html' 
exit 0
}
passou(){
[[ $1 == "administrador" ]] && administrador
[[ $1 == "tecnico" ]] && tecnico
[[ $1 == "usuario" ]] && usuario
}
verifica(){
USER=$1
PASS=$2
SENHA=$(cat passwd | grep ^$USER: | cut -d":" -f2)
[[ $PASS == $SENHA ]] && passou $USER || falhou
}

USER=$(echo $login | cut -d"&" -f1 | cut -d"=" -f2 )
PASS=$(echo $login | cut -d"&" -f2 | cut -d"=" -f2 )
echo content-type: text/html
echo
[[ $(cat passwd | cut -d":" -f1 | grep ^$USER$) ]] && verifica $USER $PASS || falhou
