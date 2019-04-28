def readPropertiesFile():
    configDict = dict(line.strip().split('=') for line in open('config.properties'))
    # print(H["application.name"])
    for key in configDict:
        print(key + "<---------->" + configDict[key])
    print("Operating System Name : ", configDict["os.name"])


if __name__ == "__main__":
    readPropertiesFile()
