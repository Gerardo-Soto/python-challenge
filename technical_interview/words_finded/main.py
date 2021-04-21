"""

"""

info = "In November 2018 Amazon announced EC2 A1 instances powered by AWS Graviton Processors that feature 64-bit Arm Neoverse cores and custom silicon designed by AWS.  A1 EC2 instances are cost and performance optimized for scale-out workloads and offer up to 45% cost savings relative to other EC2 instances.  With this Docker Desktop tech preview, Docker is making it easier than ever to develop containers on, and for Arm servers and devices.  Using the standard Docker tooling and processes you are already familiar with you can start to build, push, pull, and run images seamlessly on different compute architectures.  No changes to Dockerfiles or source code are needed to start building for Arm. Simply rebuild your image using the new features being released today.  Finally, Docker is quickly expanding into Edge and IoT, and we see this as an important step in that process.  Docker has always been about developers, and making things easy.  That is at the heart of why we did this."

info2= "Hola, hola mundo. Soy Gerard, si, hola hol bye bye see you later"

words_found = dict()


info_list = info2.replace(",","").replace(".","").replace("  "," ").upper().split(" ")

for word in info_list:
    if word in words_found:
        words_found[word] += 1
    else:
        words_found.update({word : 1})


print(words_found)
