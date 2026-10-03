
#main function
def main():

    filename = str(input("File name: ")).strip().lower()
    
    wext(filename)
    

def wext(it):
    if it.endswith(".jpg"):
        print("image/jpg")
    elif it.endswith(".gif"):
        print("image/gif")
    elif it.endswith(".jpeg"):
        print("image/jpeg")
    elif it.endswith(".png"):
        print("image/png")
    elif it.endswith(".pdf"):
        print("application/pdf")
    elif it.endswith(".txt"):
        print("txt/plain")
    elif it.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()