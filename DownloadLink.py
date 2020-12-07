from LinkList import Getlinks

class DlLink:

    # Return list of Download Links
    def DlList(self,webln,sid):
        self.webln=webln
        self.sid = sid
        lnArr = Getlinks().getlink(web = webln)
        arr=[]
        for i in lnArr:
            arr.append(Getlinks().getMp4(i, cookieSid = sid))
        return arr