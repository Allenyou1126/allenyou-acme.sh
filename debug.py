from allenyoucert import Cert
import env

def debugMain():
    print(env.DEBUG)
    testCert = Cert(["allenyou.wang", "*.allenyou.wang"], "rsa", "dns_cf")
    testCert.issue()

env.DEBUG = True
debugMain()