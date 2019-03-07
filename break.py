def callTheBreak(k,m):
  m0 = m
  k0 = k
  a = 1  
  ret = []
  a0 = 0
  while k>0:
    if(len(ret) % 2 == 0):
      ret += [(a,k)]
    else:
      ret += [(a,-k)]
    a0,a = a,a*(m//k) + a0
    k,m = m % k,k
  ret += [(a,0)]
  return ret
 
## [a,b]
def pehla(a,b,breaks,mm):
#  print(a,b)
  ret = 0  
  v = 0
  if a <= 0 and b >= 0:
    return 0
  if a<0:
    a += mm
    b += mm
  for c,k in breaks:
    if k>0 and v<a:
      n = (1+(a-v-1)//k)
      v += k*n
      ret += c*n
      if v >= a and v <= b:
        return ret
    elif k<0 and v > b:
      n = (1+(v-b-1)//(-k))
      v += k*n
      ret += c*n
      if v >= a and v <= b:
        return ret
  
 
def deepcall(a,b,m,n):
  if(n==1):
    return 0
  breaks = callTheBreak(b,m)
  target = (a+b*(n%m)) % m
  mn,mx = 0,m-1
  v = (a + b) % m
  if v <= target:
    mn = v
  else:
    mx = v-1
  ret = 0
  n -= 1
  while True:
#    print("--",target,v,mn,mx,ret,n)
    if mn == v:
      r0 = pehla(1,mx-v,breaks,m)
      if r0 is None:
        break
      dv = b*r0 % m
      k = (target-v)//dv
      v = v + dv*k
      n -= r0*k
      ret += k
      mn = v
#      print(r0,k,dv)
      if n == 0:
        break
      if v + dv <= mx:
        v += dv
        n -= r0
        ret += 1
        mx = v-1
    else:
      r0 = pehla(mn-v,-1,breaks,m)
      if r0 is None:
        break
      dv = m - (b*r0 % m)
      k = (v-target-1)//dv
      v = v - dv*k
      n -= r0*k
      ret += k
      mx = v -1
#      print(r0,k,dv)
      if n == 0:
        break
      if v - dv >= mn:
        v -= dv
        n -= r0
        ret += 1
        mn = v
    if mn == mx and v == target:
      break
#  print("rr",ret,v,n)
  ret += n//breaks[-1][0]
  return ret
 
 
import sys
F = sys.stdin
 
#F = open("input.txt")
 
def calltheints():
  return map(int,F.readline().split())
 
n = int(F.readline())
pts = []
for i in range(n):
  print(deepcall(*calltheints())) 
