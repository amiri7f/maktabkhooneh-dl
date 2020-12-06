from LinkList import Getlinks

class DlLink:

    # Return list of Download Links
    def DlList(self,webln):
        self.webln=webln
        lnArr = Getlinks().getlink(web = webln)
        print(lnArr)
        arr=[]
        for i in lnArr:
            arr.append(Getlinks().getMp4(i))
        return arr