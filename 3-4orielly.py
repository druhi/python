guest = ["aunt","uncle","sister"]
print(f"dear{guest[0]} you are invited for our birthday")
print(f"dear{guest[1]} you are invited for our birthday")
print(f"dear{guest[2]} you are invited for our birthday")
print("sister has imfomed she is not attending")
guest.remove(guest[2])
guest.append("niece")
print(f"dear{guest[0]} you are invited for our birthday")
print(f"dear{guest[1]} you are invited for our birthday")
print(f"dear{guest[2]} you are invited for our birthday")
# guest list