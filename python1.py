#coding=utf-8 
#coding=gbk 
#����������ѡһ��������
message="   hello python world!    "
print(message.strip())          #to delete space before and after the string
print(message.title())
print(message.upper())
print(message.lower())
go=['g','o','g','o','l']
print(go)
#use last element in list
print(go[-1])
#list add element at end
go.append('is')
print(go)
#insert element in a list
go.insert(1,'haha')
print(go)
#use del to delete a element in a list
del go[1]
print(go)
#pop�����б�Ԫ��
test1=go.pop()
print(test1)
test2=go.pop(1)
print(test2)
#�˷���û�з���ֵ�����ܸ�������ֵ���˷���ֻɾ����һ��ָ����ֵ
go.remove('g')
print(go)

