# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 프로그래머스 : 호텔 방 배정 (https://programmers.co.kr/learn/courses/30/lessons/64063)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def solution(k, room_number):
    result=[]
    node_list={}
    
    for i in room_number:
        if len(result)==0:
            result.append(i)
            temp=Node(i)
            temp.next=0
            node_list[i]=temp
            continue
        
        if i not in node_list:
            result.append(i)
            temp=Node(i)
            temp.next=0
            node_list[i]=temp
            
            if i-1 in node_list:          
                node_list[i-1].next=temp
            if i+1 in node_list:
                temp.next=node_list[i+1]
        else:
            temp_list=[]
            temp_target=node_list[i]
            temp_list.append(temp_target)
            while 1:
                if temp_target.next==0:
                    index=temp_target.data+1
                    result.append(index)
                    temp=Node(index)
                    temp.next=0
                    node_list[index]=temp
                    
                    if index+1 in node_list:
                        temp.next=node_list[index+1]
                    
                    for j in temp_list:
                        j.next=temp                        
                        
                    break
                temp_target=temp_target.next
                temp_list.append(temp_target)
    
    return result
