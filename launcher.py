# Script to pull up four streams for restreaming, based off python 3.5 
# created by legendharvest and available under the MIT License for free use and distribution

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os, platform, subprocess
import winreg

# for python 2.7
#import _winreg as winreg

if __name__ == '__main__':
    
    #prompt for user input
    stream1 = input("Please enter the first streamer to pull up in streamlink via VLC: ")
    stream2 = input("Who is the next streamer: ")
    stream3 = input("Who is the next streamer: ")
    stream4 = input("Who is the next streamer: ")
    
    print("Pulling up all the streamers now:", stream1, stream2, stream3, stream4)
    
    # todo, check for right architecture, or just assume you know where the exe will be...
    arch = platform.architecture()
    if arch[0] == '64bit':
        print("running 64bit OS, make sure to use 64bit python!\r\n")
        
    # if on a 64bit machine, this will fail if using 32bit python HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Streamlink\InstallLocation
    
    # must run as administrator
    streamlink_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Streamlink")
    
    # path where the streamlink exe is on the person's machine
    s_location = winreg.QueryValueEx(streamlink_key, "InstallLocation")
    
    # actually set the exe to this path (dont forget to add "bin")
    s_file = s_location[0] + "\\" + "bin" + "\\" + "streamlink.exe"
    
    # there is the option to go to this directory, but let's not for now
    #os.chdir(s_location[0])
    
    # can use this to see what all is in our directory
    #import glob
    #print (glob.glob("*"))
    
    # prep the streams
    # yes I know I could use a loop
    stream1 = "twitch.tv/" + stream1
    stream2 = "twitch.tv/" + stream2
    stream3 = "twitch.tv/" + stream3
    stream4 = "twitch.tv/" + stream4
    
    # call the streams - use popen rather than call to not wait for the first command to complete
    subprocess.Popen([s_file, stream1, "best"])
    subprocess.Popen([s_file, stream2, "best"])
    subprocess.Popen([s_file, stream3, "best"])
    subprocess.Popen([s_file, stream4, "best"])