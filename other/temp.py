def solution(time, gold, upgrade):
    upgrade_r = []
    for i in range(len(upgrade)):
        #print(i, "-----------")
        r = 0
        time_ = time

        cu, cd = upgrade[0][0], upgrade[0][1]
        u = None
        for u in range(1,i+1):
            if r >= upgrade[u][0]:
                r -= upgrade[u][0]
                cu, cd = upgrade[u][0], upgrade[u][1]
            elif (time_//cd)*gold >= upgrade[u][0]:
                t = ((upgrade[u][0]//gold)+1)*cd
                g = ((upgrade[u][0]//gold)+1)*gold
                
                r += (g - upgrade[u][0])
                time_ -= t
                #print(time, time_, r)
                cu, cd = upgrade[u][0], upgrade[u][1]
            else:
                break
        
        r+= (time_//cd)*gold
        upgrade_r.append((r, -i))
        #print("\n=====================\n")
    #rint(upgrade_r)
    upgrade_r.sort(reverse = True)
    return upgrade_r[0][0]

print(solution(100, 200, [[0, 5], [1500, 3], [3000, 1]]	))