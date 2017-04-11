def check_free_bytes(registry):
	TAKEN_ADD = 0
	for addr in registry:
		if not addr == 0:
			TAKEN_ADD += 1
	free_bytes = len(MEMCAP) - TAKEN_ADD
	return free_bytes

