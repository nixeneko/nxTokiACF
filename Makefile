
TTXCMD = /cygdrive/c/softs/FDK/Tools/win/ttx.cmd
PYTHONCMD = python
TARGETFONTBASENAME = nxTokiACF

OUTPUTFONTFILE = output/$(TARGETFONTBASENAME).ttf
TEMPTTXFILE = temp/$(TARGETFONTBASENAME).ttx
TTXFILE = $(TARGETFONTBASENAME).ttx

all: $(TEMPTTXFILE)
	$(TTXCMD) -o $(OUTPUTFONTFILE) $(TEMPTTXFILE)

$(TEMPTTXFILE): $(TTXFILE)
	$(PYTHONCMD) replacetobinary.py $(TTXFILE) $(TEMPTTXFILE)
