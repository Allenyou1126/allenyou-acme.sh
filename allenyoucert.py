import env
import os

class Cert(object):
    def __init__(self, names, type, dnsapi) -> None:
        super().__init__()
        self.names = names
        self.type = type
        self.dnsapi = dnsapi
    def issue(self) -> None:
        commandToRun = "~/.acme.sh/acme.sh --issue --dns " + self.dnsapi
        for key in self.names:
            commandToRun = commandToRun + " -d " + key
        commandToRun = commandToRun + " --keylength " + self.type
        if env.DEBUG == True: # Debug Command
            print(commandToRun)
        if env.DEBUG == False:
            os.system(commandToRun)

def cert2dict(a) -> dict:
    return {
        'name' : a.names,
        'type': a.type,
        'dnsapi': a.dnsapi
    }