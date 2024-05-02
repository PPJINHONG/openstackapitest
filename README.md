nova api 오브젝트 조회

nova = client.Client('2.1', **auth)
print(dir(nova))
//출력값 servers,hypervisors 등등


그 하위 단계 조회 
print(dir(nova.servers))
//출력값 list,tag_list 등등 


api 데이터 속성값 조회

attr = nova.servers.list(search_opts={'all_tenants': 1})
print(dir(attr[0]))
//출력값 tenant_id,name,topology 등등

위에 값으로 데이터 출력한다.

for a in attr:
  print(a.tenant_id, a.name)
