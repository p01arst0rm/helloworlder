import os
import sys
import ast
import json
import glob
import tweepy
import dateutil.parser
import zipfile
import tempfile

class twelete:

        # private variables
        #----------------------------------------------------------------------------
        api_key_set = False
        access_token_set = False

        
        filter_date = False
        filter_activity = False
        filter_media = False

        
        filter_phrase_black = False
        filter_phrase_white = False

        
        # variable selection
        # ---------------------------------------------------------------------------           

        def set_media_filter(self, x):
                twelete.filter_media = True
                self.media_filter = x



        # Error handler
        #----------------------------------------------------------------------------
        def log_handle(self, log, log_file):
                print(log)
                with open(log_file, "a") as x:
                    x.write(log + "\n")
           

        def log_notify(self, notif):
                self.log_handle(str("[INFO]: "+notif),self.notify_log_file)


        def log_warn(self, warn):
                self.log_handle(str("[WARNING]: "+warn),self.warn_log_file)


        def log_err(self, err):
                self.log_handle(str("[ERROR]: "+err),self.err_log_file)
                sys.exit()         





        # main
        # ---------------------------------------------------------------------------       
        def run(self):
                self.get_api_tokens()
                self.get_filters()
                self.archive_dir=self.get_archive_dir()
                confirm_delete = self.get_confirm()
                

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