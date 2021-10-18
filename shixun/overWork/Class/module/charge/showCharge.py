from shixun.overWork.Class.IO.AllUserIO import  AllUserIO
def showCharge(loginUser=None):
    io=AllUserIO(user=loginUser)
    jsonData=io.selectById()
    return jsonData['charge']
    pass