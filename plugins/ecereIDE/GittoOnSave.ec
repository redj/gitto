import "ecere"
import "ecereIDE"

class GittoOnSave : IDEEventListener
{
   GittoOnSaveQueue queue { };

   void Init()
   {
      queue.Create();
   }

   void Destroy()
   {
      queue.Terminate();
   }

   void OnFileSave(String filePath)
   {
      char cwd[MAX_DIRECTORY];
      char path[MAX_DIRECTORY];
      StripLastDirectory(filePath, path);
      queue.Add(path);
   }
}

class GittoOnSaveQueue : Thread
{
   bool terminate;
   Array<String> paths { };
   Mutex control { };
   Semaphore work { };

   unsigned int Main()
   {
      for(;;)
      {
         work.Wait();
         control.Wait();
         if(terminate)
         {
            control.Release();
            break;
         }
         else
            control.Release();
         while(paths.count)
         {
            char * firstPath;
            char cwd[MAX_DIRECTORY];
            char path[MAX_DIRECTORY];
            int count;
            control.Wait();
            count = paths.count;
            firstPath = paths[0];
            strcpy(path, firstPath);
            paths.firstIterator.Remove();
            control.Release();
            GetWorkingDir(cwd, MAX_DIRECTORY);
            while(FileExists(path).isDirectory)
            {
               char git[MAX_LOCATION] = "";
               char gitto[MAX_LOCATION] = "";
               strcpy(git, path);
               strcpy(gitto, path);
               PathCat(git, ".git");
               PathCat(gitto, ".gitto");
               if(FileExists(git).isDirectory && FileExists(gitto).isFile)
               {
                  ChangeWorkingDir(path);
                  Execute("gitto flash");
                  Sleep(1);
               }
               StripLastDirectory(path, path);
            }
            ChangeWorkingDir(cwd);
            delete firstPath;
         }
      }
      return 0;
   }

   void Add(String newPath)
   {
      control.Wait();
      if(!paths.Find(newPath))
      {
#if 0
         //bool worked = true;
         //while(worked)
         {
            //worked = false;
            Iterator<String> it { paths };
            while(it.Next())
            {
               String path = it.data;
               PrintLn("IsPathInsideOf(\"", newPath, "\", \"", path, "\")");
               if(IsPathInsideOf(newPath, path))
               {
                  PrintLn("GittoOnSaveQueue::Add -- removing ", path);
                  it.Remove();
                  delete path;
                  //worked = true;
                  //break;
               }
            }
         }
         PrintLn("GittoOnSaveQueue::Add -- adding ", newPath);
#endif
         paths.Add(CopyString(newPath));
      }
      control.Release();
      work.Release();
   }

   void Terminate()
   {
      if(created)
      {
         control.Wait();
         terminate = true;
         control.Release();
         work.Release();
         Wait();
      }
   }

   ~GittoOnSaveQueue()
   {
      paths.Free();
   }
}
