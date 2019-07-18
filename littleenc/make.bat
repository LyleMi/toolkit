@ECHO OFF

if "%1" == "clear" goto clear
if "%1" == "test" goto test

go fmt enc.go
go build
goto end

:test
go build
littleenc -h
littleenc -e -f enc.go
littleenc -d -f enc.go.enc
goto end

:clear
rm -rf *.key
rm -rf *.exe
goto end

:end
