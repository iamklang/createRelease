import sys 
from subprocess import call

#call(["cd", sys.argv[1]])

call(["pwd"])
call(["git", "checkout", "master"])
call(["git", "pull", "origin", "master"])

call(["git", "checkout", "develop"])
call(["git", "pull", "origin", "develop"])

call(["git", "fetch", "--all"])

call(["git", "flow", "release", "start", sys.argv[1]])
call(["git", "flow", "release", "finish", "-m", sys.argv[1], sys.argv[1]])
