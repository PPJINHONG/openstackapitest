
from datetime import datetime, timedelta
from novaclient import client



def nova_extract():
  

        auth = {
                'auth_url':'http://10.109.130.161:35357/v3',
                'project_name':'admin',
                #'tenant_name':'eutmsprd',
                'username':'spark',
                'password':'tmvkzm1!',
                'user_domain_name':'Default',
                'project_domain_name':'Default'
        }

        nova = client.Client('2.1', **auth)
        vms2 = nova.servers.list(search_opts={'all_tenants': 1})
        vms4 = nova.availability_zones.list(detailed=True) 


        vms3 = nova.hypervisors.list()
        
        for a in vms3:
                print(a.id, a.hypervisor_hostname ,a.status)
        # print(vms2[1])






import json

# nova.availability_zone.list(detailed=True)를 호출하여 데이터 가져오기
availability_zones = nova.availability_zone.list(detailed=True)

# 결과를 저장할 리스트
availability_zone_info = []

# 각 availability zone의 정보를 순회하며 변환
for zone in availability_zones:
    zone_info = {
        "zoneName": zone.zoneName,
        "zoneState": {
            "available": zone.zoneState.available
        },
        "hosts": {}
    }
    for host, services in zone.hosts.items():
        for service, status in services.items():
            service_info = {
                service: {
                    "active": status.active,
                    "available": status.available,
                    "updated_at": status.updated_at
                }
            }
            zone_info["hosts"][host] = service_info

    availability_zone_info.append(zone_info)

# JSON 형식으로 출력
json_data = json.dumps(availability_zone_info, indent=4)
print(json_data)


        # for b in vms2:
        #         print(  b[])
        #         print('\n')
        
    


nova_extract()


