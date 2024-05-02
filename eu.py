
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

        # for b in vms2:
        #         print(  b[])
        #         print('\n')
        
    


nova_extract()


