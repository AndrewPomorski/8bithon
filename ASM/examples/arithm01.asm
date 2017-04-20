set	v0, 0x20 		// Set the first register  to 32
set 	v1, 0x40		// Set the second register to 64
draw	v0, v1   		// Draw a pixel at position X:v0, Y:v1
rand	v2, 0xF  		// Store a random number in registry v2
set	v3, 0xA 		// Set v3 to 10
set	v4, 0x8  		// Set v4 to 8
mov	v4, v3	 		// Move value from v4 to v3 (Erases v4)
set 	v5, 0xF			
timr	v5			// Sets timer to value of v5, and starts counting down 60Mhz
skip	v5, 0xF			// Skips next instruction if v5 equals to 15 (True)
jmp	0x200	 		// Jump to memory location 512 (first instruction)
