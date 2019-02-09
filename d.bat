@ECHO OFF
set done=false
set prefix=docker-compose
set suffix=
IF %1==prod (
    set prefix=docker-compose -f docker-compose.prod.yml
    SHIFT
)
IF %1==shell (
    set suffix= exec web sh
    set done=true
)

IF %1==bash (
    set suffix= exec web bash
    set done=true
)

IF %1==exec (
    @ECHO OFF
    :ExecLoop
    IF "%1"=="" GOTO ContinueExec
    set suffix=%suffix% %1
    SHIFT
    GOTO ExecLoop
    :ContinueExec
    set suffix=exec web %suffix%
    set done=true
)

IF %done%==false (
    @ECHO OFF
    :OtherLoop
    IF "%1"=="" GOTO ContinueOther
    set suffix=%suffix% %1
    SHIFT
    GOTO OtherLoop
    :ContinueOther
    set done=true
)

@ECHO ON
%prefix% %suffix%