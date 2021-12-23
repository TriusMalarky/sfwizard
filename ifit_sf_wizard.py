import py2exe;import win32com.client as comclt;import webbrowser

wsh=comclt.Dispatch("WScript.Shell")
webbrowser.open("https://iconfitness.lightning.force.com/lightning")
for i in range(17):
    wsh.SendKeys('{TAB}')
wsh.SendKeys("{ENTER}");wsh.SendKeys("{DOWN}");wsh.SendKeys("{DOWN}");wsh.SendKeys("{ENTER}")
print("Hello World!")
