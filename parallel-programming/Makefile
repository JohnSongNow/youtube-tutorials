CC = gcc
CFLAGS += -std=gnu11 -Wall -Werror -g3 -DNDEBUG 
EXTRA_CFLAGS += -O3 -fopenmp
LDFLAGS += -lm -fopenmp 

all: avg-run-test avg-run-test-parallel

avg-run-test: avg-run-test.o
	$(CC) $^ -o $@ $(LDFLAGS)

avg-run-test-parallel: avg-run-test-parallel.o
	$(CC) $^ -o $@ $(LDFLAGS) $(EXTRA_CFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o avg-run-test avg-run-test-parallel