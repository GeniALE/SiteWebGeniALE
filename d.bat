@ECHO OFF
set done=false
set prefix=docker-compose
IF %1==prod (
    set prefix=docker-compose -f docker-compose.prod.yml
    SHIFT
)
IF %1==shell (
    %prefix% exec web sh
    set done=true
)

IF %1==exec (
    @ECHO ON
    for /f "tokens=1,* delims= " %%a in ("%*") do @ECHO OFF && set ALL_BUT_FIRST=%%b
    %prefix% exec web %ALL_BUT_FIRST%
    set done=true
)

IF %done%==false (
    @ECHO ON
    for /f "tokens=1,* delims= " %%a in ("%*") do @ECHO OFF && set ALL_BUT_FIRST=%%b
    %prefix% %ALL_BUT_FIRST%
)