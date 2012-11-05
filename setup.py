

































# This is the distutils script for creating a Python-based com exe
# server using ctypes.com.  This script should be run like this:
#
#  % python setup.py py2exe
#
# After you run this (from this directory) you will find two directories here:
# "build" and "dist".  The .exe file in dist is what you are looking for.
##############################################################################

#import win32traceutil
from distutils.core import setup
import py2exe
import sys
import os

try:
    # py2exe 0.6.4 introduced a replacement modulefinder.
    # This means we have to add package paths there, not to the built-in
    # one.  If this new modulefinder gets integrated into Python, then
    # we might be able to revert this some day.
    # if this doesn't work, try import modulefinder
    try:
        print "import py2exe.mf as modulefinder     "
        import py2exe.mf as modulefinder        
    except ImportError:
        import modulefinder
    import win32com, sys
    print "for p in win32com.__path__[1:]:"
    for p in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", p)
    for extra in ["win32com.shell"]: #,"win32com.mapi"
        __import__(extra)
        m = sys.modules[extra]
        for p in m.__path__[1:]:
            modulefinder.AddPackagePath(extra, p)
except ImportError:
    # no build path setup, no worries.
    pass

'''
if 1:
 try:
    import py2exe.mf as modulefinder
 except ImportError:
    import modulefinder
 import win32com
 for p in win32com.__path__[1:]:
     modulefinder.AddPackagePath("win32com", p)
 for extra in ["win32com.shell"]:
    __import__(extra)
    m = sys.modules[extra]
    for p in m.__path__[1:]:
        modulefinder.AddPackagePath(extra, p)    
    
print "finito*************"

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    #if os.path.basename(pathname).lower() in ("msvcp71.dll","dwmapi.dll", "mfc71.dll"):
    if os.path.basename(pathname).lower() in ("msvcp90.dll"):
        return 0
        return origIsSystemDLL(pathname)
        
py2exe.build_exe.isSystemDLL = isSystemDLL

'''

sys.path.append("C:\\Python27\\PYComServer_p\\Microsoft.VC90.CRT")

from glob import glob

data_files = [("Microsoft.VC90.CRT", 
              glob(r"C:\\Python27\\PYComServer_p\\Microsoft.VC90.CRT\\*.*"))
]

#import win32com
#import win32com.shell
#import win32com.shell.shell
#import win32com.shell.shellcon
#from win32com.shell.shellcon import *
#from win32com.shell import shell

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the version info resources (Properties -- Version)
        self.version = "0.0.1"
        self.company_name = "my company"
        self.copyright = "2006, my company"
        self.name = "my com server name"

mod_includes = [
    #"Cheetah.DummyTransaction",
    "win32com",
    "win32com.server.register",
    "os",
    "zipextimporter"
]       
        
mod_excludes = [
]          
        
dll_excludes = [
    "API-MS-Win-Core-LocalRegistry-L1-1-0.dll",
    "POWRPROF.dll",
    "w9xpopen.exe"
]
                
package_includes = [
##    "pkg_resources",
    ##"setuptools",
    #"win32com"
]
        
py2exe_options = {
    "optimize": 2, # 0 (None), 1 (-O), 2 (-OO)
    "includes": mod_includes,
    "excludes": mod_excludes,
    "dll_excludes": dll_excludes,
    "packages": package_includes,
    #"xref": False,
    # bundle_files: 1|2|3
    #    1: executable and library.zip
    #    2: executable, Python DLL, library.zip
    #    3: executable, Python DLL, other DLLs and PYDs, library.zip
    "bundle_files": 1
    #"dist_dir": dist_dir
}       
        
PyCOMServer = Target(
    description = "my com server",
    # use filename for ctypes.com exe server
    #script = "PYCOMServer_p\PyCOMServer.py",
    #modules = ["PythonUtilities"],
    #script = "PyCOMServer.py",
    # dest_base specifies basename of the exe file (should match setup name)
    dest_base = "PyCOMServer",
    # the following line embeds the typelib within the exe
    #other_resources = [("TYPELIB", 1, open(r"dc:\Python27\PyCOMServer.tlb", "rb").read())],
    # we only want the local (exe) server
    ##create_dll = True
    create_exe = True,
    create_dll = False    
    )

setup(
    name="PyCOMServer",
    # the following two parameters embed support files within exe file   
    #options={"py2exe": {"bundle_files": 1, }},
    options={"py2exe": py2exe_options},
    data_files=data_files,
    zipfile=None,
    version="0.0.1",
    description="my com server",
    # author, maintainer, contact go here:
    author="First Last",
    author_email="some_name@some_company.com",
    packages=["PyCOMServer_p"],
    #packages=["c:\Python27"],
    #console=[my_com_server_target]  
    com_server=["PyCOMServer"]
)    