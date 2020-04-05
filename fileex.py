import os
import shutil

filelist = [
	"Assets/Complete Vehicle Pack V2/Textures/Cars_2_D.tif",
	"Assets/Complete Vehicle Pack V2/Textures/Cars_2_D(EU).tif",
	"Assets/Complete Vehicle Pack V2/Textures/Cars_2_G(EU).tif",
	"Assets/Complete Vehicle Pack V2/Textures/Cars_2_E.tif",
	"Assets/Standard Assets/Effects/LightCookies/Textures/FlashlightIrregularCookie.tif",
	"Assets/_materials/Skyboxes/Textures/Sunny1/Sunny1_right.tif",
	"Assets/_materials/Skyboxes/Textures/Sunny1/Sunny1_back.tif",
	"Assets/_materials/Skyboxes/Textures/Sunny1/Sunny1_down.tif",
	"Assets/Standard Assets/Effects/GlassRefraction/Textures/GlassStainedNormals.tif",
	"Assets/Standard Assets/Effects/GlassRefraction/Textures/GlassStainedAlbedo.tif",
	"Assets/Standard Assets/Effects/LightCookies/Textures/FlashlightCookie.tif",
	"Assets/_materials/Skyboxes/Textures/Sunny1/Sunny1_up.tif",
	"Assets/_materials/Skyboxes/Textures/Sunny1/Sunny1_front.tif",
	"Assets/_materials/Skyboxes/Textures/Sunny1/Sunny1_left.tif",
	"Assets/_textures/laser.tif",
	"Assets/Complete Vehicle Pack V2/Textures/Smoke_Particle.tif",
	"Assets/SampleScenes/Textures/FlyerPlayershipOcclusion.tif",
	"Assets/SampleScenes/Textures/FlyerPlayershipEmission.tif",
	"Assets/SampleScenes/Textures/FlyerPlayershipAlbedo.tif",
	"Assets/SampleScenes/Textures/FlyerAsteroidEmissive.tif",
	"Assets/Complete Vehicle Pack V2/Textures/Cars_2_G.tif",
	"Assets/Standard Assets/Effects/LightCookies/Textures/LightSoftCookie.tif"]

for fn in filelist:
    #frpathname = "d:/unity/onefloortestforparking/"+fn
    frpathname = "d:/unity/protocampsim/"+fn
    isthere = os.path.exists(frpathname)
    fsize = os.path.getsize(frpathname)
    print(f"isthere:{isthere} sz:{fsize:>10} - {frpathname}")
    #shutil.copyfile(frpathname, tupathname)
