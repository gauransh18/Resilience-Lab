#!/bin/bash

# Randomly kill a container
#!/bin/bash

# Randomly kill a container
docker run -d --rm --name pumba gaiaadm/pumba pumba --interval 10s --random --log-level info kill --signal SIGKILL user_service