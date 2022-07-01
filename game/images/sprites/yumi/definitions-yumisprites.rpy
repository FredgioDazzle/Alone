
init python:

    YUMI_DIR_n = "sprites/Yumi/yumi_normal/"
    YUMI_DIR_f = "sprites/Yumi/yumi_front/"

    make_sprites("yumi", "yumi_normal", "yn", 1, 4, 2, 2, 6, 1, 1, False, True, 3)
    make_sprites("yumi", "yumi_front", "yf", 2, 4, 2, 2, 7, 1, 1, False, True, 5)

image ynsbody01 = LiveComposite((591, 960), (0,0), "yn1al", (0,0), "yn1ar", (0,0), "ynhead")

image yfsbody01 = LiveComposite((591, 960), (0,0), "yf1al", (0,0), "yf1ar", (0,0), "yfhead1")
image yfsbody02 = LiveComposite((591, 960), (0,0), "yf1bl", (0,0), "yf1ar", (0,0), "yfhead1")

image yfslbody01 = LiveComposite((591, 960), (0,0), "yf4al", (0,0), "yf4ar", (0,0), "yfhead1")
image yfslbody02 = LiveComposite((591, 960), (0,0), "yf4bl", (0,0), "yf4ar", (0,0), "yfhead1")

######################################################

image yumi ns01 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows1", (0,0), "yneye1", (0,0), "ynmouth1")
image yumi ns02 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows1", (0,0), "yneye1", (0,0), "ynmouth2")
image yumi ns03 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows1", (0,0), "yneye1", (0,0), "ynmouth4")
image yumi ns04 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows1", (0,0), "yneye1", (0,0), "ynmouth5")
image yumi ns05 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows1", (0,0), "yneyeexp1", (0,0), "ynmouth2")
image yumi ns06 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows1", (0,0), "yneyeexp1", (0,0), "ynmouth1")
image yumi ns07 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows2", (0,0), "yneye2", (0,0), "ynmouth5")
image yumi ns08 = LiveComposite((591, 960), (0,0), "ynsbody01", (0,0), "yneyebrows2", (0,0), "yneye2", (0,0), "ynmouth4")

image yumi fs01 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth1")
image yumi fs02 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth2")
image yumi fs03 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth4")
image yumi fs04 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth5")
image yumi fs05 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth2")
image yumi fs06 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth1")
image yumi fs07 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth5")
image yumi fs08 = LiveComposite((591, 960), (0,0), "yfsbody01", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth4")

image yumi fsb01 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth1")
image yumi fsb02 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth2")
image yumi fsb03 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth4")
image yumi fsb04 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth5")
image yumi fsb05 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth2")
image yumi fsb06 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth1")
image yumi fsb07 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth5")
image yumi fsb08 = LiveComposite((591, 960), (0,0), "yfsbody02", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth4")

image yumi fsl01 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth1")
image yumi fsl02 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth2")
image yumi fsl03 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth4")
image yumi fsl04 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth5")
image yumi fsl05 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth2")
image yumi fsl06 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth1")
image yumi fsl07 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth5")
image yumi fsl08 = LiveComposite((591, 960), (0,0), "yfslbody01", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth4")

image yumi fslb01 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth1")
image yumi fslb02 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth2")
image yumi fslb03 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth4")
image yumi fslb04 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows1", (0,0), "yfeye1", (0,0), "yfmouth5")
image yumi fslb05 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth2")
image yumi fslb06 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows1", (0,0), "yfeyeexp1", (0,0), "yfmouth1")
image yumi fslb07 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth5")
image yumi fslb08 = LiveComposite((591, 960), (0,0), "yfslbody02", (0,0), "yfeyebrows2", (0,0), "yfeye2", (0,0), "yfmouth4")

