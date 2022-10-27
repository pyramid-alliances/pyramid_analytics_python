import os
import json
from pathlib import Path


import pyramid_api as pa
from uuid import uuid4

test_settings_path = Path(os.environ.get("PA_TEST_SETTINGS", ""))
if test_settings_path.exists():
    print(f"loading {test_settings_path}")
    settings = json.load(open(test_settings_path,"r"))
    print (settings)

pa.setup_logging()

session = pa.login(
    domain=settings["pyramid_server_url"], 
    username=settings["pyramid_server_admin_user"], 
    password=settings["pyramid_server_admin_password"]
)

me = pa.access.getMe()

print(me)
users = pa.access.getUsersByName(me.userName)
print(users)
users = pa.access.getUsersByRole(me.userName)
print(users)
roleid = str(uuid4())
rd = pa.objects.RoleData(roleId=str(roleid), roleName="somerole", tenantId=me.tenantId)

res_create = pa.access.createRole(rd)
print(pa.access.getRolesByName(searchCriteria=pa.objects.SearchCriteria(searchValue="somerole*")))


created_roles = [r for r in pa.access.getAllRoles() if "somerole" in r.name]
for r in created_roles:
    pa.access.deleteRole(r.id)


schedules = pa.tasks.findSchedule(pa.objects.ScheduleSearchCriteria())


folderTenantObject=pa.objects.FolderTenantObject(
    tenantId=me.tenantId, 
    validRootFolderType=ValidRootFolderType.public
    )