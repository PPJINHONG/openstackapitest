# openstackapitest

# import csv
# import schedule
# import time
import os

# from datetime import datetime, timedelta
# from schedule import every, repeat, run_pending, clear
# from kafka import KafkaProducer
from novaclient import client

# def producer():
#         current_date = datetime.now().strftime("%Y%m%d")

#         bootstrap_servers_cn_kafka = '10.109.172.116:9092'
#         producer_cn_kafka = KafkaProducer(bootstrap_servers=bootstrap_servers_cn_kafka)

#         file_path = '/root/kbj/vm/csv/vm_cn_1_new-stg_{}.csv'.format(current_date)
#         #file_path = 'test.csv'

#         with open(file_path, 'rb') as file:
#                 content = file.read()

#         producer_cn_kafka.send('CN_VM_1_NEW-STG', value=content)
#         producer_cn_kafka.flush()
#         producer_cn_kafka.close()


def nova_extract():
        #current_date = datetime.now().strftime("%Y%m%d")

        auth = {
                'auth_url':'http://10.107.147.31:35357/v3',
                'project_name':'admin',
                #'tenant_name':'eutmsprd',
                'username':'spark',
                'password':'TldhTl1!',
                'user_domain_name':'Default',
                'project_domain_name':'Default'
        }

        nova = client.Client('2.1', **auth)

        vms = nova.servers.list(search_opts={'all_tenants': 1})
        hypervisors = nova.hypervisors.list()

        print(vms)

        # csv_file_path = '/root/kbj/vm/csv/vm_cn_1_new-stg_{}.csv'.format(current_date)
        # csv_header = ["id", "name", "status", "flavor", "address", "availability_zone", "hostname", "created_at", "updated_at"]

        # with open(csv_file_path, mode='w') as csv_file:
        #         writer = csv.writer(csv_file)
        #         writer.writerow(csv_header)

        #         for vm in vms:
        #                 addresses_info = ""
        #                 for key, values in vm.addresses.items():
        #                         for addr_info in values:
        #                                 address = addr_info['addr']
        #                                 addresses_info += f'{key}:{address}\n'
        #                 addresses_info = addresses_info.strip()

        #                 flavor_id = vm.flavor['id']
        #                 flavor = nova.flavors.get(flavor_id)

        #                 vm_data = [vm.id, vm.name, vm.status, flavor.name, addresses_info, vm._info['OS-EXT-AZ:availability_zone'], vm._info['OS-EXT-SRV-ATTR:host'], vm.cr                                   eated, vm.updated]
        #                 writer.writerow(vm_data)

# def cleanup():
# #       schedule.run_pending()
#        time.sleep(1)

#        current_date = datetime.now().strftime("%Y%m%d")
#        retention_period = 3

#        delete_date = (datetime.now() - timedelta(days=retention_period)).strftime("%Y%m%d")

#        host_dir = '/root/kbj/vm/csv'
#        file_list = os.listdir(host_dir)

#        for file_name in file_list:
#                if file_name.startswith('vm_cn_1_new-stg_') and file_name <= f'vm_cn_1_new-stg_{delete_date}.csv':
#                        file_path = os.path.join(host_dir, file_name)
#                        os.remove(file_path)
#                        print("file remove success!")


#every().day.at("01:25").do(nova_extract)
#every().day.at("01:28").do(producer)

# cleanup()
nova_extract()
#time.sleep(30)
# producer()

