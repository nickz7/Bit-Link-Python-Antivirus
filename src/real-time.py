import os

import win32file
import win32con
import engine

def RealTime(): 

  usernameUp = os.environ.get('USERNAME').upper().split(" ")
  username = os.environ.get('USERNAME')

  ACTIONS = {
    1 : "Created",
    2 : "Deleted",
    3 : "Updated",
    4 : "Renamed from something",
    5 : "Renamed to something"
  }

  FILE_LIST_DIRECTORY = 0x0001

  path_to_watch = "C:\\"
  hDir = win32file.CreateFile (
    path_to_watch,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
  )
  while 1:
  
    results = win32file.ReadDirectoryChangesW (
      hDir,
      1024,
      True,
      win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
      win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
      win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
      win32con.FILE_NOTIFY_CHANGE_SIZE |
      win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
      win32con.FILE_NOTIFY_CHANGE_SECURITY,
      None,
      None
    )

    paths = [] 
  
    for action, file in results:
      paths.append(os.path.join (path_to_watch, file))
    
      if paths[0][0:32] == "C:\\Users\\{}\\AppData\\".format(username):paths.clear()
      elif paths[0][0:18] == "C:\\Users\\{}~1\\".format(usernameUp[0]):paths.clear()
      elif paths[0][0:20] == "C:\\Windows\\Prefetch\\":paths.clear()
      elif paths[0][0:15] == "C:\\Windows\\Temp":paths.clear()
      elif paths[0][0:15] == "C:\\$Recycle.Bin":paths.clear()
      elif paths[0][0:14] == "C:\\ProgramData":paths.clear()
      elif paths[0][0:23] == "C:\\Windows\\ServiceState":paths.clear()
      elif paths[0][0:15] == "C:\\Windows\\Logs":paths.clear()
      elif paths[0][0:26] == "C:\\Windows\\ServiceProfiles":paths.clear()
      elif paths[0][0:19] == "C:\\Windows\\System32":paths.clear()
      elif paths[0][0:28] == "C:\\Program Files\\CUAssistant":paths.clear()
      elif paths[0][0:23] == "C:\\Windows\\bootstat.dat":paths.clear()

      # try:print (paths[0], ACTIONS.get (action, "Unknown"))
      # except:pass
      try:engine.virusScanner(paths[0])
      except:pass
      paths.clear()
    

RealTime()