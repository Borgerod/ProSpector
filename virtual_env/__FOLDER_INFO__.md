## What is this folder? - purpose & content

### Purpose:
Will install config settings as enviourment variables.
	"install_virtual_env.bat" is the manager of this folder 

### Content:
NOTE: I don't think 1-3 is nessasary since setEnv.bat has it all. 
1. /env/ : the enviourment containing the nessasary paths for config 
2. activate_env.bat : finds and calls the actual activate.bat
3. env_builder.bat : build the virtual env 
4. install_virtual_env.bat : The manager for all the bats
5. setEnv.bat : sets paths (security risk)