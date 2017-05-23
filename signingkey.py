import hmac
import hashlib
# key = 'wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY'
# dateStamp = '20120215'
# regionName = 'us-east-1'
# serviceName = 'iam'

def sign(key,msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_reguest")
    return kSigning

# b = sign("wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",20120215);
c = getSignatureKey('wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY','20120215','us-east-1','iam');
print c;
