#source("http://bioconductor.org/biocLite.R")
#biocLite("EBImage")
library('EBImage')
library('seewave')
library('tuneR')
setWavPlayer("afplay")

filename <- '~/Downloads/set1.wav'
song <- readWave(filename)

flim<-c(0,.8)
tlim<-c(126,148)
s <-spectro(song,wl=8000,ovlp=80,tlim=tlim,flim=flim,scale=TRUE,listen=TRUE)

thresh <- -6
M2 <- s$amp
M2[s$amp < thresh] <- 0
M2[s$amp >= thresh] <- 1

img<-Image(t(M2))
#display(img)

kernel<-t(rbind(
  c(0,0,0,0,0),
  c(0,0,0,0,0),
  c(0,1,1,1,0),
  c(0,0,0,0,0),
  c(0,0,0,0,0)
))

seg<-erode(img, kernel)
#display(seg)


scaled.freq<-s$freq*1000
notes <-read.csv("~/Documents/Ant/Freq.csv",header=T)
labels<-as.character(seq(1, length(s$freq)))
note.pointer<-1
for(i in 1:length(s$freq)) {
  if(note.pointer>nrow(notes)) break;
  while(note.pointer<nrow(notes) && notes[note.pointer,2]<scaled.freq[i]){
    note.pointer<-note.pointer+1
  }
  if(note.pointer>1 && notes[note.pointer,2]>=scaled.freq[i]){
    labels[i]<-as.character(notes[note.pointer-1,1])
  }
}
labels<-make.unique(labels)
note.data<-data.frame(t(imageData(seg)))
row.names(note.data)<-labels

final<-which(note.data>0,arr.ind=TRUE)
final