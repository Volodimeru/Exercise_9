file_name = input("File name: ")
if ".jpg" in file_name:
    print("image/jpg")
elif ".gif" in file_name:
    print("image/gif")
elif ".gpeg" in file_name:
    print("image/gpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name:
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name:
    print("application/zip")
else:
    print("application/octet-stream")