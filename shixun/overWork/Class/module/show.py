from shixun.overWork.Class.IO.AllUserIO import AllUserIO
from shixun.overWork.Class.module.showOfUser import showOfUser
from shixun.overWork.Class.module.showOfSuperUser import showOfSuperUser
from shixun.overWork.Class.module.showOfMerchanter import showOfMerchanter
from shixun.overWork.Class.module.chooseMode import chooseMode
def show():
    io=AllUserIO()
    loginUser=io.getIO(pathIndex=4)
    if loginUser['perMission']==1:
        showOfUserAgain = showOfUser(loginUser=loginUser)
        while showOfUserAgain:
            showOfUserAgain = showOfUser(loginUser=loginUser)
    if loginUser['perMission']==2:
        showOfMerchanterAgain=showOfMerchanter(loginUser=loginUser)
        while  showOfMerchanterAgain:
            showOfMerchanterAgain = showOfMerchanter(loginUser=loginUser)
    if loginUser['perMission']==3:
        showOfSuperUserAgain = showOfSuperUser(loginUser=loginUser)
        while showOfSuperUserAgain:
            showOfSuperUserAgain = showOfSuperUser(loginUser=loginUser)
    print("-" * 10 + "正在跳转到登录页面" + "-" * 10)
    print("-" * 10 + "跳转成功" + "-" * 10)
    chooseMode()
    show()