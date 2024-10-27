# linear search function
def linsearch(arr):
  val20 = ["Indicies for 20:"]
  val25 = ["Indicies for 25:"]
  val60 = ["Indicies for 60:"]
  val74 = ["Indicies for 74:"]
  val97 = ["Indicies for 97:"]
  for n in range(len(arr)):
    if arr[n] == 20:
      val20.append(n)
    if arr[n] == 25:
      val25.append(n)
    if arr[n] == 60:
      val60.append(n)
    if arr[n] == 74:
      val74.append(n)
    if arr[n] == 97:
      val97.append(n)
  print("\n".join(map(str, val20)), "\n")
  print("\n".join(map(str, val25)), "\n")
  print("\n".join(map(str, val60)), "\n")
  print("\n".join(map(str, val74)), "\n")
  print("\n".join(map(str, val97)), "\n") 
  print(" ")
  return (arr)
  
# your main code here
myArr = [20, 20, 24, 27, 39, 40, 43, 46, 50, 
         60, 60, 62, 71, 74, 76, 86, 86, 87, 97, 97]

print(linsearch(myArr))
