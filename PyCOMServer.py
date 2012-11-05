import sys
class PythonUtilities:
  _public_methods_ = [ 'SplitString', 'SumInteger', 'HelloWorld' ]
  _reg_desc_ = "PythonDemos Utilities "
  _reg_progid_ = "PythonDemos.Utilities"
  # NEVER copy the following ID 
  # Use "print pythoncom.CreateGuid()" to make a new one.
  _reg_clsid_ = "{D7ED4E9F-6569-4B02-A806-C028867E5252}"

  def SplitString(self, val, item=None):
    import string
    if item != None: item = str(item)
    return string.split(str(val), item)

  def SumInteger(self, num1, num2=None):    
    if num2 != None: 
      return str(num1 + num2)
      return str(num1)

  def HelloWorld():
      return "Hello World"  
      

def Register():
    import win32com.server.register
    print "Registger"	
    return win32com.server.register.UseCommandLine(PythonUtilities)
	
def UnRegister():
    import win32com.server.register
    print "Unregister"
    return win32com.server.register.UseCommandLine(PythonUtilities)	

# Add code so that when this script is run by
# Python.exe, it self-registers.
if __name__=='__main__':
    #print "Registering COM server..."
    #import win32com.server.register
   #win32com.server.register.UseCommandLine(PythonUtilities)
 

    if '/register' in sys.argv[1:] or '/unregister' in sys.argv[1:]:
           if  sys.argv[1:] == '/register':
              Register()
           else:
              UnRegister()
    else:
           Register()
