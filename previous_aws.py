#!/usr/bin/python3
import getpass
import subprocess
import os
import pip


boto_check = 0
USER = getpass.getuser()
while True:
    os.system("clear")
    print('''\033[91m		             .
		     -`     +`
		      /-   ++  -:`              \033[92mWelcome user\033[37m @\033[36m''', USER, '''\033[91m
		       :o. ys o:``
		      `.-ssoN+d +` -+`
		  `/shhyysyhNMMsd+:y`           \033[92m Select your choice:\033[91m
		 `+oso+/:.+y:NMMMNNy            \033[94m 1. \033[93mBasic Linux\033[91m
	      -/sdNNdsoss+--+sdMMmsd+           \033[94m 2. \033[93mYum\033[91m
	   .+yydNMNy++m+`   ./+NMhymNh:`        \033[94m 3. \033[93mDocker\033[91m
	   -..yNMmys. -   `-:y:sNs+:ydNy`       \033[94m 4. \033[93mHadoop\033[91m
	    .dNMMsMmo:  `ddoshhmN/-o``s.        \033[94m 5. \033[93mAmazon\033[91m
	    yyyMM/NmMs  yMNd/-:-..``/-.`        \033[94m 6. \033[93mExit\033[91m
	    o`sMMy/yhNy:hyh:s:       `-`
	    ` +MhMh/:/hNh..+`o         .`
	      .d.yMNho//:..- :
	       ::yoh+mNmdys+/:--..``
	       `hMh/:.+dNNhdNMNy//:/::.`
	       .yMMm.`.-/yh+::+ooo/:/oydho-`
	       .yMM/-o/:--...`     `.-+/hNh/-
		-dMsNh+:-.`           :h+sMm:
		 `omNNs/:-`           `ym+mMN+
		  `--:.```.`          .+ddyM+y/
	      `/+o+/+:..`           `:sdNyhM/`+`
	    .ohdyosydMdmh//:``--`.//+hmNh/MM-
	   /mh/` `.:+syhdmdmmy/ymsoMNdho/NMy
	  -Ns`       `-+ydmNNNNdNNmdhhyyoMy`
	  sM-             ``.--:ymmmho-`o+`
	  .Ms`             `-:/+/:.`  `-`
	   yMh/`       `..           `-:
	   `hMMNs+///:::.````   `:+::+/.
	     oNmmNmdhyso+/:.`   :/+/-`
	      -s/-+hNdysyssssoo+/-`
		./:.`:oo/-`
		   `-.`  .--.``
	\033[0m''')
    a = input("Enter your choice : ")
    # ---------------------------------docker---------------------------------------------

    if int(a) == 1:
        while True:
            os.system("clear")
            print(''' \033[97m
                                      ```
                              `-/oyhdmNNNNmmhys+/-`
                        -+syhmNMMMMMMMMMMMMMNmmmMMNmy+-`
                    `:smNMMMMMMMNm\033[31mdddd\033[97mmNmm\033[31mdhhddhy\033[97mmMMMMMms:
                  -smMMMMMMMMMMm\033[31myyyyyyyyyyyyyhNmyy\033[97mNMMMMMMMd+`
               `:hNMMMMMMMMMMMM\033[31mymdhhhyyyyyyyyhyyyyh\033[97mMMMMMMMMMm/
              :dMMMMMMMMMMMMMMN\033[31myhdmhhyyyyyyyyyyyyyyd\033[97mMMMMMMMMMNh.
            -hNMMMMMMMMMMMMMMM\033[31mdyyyyyyyyyyyyyyyyyyyyy\033[97mNMMMMMMMMMMm:
           /mMMMMMMNmdddddmmmmh\033[31myyyyyyyyyyyyyyyyyyyyy\033[97mmMMMMMMMMMMMm:
          /NMMMMMMm\033[31myyyyyyyyyyy\033[97mmm\033[31mhhhhhhhyyyyyyyyyyyyy\033[97mdMNmmmNNMMMMMm-
         .mMMMMMMM\033[31myyyyyyyyyyyy\033[97mdNMMMMMMMNNh\033[31myyyyyyyyyyNNyyyyyhhm\033[97mNMMMd.
         hMMMMMMMM\033[31mhyyyyyyyyyyyy\033[97mhhdmNNNMMMNh\033[31myyyyyyyyhhyyyyyyyyyhd\033[97mMMMo
        /MMMMMMMMMM\033[31mdyyyyyyyyyyyyyyyyy\033[97mhhhhh\033[31myyyyyyyyyyyyyyyyyyyyyy\033[97mdMMm`
        dMMMMMMMMMMMmh\033[31myyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\033[97mhMMM/
        NMMMMMMMMMMMMMNdh\033[31myyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\033[97mdMMMh
       -NMMMMMMMMMMMMMNssddh\033[31myyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\033[97mhNMMMN.
       /MMMMMMMMMMMMMM/  :NMNmhhh\033[31myyyyyyyyyyyyyyyyyyyyyyyyyyyy\033[97mhmMMMMMM/
       :MMMMMMMMMMMMMd    -oyMMMNNNmm\033[31mdddhhhyyyyyyyyyyyyyyh\033[97mhdmMMMMMMMM+
       -MMMMMMMMMMMMMm`     `+mMMMMMMMMMMNmmNNNmmmmddhmmmNNMMMMMMMMMMo
       `NMMMMMMMMMMMMMs`      ./shddddhs+:--/os//os+-/NMMMMMMMMMMMMMM/
        hMMMMMMMMMMMMMM+          ````    ``   `     /MMMMMMMMMMMMMMN:
        .mMMMMMMMMMMMMMNh/`             `+yso+oy`    .NMMMMMMMMMMMMMm`
         -mMMMMNmy++smNMNm-              -..:++:     +MMMMMMMMMMMMMMs
          -dNds:`    .:/:.                          .NMMMMMMNNmmmmNm.
           `.`                                     `dMMMMMNh--....--
                                                  `yMMMdo:-`
                                                `/hMMd/`
                                                omdy/`
                                    //:   ++     `               ..
                                    NMd   Nm                    .Ns
          -++.+s+` ./oso/.    .+ss+.NMd   Nm:osss:   `:ossss/` -sMdo-
          +MMmhys sNNsoyMN/  oNMhoodMMd   NMs:.-yM/  sN/..-+Ms `/My-`
          +MMo   :MMh///dMN`.MMh   `MMd   NN    .Ms  `-:/+osMd  -Ms
          +MM:   /MMh+++ooo`.MMy   `NMd   Nm    .My `hNo/:--Md  -Ms
          +MM:   `hMNo/+  ,  sMMy/+dMMd   Nm    .My -Md.``-yMd  .Mh-`
          :ss.     :oyhyo:    -oyys:+so   oo    `s/  -oyys+-+s`  /sy:
		   	\033[92m Select your choice:\033[91m
			\033[92m---------------------\033[91m
	\033[94m 1. \033[93mStart a Process\033[91m                      \033[94m 6. \033[93mTo delete file \033[91m
	\033[94m 2. \033[93mStop a Process\033[91m                       \033[94m 7. \033[93mTo copy file\033[91m
	\033[94m 3. \033[93mStatus of Process\033[91m                    \033[94m 8. \033[93mMove file\033[91m
	\033[94m 4. \033[93mTo Know Which Directory\033[91m              \033[94m 9. \033[93mTo make file executable\033[91m
	\033[94m 5. \033[93mShow files in directory\033[94m              \033[94m 10. \033[93mExit\033[91m
	\033[0m''')
            b = input("Enter your choice : ")
            if int(b) == 1:
                app = input(
                    "Please Enter the name : ")
                os.system('systemctl start %s' % (app))
                print("Press enter to continue !")
                input()
            elif int(b) == 2:
                app = input(
                    "Please Enter the name : ")
                os.system('systemctl stop %s' % (app))
                print("Press enter to continue !")
                input()
            elif int(b) == 3:
                app = input(
                    "Please Enter the name : ")
                os.system('systemctl status %s' % (app))
                print("Press enter to continue !")
                input()
            elif int(b) == 4:
                os.system('pwd')
                print("Press enter to continue !")
                input()
            elif int(b) == 5:
                os.system('ls')
                print("Press enter to continue !")
                input()
            elif int(b) == 6:
                file_name = input("Enter the name of file to delete : ")
                os.system('rm -f %s' % (file_name))
                print("Press enter to continue !")
                input()
            elif int(b) == 7:
                file_name = input("Enter the name of file to copy : ")
                os.system('cp %s' % (file_name))
                print("Press enter to continue !")
                input()
            elif int(b) == 8:
                file_name = input("Enter the name of file to move : ")
                path = input("Give the path where you have to move the file")
                os.system('mv %s %s' % (file_name, path))
                print("Press enter to continue !")
                input()
            elif int(b) == 9:
                file_name = input(
                    "Enter the name of file to make executable : ")
                os.system('chmod +x %s' % (file_name))
                print("Press enter to continue !")
                input()
            elif int(b) == 10:
                print("Press Enter to Main Menu !")
                input()
                os.system("clear")
                break
            else:
                print("Invalid Option")
                input()


    # -----------------------------yum---------------------------------------------
    elif int(a) == 2:
        while True:
            os.system("clear")
            print(''' \033[94m
                   `.-/ym       `-.
             `..--::----d.    ./:/o/:-`
 ./:-...--:::---os/:::::/h:..o:://+oo--::::/:`
 .o+:------ohoosN:       ```````  `do-------:/+++-
    .::----:d  `y.              ```h:.---------:y-
      -s:..-y: `+             `````d-...------:/`
       +Mo///o``+          ````````m+/-...---.
     .-:/hs--h.`h`      ``````````.m/-+s+/s`
 `--:----.:+/ho.ys    `````````.-:-hs:::/oy`     `---     ---`.--.   `--- `... `...   ...`
:m/--------...:-/h//:..-...-----..........-:-`   `oyy:   :yyo +yyo   -yyy .///://///-/:///:`
  -/+/-------.......oMm```.............------::--``syy. .yys` +yyo   :yyy .///.  :///`  ///-
     -+o:-----......-Mm+............------:----/+- .yys`oyy-  +yyo   :yyy .///   -//:   ://-
       /oso:----....+M:N........---/+++/o-          -yysyy/   /yys-`-syyy .///   -//:   ://-
       -/--///+o/-..hm`sh-..-:::/++:----/.           :yyyo    `+yyyyo+yyy .///   -//:   ://-
       :o----..-+yhsNd.-ho/:-....-------/-           .yys.
       ho------....:+s..........--------/:         syyy+``---..--...-: .:..--.-- ..-..-.--..
      `my:------....os.......-----------ss         ```
        `:/+:-----..hh.....---------:///o:
           `+so:----dh...----:/+/::-.
              `-:/+sds:---::--.
	\033[92m Select your choice:\033[91m
	\033[92m---------------------\033[91m
	\033[94m 1. \033[93mYum Configuration\033[91m
	\033[94m 2. \033[93mInstall Application\033[91m
	\033[94m 3. \033[93mRemove Application\033[91m
	\033[94m 4. \033[93mExit\033[91m
	\033[0m''')
            b = input("Enter your choice : ")
            if int(b) == 1:
                os.system('''
                ansible slave -m yum_repository -a '' -b
                ''')
                input()
            elif int(b) == 2:
                app = input("Enter the name of App : ")
                os.system('yum install %s' % (app))
                print("Press enter to continue !")
                input()
            elif int(b) == 3:
                app = input("Enter the name of App : ")
                os.system('yum remove %s' % (app))
                print("Press enter to continue !")
                input()
            elif int(b) == 4:
                print("Press Enter to Main Menu !")
                input()
                os.system("clear")
                break
            else:
                print("Invalid Option")
                input()


    # ---------------------------------docker---------------------------------------------

    elif int(a) == 3:
        while True:
            os.system("clear")
            print(''' \033[96m
                                       /yssssssy.
                                       /y++++++h.
                                       /y++++++h.
                         .-------------+yooooood-                  `
                        `yysssssyysssssshssssssd.                `/so-`
                        `hsoooooys+++++ohooooood.                /yooyo.
                        `hsoooooys+++++ohooooood.               `ys+++sy.
                 .///////hysssssyyoooooshssssssh+//////-        `ho++++ss..---..`
                 -hsssssshsoooooyysssssshoooooohssssssh/        `ss++++ohsyyssyss+`
                 -hooooooho+++++syooooosy++++++hooooooh/         -yoo++oooooooosy+`
                 -hsoooooho+++++syooooosy++++++hooooooh+     ```.:syooooooosssso-
           :oooooshyyyyyyhysssssyyyyyyyyysssssshyyyyyyhsoooooossssooooyssso+/:.
      `    oyooo++++++++++++++++o+++++++++++++++o++++++++++++++++ooooys`
     `o/.``oyooooosso+++++++++++ooyyoo++++++o+osysoo++++++++++ooysssys` ```-o:`
 ``-/ossso+shyyyyhhhhyyyssssyyyyhhhhhyyyssssyyyhhhhhyyysssssyyhhhhhhy+///+osss+:.`
           `hyyyssssssssssssssssssssssssssssssssssssssssssssyyyyyyh+
            +hyyysssssssssssss O ossssssssssssssssssssssyyyyyyyyyy-
            `ohyyyssssssssssss/ys/ssssssssssssssssssssyyyyyyyyyh/`
             `+hyyyyysssyyyyyysoossssssssssssssssssyyyyyyyyyyy+`
               :ys+++++//:-..+sssssssssssssssyyyyyyyyyyyyyhs:`
                `/s+:-------.-/sssssssyyyyyyyyyyyyyyyyyys/.`
                  `-+o+/--------+syyyyyyyyyyyyyyyyyys+:.
                     `./+oo++//:::/oyyyyyyyyyyso+/-``
                         ``.-:://///++//::-.```
            ``                    \033[34m             `
             -yy`                               sy:
             :dd`                               dd/
    `-/+oo+:.:dd`   `-/+oo+/-`      `-/+oo+/-   dd/  ./+.   `.:+ooo/:.       .:/++-
  `+yhyoooshhydd` `/yhysoosyhs:   `/yhyo++sys.  dd/`/yhs.  -shyso+oyhy+`   .oyhyso-
 .yhy-`   `.+hhd``shy:`    ./hh+ `ohy:`    ``   dhsyhs:`  /hh+.`   .ohh+  -hho-`
 /dh.        +dd`:dd.        /dd`-dd:           dhhy:`   `hd+    ./yhy/` `yds
 +dh`        /dd`:dd`        :dd.-dd-           ddhs.    .hh+ `-ohhs-`   `yh+
 .ydo.     `:hho `yds.`    `-yds `sdy-`         dhyhh+.   +dh/shho-``    `yh+
  .shho/:/+shy/`  .ohhs+//+shh+`  `ohhs+//+so`  dd/-ohh+`  /yhdho/+os-   `yh+
   `-/syyyso:.      -/osyyso:.      -/osyyso/`  oy-  -oy-   `:+syyyo/.    oy:
		   	\033[92m Select your choice:\033[91m
			\033[92m---------------------\033[91m
\033[94m 1. \033[93mDocker Configuration\033[91m        \033[94m 8. \033[93mCreate a Container !\033[91m
\033[94m 2. \033[93mInstall Docker\033[91m              \033[94m 9. \033[93mCheck all created os \033[91m
\033[94m 3. \033[93mDocker Status\033[91m               \033[94m 10. \033[93mDelete all created os \033[91m
\033[94m 4. \033[93mCheck Docker Images\033[91m         \033[94m 11. \033[93mStart Docker Container Network Connectivity\033[91m
\033[94m 5. \033[93mDownload Docker Image\033[91m       \033[94m 12. \033[93mCreate and Configure Webserver\033[91m
\033[94m 6. \033[93mCheck running os\033[91m            \033[94m 13. \033[93mDelete a Container !\033[91m
\033[94m 7. \033[93mDelete Container Image !\033[91m    \033[94m 14. \033[93mExit !\033[91m
	\033[0m''')
            c = input("Enter your choice : ")
            if int(c) == 1:
                f = open("/etc/yum.repos.d/docker.repo", "w")
                f.write(
                    "[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ \ngpgcheck=0 \n")
                f.close()
                print("Cofigured !")
                input()
            elif int(c) == 2:
                print("Please wait, while we are installing !")
                os.system('yum install docker-ce --nobest')
                os.system('systemctl start docker')
                print("Press enter to continue !")
                input()
            elif int(c) == 3:
                print(
                    "Please wait while checking status..\n\033[33mPress Q to exit !\033[0m")
                os.system('systemctl status docker')
            elif int(c) == 4:
                print("Please wait while Collecting Data !")
                os.system('docker images')
                print("Press enter to continue !")
                input()
            elif int(c) == 5:
                docker_image = input(
                    "Enter the name of docker image to pull with version (Default latest) : ")
                print("Please wait image is pulling !")
                os.system('docker pull %s' % (docker_image))
                print("Press enter to continue !")
                input()
            elif int(c) == 6:
                print("Please wait while checking running os in docker !")
                os.system('docker ps')
                print("Press enter to continue !")
                input()
            elif int(c) == 7:
                image_name = input(
                    "Please enter the name of image with version to delete !")
                os.system('docker rmi %s' % (image_name))
                print("Press enter to continue !")
                input()
            elif int(c) == 8:
                os_name = input("Please enter the os_name :")
                image_name = input("please enter name_name: version :")
                os.system('docker run -dit --name %s %s' %
                          (os_name, image_name))
                print("Press enter to continue !")
                input()
            elif int(c) == 9:
                print("Please wait while collecting data !")
                os.system('docker ps -a')
                print("Press enter to continue !")
                input()
            elif int(c) == 10:
                os.system('docker rm -f $(docker ps -a -q)')
                print("Press enter to continue !")
                input()
            elif int(c) == 11:
                print("Please wait while connectivity !")
                os.system(
                    'firewall-cmd --zone=public --add-masquerade --permanent;firewall-cmd --zone=public --add-port=80/tcp;firewall-cmd --zone=public --add-port=443/tcp;firewall-cmd --reload')
                print("Press enter to continue !")
                input()
            elif int(c) == 12:
                print("Please wait while configuring webserver  !")
                os.system('docker run -dit -p 1234:80 --name myos centos:7')
                os.system('docker exec -it myos yum install httpd -y')
                os.system('docker exec -it myos /usr/sbin/httpd')
                os.system('docker exec -it myos ./usr/sbin/httpd')
                print("Press enter to continue !")
                input()
            elif int(c) == 13:
                os.system('docker ps -a')
                os_name = input(
                    "Please give the Container name or first 4 character of id to delete :")
                os.system('docker rm -f %s' % (os_name))
                print("Press enter to continue !")
                input()
            elif int(c) == 14:
                print("Press Enter to Main Menu !")
                input()
                os.system("clear")
                break
            else:
                print("Invalid Option\nPress Enter to continue...")
                input()
    # -------------------------------------------------------hadoop---------------------------------------------------------------
    elif int(a) == 4:
        while True:
            os.system("clear")
            print('''\033[33m
                          :/-` ./oyyyyssso-
                          : -yho/-.......:ohs.
                          .hy.```.........../yy/
                       :yss+::-..............-:+ys.   `++.
                 `-:+ods--oy+/--....:+-.......---/d+`+do+do
             :oyys++my..-ss/-.......+-...--.----odmmys+/-:N-
  `  ./   .sho-```oh-`..+---..:-....-.-yNMh:----+shh------yy
:+`+shd``yh:````-h/`...--.....o/.....-:+/o:----//o-y------om
: ss-my/m+``...:d.`...--......+y-...------------:--+------+N
  -h+dsN/`.....m:`...-........-m:.-----------------------:sd
   -sshs`......+d:.-/-.........m/------------------------/m/
      m-......../dss-........--m/--------/:-------------/ds
      m:.........+d-......---:od/-------::os+:-------:+yd:
      ho.........+d:....-+syyoo/:--/++/---mMMMymyyyyys+-
     :Nm-.........-syssyy+::--------/yNho:dmdsd/
   :hy:oh-........-----------------:/dm/:yysso.
   dy..-oh-......-:-------/-------:/ho+N`
   .dy:-:od-..----/dyyyhhhy-------/hs//N-
     :yhhdN------:om `dh+-------:+do///d+
        .No----::om.  hh---::::ohNyssssm/
        .dds+/://mo    yd/://yd+``.....`
          `-/+ssyo`     :hhhho            \033[96m
oooo                        .o8
`888                       "888
 888 .oo.    .oooo.    .oooo888   .ooooo.   .ooooo.  oo.ooooo.
 888P"Y88b  `P  )88b  d88' `888  d88' `88b d88' `88b  888' `88b
 888   888   .oP"888  888   888  888   888 888   888  888   888
 888   888  d8(  888  888   888  888   888 888   888  888   888
o888o o888o `Y888""8o `Y8bod88P" `Y8bod8P' `Y8bod8P'  888bod8P'
                                                      888
                                                     o888o
   	\033[92m Select your choice:\033[91m
	\033[92m---------------------\033[91m
	\033[94m 1. \033[93mHadoop Installation\033[91mL
	\033[94m 2. \033[93mHadoop Status\033[91m
	\033[94m 3. \033[93mConfigure NameNode\033[91m
	\033[94m 4. \033[93mCheck Connected Nodes\033[91m
	\033[94m 5. \033[93mConfigure DataNode\033[91m
	\033[94m 6. \033[93mUpload File\033[91m
	\033[94m 7. \033[93mExit !\033[91m
\033[0m''')
            d = input("Enter your choice : ")
            if int(d) == 1:
                rc = subprocess.call(['which', 'wget'])
                if rc != 0:
                    os.system("yum install wget -y")
                rc = subprocess.call(['which', 'java'])
                if rc != 0:
                    os.system(
                        "wget http://83.103.170.157/apps/java/jdk_1.8/jdk/jdk-8u202-linux-x64.rpm")
                    os.system("rpm -ivh jdk-8u202-linux-x64.rpm")
                rc = subprocess.call(['which', 'hadoop'])
                if rc != 0:
                    os.system(
                        "wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
                    os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
                print("Installed Press Enter!")
                input()
            elif int(d) == 2:
                print(
                    "Please wait while checking status..\n\033[33mPress Q then Enter to exit !\033[0m")
                os.system("systemctl status hadoop")
                input()
            elif int(d) == 3:
                rc = subprocess.call(['which', 'wget'])
                if rc != 0:
                    os.system("yum install wget -y")
                rc = subprocess.call(['which', 'java'])
                if rc != 0:
                    os.system(
                        "wget http://83.103.170.157/apps/java/jdk_1.8/jdk/jdk-8u202-linux-x64.rpm")
                    os.system("rpm -i jdk-8u202-linux-x64.rpm")
                rc = subprocess.call(['which', 'hadoop'])
                if rc != 0:
                    os.system(
                        "wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
                    os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
                f = open("/etc/hadoop/core-site.xml", "w")
                f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://0.0.0.0:9001</value>
</property>
</configuration>
''')
                f.close()
                os.system("mkdir /dataDir")
                f = open("/etc/hadoop/hdfs-site.xml", "w")
                f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/dataDir</value>
</property>
</configuration>
''')
                f.close()
                os.system("systemctl stop firewalld")
                os.system("hadoop namenode -format -y")
                os.system("hadoop-daemon.sh start namenode")
                os.system("netstat -tnlp")
                print("Press enter to continue !")
                input()
            elif int(d) == 4:
                print(
                    "Please wait while checking status..\n\033[33mPress Enter to exit !\033[0m")
                os.system("hadoop dfsadmin -report")
                input()
            elif int(d) == 5:
                rc = subprocess.call(['which', 'wget'])
                if rc != 0:
                    os.system("yum install wget -y")
                rc = subprocess.call(['which', 'java'])
                if rc != 0:
                    os.system(
                        "wget http://83.103.170.157/apps/java/jdk_1.8/jdk/jdk-8u202-linux-x64.rpm")
                    os.system("rpm -i jdk-8u202-linux-x64.rpm")
                rc = subprocess.call(['which', 'hadoop'])
                if rc != 0:
                    os.system(
                        "wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
                    os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
                master = input("Enter Master Node's IP : ")
                f = open("/etc/hadoop/core-site.xml", "w")
                f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>
''' % (master))
                f.close()
                os.system("mkdir /dn")
                f = open("/etc/hadoop/hdfs-site.xml", "w")
                f.write('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/dn</value>
</property>
</configuration>''')
                f.close()
                os.system("systemctl stop firewalld")
                os.system("hadoop-daemon.sh start datanode")
                os.system("jps")
                input()
            elif int(d) == 6:
                filename = input("Please enter the file name with location :")
                os.system("hadoop fs -put %s" % (filename))
                os.system()
                input()

            elif int(d) == 7:
                print("Press Enter to Main Menu !")
                input()
                os.system("clear")
                break
            else:
                print("Invalid Option\nPress Enter to continue...")
                input()

    # -------------------------------------------------------AWS---------------------------------------------------------------
    elif int(a) == 5:
        if boto_check == 0:
            print("\033[33m Please wait while downloading the dependency !")
            pip.main(['install', 'boto3'])
            boto_check = 1
        import boto3

        ec2 = boto3.client('ec2')
        s3 = boto3.client('s3')
        while True:
            os.system("clear")
            print('''\033[97m
   `.---::-.   `:::`-:/:` .-::.      .---.
  `.---.-::/:  `/++++oooo/ossss+   :syyyyys/   +ssssooo+  `-///:.    ... `..`
  ``..   -://` .+++/.-oooo/:+sss- .syy/-:yyy/  /ooosssso `ossoooo+`  /+/://::-
    `..--:://` .+++-  /ooo  .sss-  .--``.syy+     -ssso` /sso  :oo+  +++/.-:::`
  `.---..-://` .+++.  /ooo  .sss-  :oyyyyyyy+    /yyy+   sss/  `ooo. +++.  :::.
  .---   -://` .+++.  /ooo  .sss- :yyy:``syy+  `+yyy:    sss/   ooo- ++/.  -::`
  .---``.:://- .+++.  /ooo  .sss- +yyy  .yyyo `oyyys+/-` +ss+  `ooo. ++/.  -::`
  `.----:--:/- .+++.  /ooo  .sss- :yyyssyyyyy:.yyyyyysss`.sss:-/oo/  ++/.  -::`
    ````   .`   .--`  .::-  `///`  -+ooo:`/o: `+:..`.-/+` .+soooo:`  ///`  -:-` \033[33m
             /+:`                             ./osyyso. *
              `/so/-`                         `-.-.-sh:
                `:oyys+:-`                  `-/oyy/ yy`
                   ./oyyyyyso++//:::://++oyhhhho:` /y-
                      `-/+syyyyhhhhhhhhhhhyo/-`    +.
                            `--://///::-.
		   	\033[92m Select your choice:\033[91m
			\033[92m---------------------\033[91m
\033[94m 1. \033[93m Installing Amazon CLI\033[91m			\033[94m 2. \033[93m List All AvailabilityZone !\033[91m
\033[94m 3. \033[93m Configuring AWS CLI Tools\033[91m			\033[94m 4. \033[93m List All Instances \033[91m
\033[94m 5. \033[93m Launch an Instance\033[91m				\033[94m 6. \033[93m List All KeyPairs \033[91m
\033[94m 7. \033[93m Attach A Volume\033[91m        			\033[94m 8. \033[93m List All SecurityGroups\033[91m
\033[94m 9. \033[93m Create S3 Bucket\033[91m       			\033[94m 10. \033[93mList All Subnets\033[91m
\033[94m 11. \033[93mAttach S3 bucket to CloudFront\033[91m		\033[94m 12. \033[93mList All InstanceTypeOfferings!\033[91m
\033[94m 13. \033[93mTerminate os\033[91m    				\033[94m 14. \033[93mList All Volume Created\033[91m
\033[94m 15. \033[93mExit\033[91m    					\033[94m 16. \033[93mList All VolumeOffering\033[91m
\033[0m''')
            d = input("Enter your choice : ")
            if int(d) == 1:
                pip.main(['install', 'awscli'])
                print("Installed Press Enter!")
                input()
            elif int(d) == 2:
                response = ec2.describe_regions()
                print('   \t\t Region \n\t ------------------------')
                count = 1
                for rg in response['Regions']:
                    print("\t%s\t%s" % (count, rg['RegionName']))
                    count += 1
                print("\n   \t Zones in Current Region \n\t ------------------------")
                response = ec2.describe_availability_zones()
                count = 1
                for sn in response['AvailabilityZones']:
                    print("\t%s\t%s" % (count, sn['ZoneName']))
                    count += 1
                input("\n Press Enter to exit !")
            elif int(d) == 3:
                print(
                    "Please Enter the Following Details : ")
                os.system("aws configure")
                print('Configured!')
                input()
            elif int(d) == 4:
                response = ec2.describe_instances()
                count = 1
                print('  {0:3}    {1:30s}  {2:15s}     {3:15s}   {4:7s}'.format(
                    "S No. ", "NAME", "INSTANCE ID", "IP ADDRESS", "STATE"))
                for reservation in response["Reservations"]:
                    for instance in reservation["Instances"]:
                        if instance['State']['Name'] == "running":
                            if instance.__contains__("Tags"):
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, instance["Tags"][0]["Value"], instance["InstanceId"],
                                    instance["PublicIpAddress"], "RUNNING"))
                                count += 1
                            else:
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, "No Name", instance["InstanceId"], instance["PublicIpAddress"], "RUNNING"))
                                count += 1
                        elif instance['State']['Name'] == "stopped":
                            if instance.__contains__("Tags"):
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, instance["Tags"][0]["Value"], instance["InstanceId"], "No IP ADDRESS",
                                    "STOPPED"))
                                count += 1
                            else:
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, "No Name", instance["InstanceId"], "No IP ADDRESS", "STOPPED"))
                                count += 1
                input("\n Press Enter to exit !")
            elif int(d) == 5:
                proc = 0
                ec2 = boto3.client('ec2')
                choice= input("Enter your choice: ")
                if len(choice) > 4:
                    AMI = choice
                else:
                    print('Wrong Option Start Again !')
                    proc = 1
                # AMI_all_Images = {1: ["Amazon Linux 2 AMI (HVM), SSD Volume Type", "ami-0e306788ff2473ccb"],
                #                   2: [" Red Hat Enterprise Linux 8 (HVM), SSD Volume Type", "ami-052c08d70def0ac62"],
                #                   3: [" SUSE Linux Enterprise Server 15 SP2 (HVM), SSD Volume Type",
                #                       "ami-0d0522ed4db1debd6"],
                #                   4: [" Ubuntu Server 20.04 LTS (HVM), SSD Volume Type", "ami-0cda377a1b884a1bc"],
                #                   5: [" Microsoft Windows Server 2019 Base", "ami-0b2f6494ff0b07a0e"],
                #                   6: [" Microsoft Windows Server 2019 Base with Containers", "ami-0295b81b270caa9d2"],
                #                   7: [" Microsoft Windows Server 2019 with SQL Server 2017 Standard",
                #                       "ami-0482c1912c3398780"]}
                # if proc == 0:
                #     print("Choose the AMI to Launch Instance")
                #     print('  {0:3}    {1:80s}  {2:30s}  '.format(
                #         "S No", "Name", "Image ID"))
                #     for i in AMI_all_Images:
                #         print('  {0:3}    {1:80s}  {2:30s}  '.format(
                #             i, AMI_all_Images[i][0], AMI_all_Images[i][1]))

                    # choice = input("Enter your choice: ")
                    # if choice != 0 and choice <= int(AMI_all_Images.__len__()):
                    #     AMI = AMI_all_Images[choice][1]
                    # else:
                    #     print('Wrong Option Start Again !')
                    #     proc = 1
                if proc == 0:
                    temp = {}
                    print('\t\t\t\t   Subnets:')
                    print('\t\t\t\t---------------\n')
                    sn_all = ec2.describe_subnets()
                    count = 1
                    print("\t%s\t%s\t%s\t\t\t%s\n" %
                          ("S No.", 'AvailabilityZone', 'SubnetId', 'VpcId'))
                    for sn in sn_all['Subnets']:
                        print("\t%s\t%s\t\t%s\t%s" % (
                            count, sn['AvailabilityZone'], sn['SubnetId'], sn['VpcId']))
                        temp[count] = sn['SubnetId']
                        count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        SUBNET = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    temp = {}
                    type_offerings = ec2.describe_instance_type_offerings()
                    for type in type_offerings["InstanceTypeOfferings"]:
                        temp[type['InstanceType']] = type["Location"]
                    new = input(
                        "Enter the Instance type (Without space in start and end e.g. t2.micro):")
                    if temp.__contains__(new):
                        INSTANCE_TYPE = new
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    temp = {}
                    kp_all = ec2.describe_key_pairs()
                    count = 1
                    print('\n\t   Key-Pairs')
                    print('\t------------- \n')
                    for kp in kp_all['KeyPairs']:
                        print("\t%s\t%s" % (count, kp['KeyName']))
                        temp[count] = kp['KeyName']
                        count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        KEY = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    temp = {}
                    response = ec2.describe_security_groups()
                    print('\n\t  securityGroups')
                    print('\t------------------\n')
                    print('{0:3s} {1:15s}     {2:15s} '.format(
                        "Sno", "Name", "ID"))
                    count = 1
                    for securityGroups in response['SecurityGroups']:
                        print('{0:3d} {1:15s}     {2:15s} '.format(
                            count, securityGroups['GroupName'], securityGroups['GroupId']))
                        temp[count] = securityGroups['GroupId']
                        count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        SECURITY = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    choice = int(
                        input("Enter the no. of Instance you want to laaunch :"))
                    if choice != 0:
                        COUNT = choice
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    os.system(
                        "aws ec2 run-instances --image-id  %s --subnet-id %s --instance-type %s --key-name %s --security-group-ids %s --count %s" %
                        (AMI, SUBNET, INSTANCE_TYPE, KEY, SECURITY, COUNT))
                    print("Instanxe Launched")

                input("Press Enter to Continue !")
            elif int(d) == 6:
                print('\n\t   Key-Pairs')
                print('\t------------- \n')
                kp_all = ec2.describe_key_pairs()
                count = 1
                for kp in kp_all['KeyPairs']:
                    print("\t%s\t%s" % (count, kp['KeyName']))
                    count += 1
                input("\n Press Enter to exit !")
            elif int(d) == 7:
                proc = 0
                if proc == 0:
                    ALL_VOLUME_TYPE = {
                        1: "standard",
                        2: "io1",
                        3: "io2",
                        4: "gp2",
                        5: "sc1",
                        6: "st1"
                    }
                    print("Choose the  volume type: ")
                    print('  {0:3}    {1:80s} '.format("S No", "Name"))
                    for i in ALL_VOLUME_TYPE:
                        print('  {0:3}    {1:80s} '.format(
                            i, ALL_VOLUME_TYPE[i]))

                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(ALL_VOLUME_TYPE.__len__()):
                        VOLUME_TYPE = ALL_VOLUME_TYPE[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    temp = int(input("Enter the size of volme : "))
                    if temp != 0:
                        SIZE = temp
                if proc == 0:
                    temp = {}
                    print(
                        "\n   \t Zones in Current Region \n\t ------------------------")
                    response = ec2.describe_availability_zones()
                    count = 1
                    for sn in response['AvailabilityZones']:
                        print("\t%s\t%s" % (count, sn['ZoneName']))
                        temp[count] = sn['ZoneName']
                        count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        ZONE = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    VOLUME_ID = subprocess.getoutput(
                        " aws ec2 create-volume --volume-type %s --size %s --availability-zone %s  --query \"VolumeId\"" % (
                        VOLUME_TYPE, SIZE, ZONE))
                    print("Your Volume is is : ", VOLUME_ID)
                if proc == 0:
                    response = ec2.describe_instances()
                    count = 1
                    temp = {}
                    print('  {0:3}    {1:30s}  {2:15s}     {3:15s}   {4:7s}'.format(
                        "S No. ", "NAME", "INSTANCE ID", "IP ADDRESS", "STATE"))
                    for reservation in response["Reservations"]:
                        for instance in reservation["Instances"]:
                            if instance['State']['Name'] == "running":
                                if instance.__contains__("Tags"):
                                    print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                        count, instance["Tags"][0]["Value"], instance["InstanceId"],
                                        instance["PublicIpAddress"], "RUNNING"))
                                    temp[count] = instance["InstanceId"]
                                    count += 1
                                else:
                                    print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                        count, "No Name", instance["InstanceId"], instance["PublicIpAddress"],
                                        "RUNNING"))
                                    temp[count] = instance["InstanceId"]
                                    count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        INSTANCE_ID = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    os.system(
                        "aws ec2 attach-volume --volume-id %s --instance-id %s --device /dev/sdf" % (VOLUME_ID, INSTANCE_ID))
                input("Press Enter to Continue !")
            elif int(d) == 8:
                response = ec2.describe_security_groups()
                print('\n\t  securityGroups')
                print('\t------------------\n')
                print('{0:3s} {1:15s}     {2:15s} '.format(
                    'S no.', 'Name', 'ID'))
                count = 1
                for securityGroups in response['SecurityGroups']:
                    print('{0:3d} {1:15s}     {2:15s} '.format(
                        count, securityGroups['GroupName'], securityGroups['GroupId']))
                    count += 1
                input("\nPress Enter to exit !")
            elif int(d) == 9:
                proc = 0
                public = 0
                if proc == 0:
                    temp = {}
                    response = ec2.describe_regions()
                    print('   \t\t Region \n\t ------------------------')
                    count = 1
                    for rg in response['Regions']:
                        print("\t%s\t%s" % (count, rg['RegionName']))
                        temp[count] = rg['RegionName']
                        count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        ZONE = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    choice = int(input(
                        "Do you want to make  your Bucket Public (Press 0 for NO or Pess 1 for YES  ): "))
                    if choice >= 0 and choice <= 1:
                        public = 1
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    temp = input(
                        "Enter the unique name of Bucket you want to launch (do not use \"_\") :")
                    if temp != "":
                        NAME = temp
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    i = os.system(
                        "aws s3api create-bucket --bucket %s --region %s --create-bucket-configuration LocationConstraint=%s" % (NAME, ZONE, ZONE))
                    if public != 0 and i == 0:
                        os.system(
                            "aws s3api put-bucket-acl --acl public-read --bucket %s" % (NAME))
                input("Press Enter to Continue!")
            elif int(d) == 10:
                print('\t\t\t\t   Subnets:')
                print('\t\t\t\t---------------\n')
                sn_all = ec2.describe_subnets()
                count = 1
                print("\t%s\t%s\t%s\t\t\t%s\n" %
                      ("S No.", 'AvailabilityZone', 'SubnetId', 'VpcId'))
                for sn in sn_all['Subnets']:
                    print("\t%s\t%s\t\t%s\t%s" % (
                        count, sn['AvailabilityZone'], sn['SubnetId'], sn['VpcId']))
                    count += 1
                input("\nPress Enter to exit !")
            elif int(d) == 11:
                proc = 0
                if proc == 0:
                    response = s3.list_buckets()
                    temp = {}
                    count = 1
                    print("\t   S3 Bucket")
                    print("\t  -------------")
                    for b in response['Buckets']:
                        if b.__contains__("Name"):
                            temp[count] = b['Name']
                            print('    {0:3d}   {1:20s}'.format(count, b['Name']))
                            count += 1
                    choice = int(input("Enter your choice: "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        BUCKET_NAME = temp[choice]
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1

                if proc == 0:
                    response = s3.list_objects(
                        Bucket=BUCKET_NAME)
                    temp = {}
                    count = 1
                    print("\t   S3 Bucket Objects")
                    print("\t  ---------------------")
                    for b in response['Contents']:
                        if b.__contains__("Key"):
                            temp[count] = b['Key']
                            print('    {0:3d}   {1:20s}'.format(count, b['Key']))
                            count += 1
                    choice = int(
                        input("Enter your choice (Don't select Folders ): "))
                    if choice != 0 and choice <= int(temp.__len__()):
                        if temp[choice][-1] != "/":
                            BUCKET_ROOT_OBJECT = temp[choice]
                        else:
                            print("You Can't Select Folder Start Again ! ")
                            proc = 1
                    else:
                        print('Wrong Option Start Again !')
                        proc = 1
                if proc == 0:
                    os.system(
                        "aws cloudfront create-distribution --origin-domain-name %s.s3.amazonaws.com --default-root-object %s" %
                        (BUCKET_NAME, BUCKET_ROOT_OBJECT))
                input()
            elif int(d) == 12:
                print('\n InstanceTypeOfferings')
                print('-----------------------\n')
                type_offerings = ec2.describe_instance_type_offerings()
                count = 1
                for type in type_offerings["InstanceTypeOfferings"]:
                    print('{0:3d}   {1:15s} '.format(
                        count, type['InstanceType']))
                    count += 1
                input()
            elif int(d) == 13:
                response = ec2.describe_instances()
                count = 1
                temp = {}
                print('  {0:3}    {1:30s}  {2:15s}     {3:15s}   {4:7s}'.format(
                    "S No. ", "NAME", "INSTANCE ID", "IP ADDRESS", "STATE"))
                for reservation in response["Reservations"]:
                    for instance in reservation["Instances"]:
                        if instance['State']['Name'] == "running":
                            if instance.__contains__("Tags"):
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, instance["Tags"][0]["Value"], instance["InstanceId"],
                                    instance["PublicIpAddress"], "RUNNING"))
                                temp[count] = instance["InstanceId"]
                                count += 1
                            else:
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, "No Name", instance["InstanceId"], instance["PublicIpAddress"], "RUNNING"))
                                temp[count] = instance["InstanceId"]
                                count += 1
                        elif instance['State']['Name'] == "stopped":
                            if instance.__contains__("Tags"):
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, instance["Tags"][0]["Value"], instance["InstanceId"], "No IP ADDRESS",
                                    "STOPPED"))
                                temp[count] = instance["InstanceId"]
                                count += 1
                            else:
                                print('  {0:3}    {1:30s}  {2:15s}   {3:15s}   {4:7s}'.format(
                                    count, "No Name", instance["InstanceId"], "No IP ADDRESS", "STOPPED"))
                                temp[count] = instance["InstanceId"]
                                count += 1
                choice = int(input("Enter your choice: "))
                if choice != 0 and choice <= int(temp.__len__()):
                    os.system("aws ec2 terminate-instances --instance-ids %s" % (temp[choice]))
                else:
                    print('Wrong Option Start Again !')
                input("Press Enter to Continue !")
            elif int(d) == 14:
                print('\t\t\t       Volumes Details')
                print('\t\t\t    --------------------\n')
                print(f"AvailabilityZone  \t\tVolumeId  \t\tName\n")
                volumes_all = ec2.describe_volumes()
                for vol in volumes_all["Volumes"]:
                    if vol.__contains__("Tags"):
                        print(
                            f'{vol["AvailabilityZone"]}  \t\t{vol["VolumeId"]}  \t\t{vol["Tags"][0]["Value"]}')
                    else:
                        print(
                            f'{vol["AvailabilityZone"]}  \t\t{vol["VolumeId"]}  \t\t{"NO Name"}')
                input("Press enter to exit !")
            elif int(d) == 16:
                print('\n\nAll Available Volumes Types')
                print("----------------------------")
                print('''
gp2 - General Purpose (SSD)
io1 - Provisioned IOPS (SSD)
io2 - Provisioned IOPS (SSD)
sc1 - Cold HDD
st1 - Throughput Optimized hard disk drive (HDD)
Magnetic (standard)
''')
                input()
            elif int(d) == 15:
                print("Press Enter to Main Menu !")
                input()
                os.system("clear")
                break
            else:
                print("Invalid Option\nPress Enter to continue...")
                input()
    # --------------------------------------------------------------------------------------------------------------
    elif int(a) == 6:
        print("Bye !")
        input()
        os.system("clear")
        break
    else:
        print("Invalid Option")
        input()
