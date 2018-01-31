@ECHO OFF
set cmds=shell, exec
set done=false

IF %1==shell (
    docker-compose exec web sh
    set done=true
)

IF %1==exec (
    @ECHO ON
    for /f "tokens=1,* delims= " %%a in ("%*") do @ECHO OFF && set ALL_BUT_FIRST=%%b
    docker-compose exec web %ALL_BUT_FIRST%
    set done=true
)

IF %done%==false (
    ECHO You must use one of the following command: %cmds%
)