import os
import sys
import subprocess
import yaml

log_dir = "/afs/cern.ch/user/b/boguo/KingMaker/data/jobs/"

def checklog(sample_list):
    for _dir in os.listdir(log_dir):
        if ("tmp" in _dir) and (os.path.isdir(os.path.join(log_dir, _dir))):
            # print(_dir)
            tmpdir = log_dir + _dir
            for f in os.listdir(tmpdir):
                if (f.startswith("std") and f.endswith(".txt")):
                    _cmd = "grep -rn ' nick=' {0}/{1}".format(tmpdir,f)
                    result_nick = subprocess.run(_cmd, shell=True, capture_output=True, text=True)
                    # print(result_nick.stdout)
                    for n in sample_list:
                        if n in result_nick.stdout:
                            print(tmpdir)
                            print(n)
                            print("total file should be {}".format(str(sample_list[n]['nfiles'])))
                            print("Next should be 'exit code 0' and 'Overall runtime'")
                            
                            _cmd1 = "grep -rn 'job exit code : 0' {0}/std*.txt | wc -l ".format(tmpdir)
                            _cmd2 = "grep -rn 'Overall runtime' {0}/std*.txt | wc -l ".format(tmpdir)
                            os.system(_cmd1)
                            os.system(_cmd2)
                    break

            
if __name__ == '__main__':
    with open("/afs/cern.ch/user/b/boguo/KingMaker/sample_database/datasets.yaml" , "r") as yamlfile:
        sample_list =  yaml.safe_load(yamlfile)
        checklog(sample_list)
