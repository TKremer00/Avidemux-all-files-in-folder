# Avidemux all files in folder
This is a script to apply the same filters to all files in a folder using the program <a href="http://avidemux.sourceforge.net/"><strong>avidemux</strong></a>

## How to apply your own filter
In the applyAdmFilters methode you have to put your filters exept the filters :

<ul>
  <li>adm = Avidemux()
  <li>adm.loadVideo(".....")
  <li>adm.clearSegments()
  <li>adm.addSegment(0, 0, .....)
  <li>adm.markerA = 0
  <li>adm.markerB = ......
</ul>
  
## How to use
To run the script you have to download and install <a href="http://avidemux.sourceforge.net/">avidemux</a>.Then you click file>Project script>Run Project. Then you select this file. If the script runs you are promt to select a folder this is the folder where the files that you want to apply filters to are. Then you have to select the folder where you want to save to. 
