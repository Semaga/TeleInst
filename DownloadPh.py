
import os
from urllib.request import urlretrieve
import matplotlib.pyplot as plt 
from instagram import Account, Media, WebAgent, AsyncWebAgent

def download_Photo(number, url):
    """
    
    """
    # url = url 
    number = number
    destination = str(number)+".png"
    urlretrieve(url, destination)


def write_comment_file(medias, account):
    """
    Make comment's file 
    Function take list of medias as first argument and account as second
    Consist of name, Surname of users and their BIO 
    """
    print("Type of medias is {}".format(type(medias)))

    with open('text.txt','w') as write:
        print("\t*Open writefile")
        write.write("username  - {}\nfull-name - {}\nBio:\n\n".format(account.username, account.full_name, account.biography))
        for i, media in enumerate(medias):
            if not media.is_video:
                write.write("{}\n{}\n\n".format(i, media.caption))


def DoIt(name):
    """
    Download function
    Function takes loggin of accaunt's user
    """

    dir_home = os.getcwd()

    print("Start work with {}".format(name))
    try:
        print("\tExcess with open ")
        agent = WebAgent()
        account = Account(name)
        if account.is_private:
            print("\tAccount {} is private".format(account))
            return 0
        else:
            print("\tAccount {} is not private".format(account))
            agent.update(account)
            agent.get_media(account)
            medias, point = agent.get_media(account, count = account.media_count)
            try:
                os.mkdir("_{}".format(name))
                print("\t##Make _{} directory".format(name))
                os.chdir("_{}".format(name))
                print("\t##Into _{} directory".format(name))            
            except:
                os.chdir("_{}".format(name))
                print("\t##Into _{} directory".format(name))
                
            #ебануть проверку    
            for i, media in enumerate(medias):
                if not media.is_video:
                    download_Photo(i, media.display_url)

            write_comment_file(medias, account)

    except:
        print("Haven't excess with open - {}".format(name))
        pass

    os.chdir(dir_home)
    print("\t##Go to {}".format(dir_home))    


def ReadNamesFromFile(FileName):
    """
    Return list consist of loggins of users
    Input - name of file with loggins
    return - list with loggins 
    """

    a = []
    b = ""
    with open(FileName, "r") as read:
        for i, line in enumerate(read):
            b = ""
            for j in line:
                if (j != ','):
                    b+=j
                else:
                    break
            a.append(b)
    return a



names = ["al.semakin", 
         "zuck", 
         "travel__my_soul",
         "v_adikk",
         "kaiskhakova",
         "almaz_nasybullin",
         "_quitehour_",
         "annmorozko",
         "niyazeoh",
         "airatphd",
         "pilebokafilm"]

names1 = ["al.semakin", 
         "zuck"]


def main():
    """
    Main function
    """
    for name in names1:
        DoIt(name)


if __name__ == "__main__":
    main()