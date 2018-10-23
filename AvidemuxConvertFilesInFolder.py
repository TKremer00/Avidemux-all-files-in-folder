import os

gui = Gui()
adm = Avidemux()
#Place your extention to start with.
ext = "mp4"
sep = "\\"


#always let the user first select source folder 
inputFolder = gui.dirSelect("Select the source folder", "test")

#apply filters
def convert(filein):   
  filename = basename(filein)
  dir = dirname(filein)
  if(0 == adm.loadVideo(filein)):
      ui.displayError("oops","cannot load "+filein)
      raise
  
  applyAdmFilters(filein)
  #save to the selected folder whit the same name as started
  adm.save(folder_to_save + sep + filename)
  
  print("Done")    

'''
place here your adm filters
make sure they all have 1 tab or the same ammount of spaces 
except 
adm = Avidemux()
adm.loadVideo(".....")
adm.clearSegments()
adm.addSegment(0, 0, .....)
adm.markerA = 0
adm.markerB = ......
'''  
def applyAdmFilters(filein):
  adm.videoCodec("xvid4", "params=CBR=1500", "profile=244", "rdMode=3", "motionEstimation=3", "cqmMode=0", "arMode=1", "maxBFrame=2", "maxKeyFrameInterval=200", "nbThreads=99", "qMin=2", "qMax=25", "rdOnBFrame=True", "hqAcPred=True"
  , "optimizeChrome=True", "trellis=True", "useXvidFCC=False")
  adm.addVideoFilter("asharp", "t=1.000000", "d=1.000000", "b=4.000000", "bf=False")
  adm.addVideoFilter("swscale", "width=848", "height=480", "algo=2", "sourceAR=0", "targetAR=0", "lockAR=False", "roundup=False")
  adm.addVideoFilter("fluxsmooth", "temporal_threshold=8", "spatial_threshold=3")
  adm.addVideoFilter("lavdeint", "deintType=1", "autoLevel=True")
  adm.addVideoFilter("eq2", "contrast=1.110000", "brightness=0.080000", "saturation=1.780000", "gamma=0.870000", "gamma_weight=1.000000", "rgamma=1.000000", "bgamma=1.000000", "ggamma=1.000000")
  adm.audioClearTracks()
  adm.setSourceTrackLanguage(0,"und")
  adm.audioAddTrack(0)
  adm.audioCodec(0, "copy");
  adm.audioSetDrc(0, 0)
  adm.audioSetShift(0, 0,0)
  adm.setContainer("MP4", "muxerType=0", "useAlternateMp3Tag=True", "forceAspectRatio=False", "aspectRatio=1")
  
#
try : 
	list = get_folder_content(inputFolder,ext)
	#Select a save folder if there are files in the list
	if(list is None):
	    raise
	else:
        folder_to_save = gui.dirSelect("Select a folder to save to")	
	
	for i in list:
        convert(i)
except:
	gui.displayError("Error","An issue occurred")
