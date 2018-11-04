CC = g++
DEPS = solve.cpp
PY = python3
PDEPS = scrap.py

all: $(CDEPS) $(PDEPS)
	$(CC) -shared -Wl,-soname,libc.o -o libc.so -fPIC $(CDEPS)
	$(PY) $(PDEPS)

clean:
	rm *.so