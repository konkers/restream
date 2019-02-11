# Script to pull up four streams for restreaming, based off python 3.5
#
# created by legendharvest. Copyright 2019.
# edited by konkers
# available under the MIT License for free use and distribution
#
# Permission is hereby granted, free of charge, to any person obtaining a coply
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#  IN THE SOFTWARE.

import os
import platform
import subprocess
import sys
import winreg


def find_streamlink():
    try:
        # must run as administrator
        streamlink_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, "\\".join(
                ["SOFTWARE", "WOW6432Node", "Microsoft", "Windows",
                 "CurrentVersion", "Uninstall", "Streamlink"]))

        # path where the streamlink exe is on the person's machine
        install_location = winreg.QueryValueEx(
            streamlink_key, "InstallLocation")
        return "{}\\bin\\streamlink.exe".format(install_location[0])
    except FileNotFoundError:
        err_desc = "Can't find streamlink.  Is it installed?"
        arch = platform.architecture()
        if arch[0] == '64bit':
            err_desc += "\nRunning 64bit OS.  Make sure to use 64bit python!\n"
        raise FileNotFoundError(err_desc)


if __name__ == '__main__':

    streamlink_path = find_streamlink()

    streams = sys.argv[1:]

    if len(streams) <= 0:
        # We could read IDs from stdin like the old script here.
        print("Please specify twich IDs as command line args.")
        sys.exit(1)

    print("Pulling up all the streamers now:", ", ".join(streams))

    print(streamlink_path)

    for stream in streams:
        url = "twitch.com/" + stream
        subprocess.Popen([streamlink_path, url, "best"])
