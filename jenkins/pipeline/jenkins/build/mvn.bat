@echo off
REM Script para executar comando Docker sem privilégios de administrador

docker run --rm -v "C:/Users/admin/Desktop/formação/material-de-foma-oes/jenkins/pipeline/java-app:/app" -v "/root/.m2/:/root/.m2/"  -w /app maven:3-alpine mvn -X -B -DskipTests clean package

REM Pausa opcional para visualização do resultado
pause
