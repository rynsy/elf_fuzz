all:
	gcc gate.c -o gate

clean:
	rm gate gate_fuzz tmp/*
	
