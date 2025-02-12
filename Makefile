.PHONY: all
all: hw.so

hw.so: hw.c
	${CC} -shared -o hw.so ${LDFLAGS} ${LDLIBS} hw.c

.PHONY: clean
clean:
	rm -f main.so
