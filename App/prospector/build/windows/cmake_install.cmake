# Install script for directory: C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "$<TARGET_FILE_DIR:prospector>")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/flutter/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/bitsdojo_window_windows/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_acrylic/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_secure_storage_windows/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/url_launcher_windows/cmake_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/prospector.exe")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug" TYPE EXECUTABLE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/prospector.exe")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/prospector.exe")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile" TYPE EXECUTABLE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/prospector.exe")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/prospector.exe")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release" TYPE EXECUTABLE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/prospector.exe")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/data/icudtl.dat")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/data" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows/flutter/ephemeral/icudtl.dat")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data/icudtl.dat")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows/flutter/ephemeral/icudtl.dat")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data/icudtl.dat")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows/flutter/ephemeral/icudtl.dat")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/flutter_windows.dll")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows/flutter/ephemeral/flutter_windows.dll")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/flutter_windows.dll")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows/flutter/ephemeral/flutter_windows.dll")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/flutter_windows.dll")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/windows/flutter/ephemeral/flutter_windows.dll")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/bitsdojo_window_windows_plugin.lib;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/flutter_acrylic_plugin.dll;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/flutter_secure_storage_windows_plugin.dll;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/url_launcher_windows_plugin.dll")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug" TYPE FILE FILES
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/bitsdojo_window_windows/Debug/bitsdojo_window_windows_plugin.lib"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_acrylic/Debug/flutter_acrylic_plugin.dll"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_secure_storage_windows/Debug/flutter_secure_storage_windows_plugin.dll"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/url_launcher_windows/Debug/url_launcher_windows_plugin.dll"
      )
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/bitsdojo_window_windows_plugin.lib;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/flutter_acrylic_plugin.dll;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/flutter_secure_storage_windows_plugin.dll;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/url_launcher_windows_plugin.dll")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile" TYPE FILE FILES
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/bitsdojo_window_windows/Profile/bitsdojo_window_windows_plugin.lib"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_acrylic/Profile/flutter_acrylic_plugin.dll"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_secure_storage_windows/Profile/flutter_secure_storage_windows_plugin.dll"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/url_launcher_windows/Profile/url_launcher_windows_plugin.dll"
      )
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/bitsdojo_window_windows_plugin.lib;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/flutter_acrylic_plugin.dll;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/flutter_secure_storage_windows_plugin.dll;C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/url_launcher_windows_plugin.dll")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release" TYPE FILE FILES
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/bitsdojo_window_windows/Release/bitsdojo_window_windows_plugin.lib"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_acrylic/Release/flutter_acrylic_plugin.dll"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/flutter_secure_storage_windows/Release/flutter_secure_storage_windows_plugin.dll"
      "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/plugins/url_launcher_windows/Release/url_launcher_windows_plugin.dll"
      )
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    
  file(REMOVE_RECURSE "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/data/flutter_assets")
  
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    
  file(REMOVE_RECURSE "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data/flutter_assets")
  
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    
  file(REMOVE_RECURSE "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data/flutter_assets")
  
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/data/flutter_assets")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Debug/data" TYPE DIRECTORY FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build//flutter_assets")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data/flutter_assets")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data" TYPE DIRECTORY FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build//flutter_assets")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data/flutter_assets")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data" TYPE DIRECTORY FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build//flutter_assets")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Pp][Rr][Oo][Ff][Ii][Ll][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data/app.so")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Profile/data" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/app.so")
  elseif("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data/app.so")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/runner/Release/data" TYPE FILE FILES "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/app.so")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/App/prospector/build/windows/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
