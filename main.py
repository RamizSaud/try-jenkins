import sys
from db import Database

print("Creating Incidents....")
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# with open("output.txt", "w") as f:
#     f.writelines(lines)

if len(sys.argv) > 1:
    text = sys.argv[1]
    print("Argument received:", text)
else:
    print("No argument received")

db = Database(
    host="192.168.100.120",
    port=5232,
    dbname="sdp",
    user="admin",
    password="thales*"
)

print("Connection Established with Database")

incidents = db.fetch_all("SELECT * FROM incident WHERE id=%s", ('0df2fd20-0c75-4cf3-9243-0d97d0576f09',))

print(incidents)

db.close()
print("Incidents Created")