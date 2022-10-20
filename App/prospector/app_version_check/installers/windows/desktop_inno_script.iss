; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "ProSpector"
#define MyAppVersion "0.9"
#define MyAppPublisher "A.Borger�d"
#define MyAppURL "https://github.com/Borgerod"
#define MyAppExeName "prospector.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{A38EE882-4DAB-4547-8015-79DCFF80D696}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\app_version_check\installers\windows
OutputBaseFilename=setup
SetupIconFile=C:\Users\Big Daddy B\Downloads\setup.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "norwegian"; MessagesFile: "compiler:Languages\Norwegian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\bitsdojo_window_windows_plugin.lib"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\flutter_acrylic_plugin.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\flutter_secure_storage_windows_plugin.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\flutter_windows.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\prospector.exp"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\prospector.lib"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\run_server.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\url_launcher_windows_plugin.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\api_server\*"; DestDir: "{app}\api_server"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\python_test.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\check_python.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\pythonpath.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\python_installer.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\App\prospector\build\windows\runner\Release\RefreshEnv.cmd"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
Filename: "{app}\check_python.bat"; Parameters: "install";


