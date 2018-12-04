####################################################################
# File   : Makefile - automates building of the project.             #
# Author : Tim Sally                                                 #
######################################################################

CXX        = g++
CXX_FLAGS  = -std=c++11 -O2 -Wall -Wunused-variable  -fopenmp  


# - Files 
SRCS       = $(shell list=`/bin/ls . | grep -e "\.cpp"`; \
                          for i in $$list; do echo $$i; done)
OBJS       = $(SRCS:.cxx=.o)
TARGETS    = psr

.PHONY: $(TARGETS)

# --- Suffix Rules 

.SUFFIXES: 
.SUFFIXES: .cxx .o

.cxx.o:
	$(CXX) -c $(CXX_FLAGS) $< 

# --- Targets
all: $(TARGETS)

psr: $(OBJS)
	$(CXX) -o $@ $^ $(LD_FLAGS)
clean:
	rm -f psr
	rm -f *.vtk
