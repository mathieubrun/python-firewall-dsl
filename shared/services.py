
from models.service import Service

ftp = Service(
    port = 21, 
    name = "ftp"
)

ssh = Service(22, "ssh")