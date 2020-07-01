@echo off

rem set SPOTIPY_CLIENT_ID=9cc00db81f484366b336868b3c1cfefc
rem set SPOTIPY_CLIENT_SECRET=d98939e4af9e40c9b2227f50f9db36a1


IF %1.==. GOTO No1
IF "%SPOTIPY_CLIENT_ID%"=="" GOTO NoSpotipy
IF "%SPOTIPY_CLIENT_SECRET%"=="" GOTO NoSpotipy

:runprogram

python.exe .\load_artist_songs.py %*

GOTO End1

:No1
  python.exe .\load_artist_songs.py --help
GOTO End1

:NoSpotipy
set /P SPOTIPY_CLIENT_ID=Your Client ID:
set /P SPOTIPY_CLIENT_SECRET=Your Client Secret:
GOTO runprogram


:End1

