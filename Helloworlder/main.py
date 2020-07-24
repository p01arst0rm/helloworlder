import os
import sys




class helloworlder:

        # private variables
        #----------------------------------------------------------------------------




        # Error handler
        #----------------------------------------------------------------------------

        def log_handle(self, log, log_file):
                print(log)
                with open(log_file, "a") as x:
                    x.write(log + "\n")
           

        def log_notify(self, notif):
                self.log_handle(str("[-]: "+notif),self.notify_log_file)


        def log_warn(self, warn):
                self.log_handle(str("[WARNING]: "+warn),self.warn_log_file)


        def log_err(self, err):
                self.log_handle(str("[ERROR]: "+err),self.err_log_file)
                sys.exit()         




        # setters
        # ---------------------------------------------------------------------------           

        def set_project_dir(self, x):
                twelete.filter_media = True
                self.media_filter = x




        # getters
        # ---------------------------------------------------------------------------      
       
        def get_query(self, request):
            self.log_notify(request)
            while True:
                    try:
                            response = input("> ")
                            if response in ("y","Y"):
                                    return True
                            elif response in ("n","N"):
                                    return False
                            else:
                                    raise ValueError()
                    except ValueError:
                            self.log_warn("Please enter \"Y\" or \"N\"")




        # project management
        # ---------------------------------------------------------------------------

        def make_project_dir(self):
            if (os.path.exists(self.project_build_dir)) or (self.project_build_dir == ''):
                self.log_warn(str("Chosen project path already exists."))
                if not self.get_query("Do you wish to continue? (y/n)"):
                    sys,exit()
            else:
                try:
                    os.makedirs(self.project_build_dir)
                except OSError as e: # Guard against race condition
                    self.log_err(str(e))


        def set_project_config(self):
            a = 0

        
        def get_confirm(self):
            print("-----------------------------------")
            self.log_notify(str("Project build directory: {}").format(self.project_build_dir))



            print("-----------------------------------")
            response = self.get_query("Do you wish to continue? (y/n)")
            return response




        # main
        # ---------------------------------------------------------------------------       
        def run(self):
            while True:
                check_settings = self.get_confirm()
                if check_settings:
                    break
                else:
                    self.set_project_config()
            

            self.make_project_dir()
            sys.exit()

                
        def __init__(self):

                # directory of twitter archive
                self.project_build_dir = "./MyProject"
                
                # project name
                self.project_name = "MyProject"

                self.project_lang = "Python"

                #log files
                self.notify_log_file = "./helloworlder.log"
                self.warn_log_file = "./helloworlder.log"
                self.err_log_file = "./helloworlder.log"
