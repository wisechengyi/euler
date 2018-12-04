####################################################################
# File   : Makefile - automates building of the project.             #
# Author : Tim Sally                                                 #
######################################################################

CXX        = g++
CXX_FLAGS  = -g -ansi -Wall 


# - Files 
SRCS       = $(shell list=`/bin/ls . | grep -e "\.cpp"`; \
                          for i in $$list; do echo $$i; done)
OBJS       = $(SRCS:.cxx=.o)
TARGETS    = smfgen

.PHONY: $(TARGETS)

# --- Suffix Rules 

.SUFFIXES: 
.SUFFIXES: .cxx .o

.cxx.o:
	$(CXX) -c $(CXX_FLAGS) $< 

# --- Targets
all: $(TARGETS)

smfgen: $(OBJS)
	$(CXX) -o $@ $^ $(LD_FLAGS)
clean:
	rm -f smfgen
	rm -f *.vtk
