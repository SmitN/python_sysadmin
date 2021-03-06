#!/usr/bin/env python
import os
import sys
from datetime import datetime
date=datetime.now().strftime('%Y-%m-%d')
repo_dir=("\~/ic-scrips/scripts/build-tools/")
IC_repo_dir=("~/ic-scripts/deployments")
sdr_build="~/ic-scripts/scripts/build-tools/physical-shipment"
sdr_cutover="~/ic-scripts/scripts/build-tools/physical-cutover"
sdr_decomm="~/ic-scripts/scripts/build-tools/Decomm"
print (repo_dir)
menu_actions = {}
# =======================
#      MENU FUNCTIONS
# =======================
#Main Menu

def main_menu():
    global IC_repo_dir
    global repo_dir
    os.system('clear')
    print ("Welcome, \n")
    print ("Please choose the menu you want to start: ")
    print ("1. Build")
    print ("2. Decommission")
    print ("3. Cutover")
    print ("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def exec_menu(choice):
    global state
    global IC_repo_dir
    sdr = ""
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            print (choice)
            if choice == '1':
                state = "Build"
            elif choice == '2':
                state = "Decommission"
            elif choice == '3':
                state = "Cutover"
            menu_actions[ch]()
            #IC_repo_dir=("/ic-scripts/deployments/")
            Build_tools=("/ic-scripts/scripts/build-tools/")
        except KeyError:
            print ("Invalid selection, please try again. \n")
            menu_actions['main_menu']()
    return
def Build():
    print ("Hello Menu 1 !\n")
    print ("8. Physical")
    print ("9. Vmware")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def Decommission():
    print(" Creating Git for Decomission ! \n")
    print ("8. Physical")
    print ("9. Vmware")
    print ("0. exit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def Cutover():
    print ("Creating Git for Cutover !\n")
    print ("8. Physical")
    print ("9. Vmware")
    print ("0. exit")
    choice = input(" >> ")
    exec_menu(choice)
    return

def Physical():
    print ("Creating Git for Physical Host !\n")
    git_name()
    choice = input(" >> ")
    exec_menu(choice)
    return
def Vmware():
    print ("Hello Cutover !\n")
    print ("8. Physical")
    print ("9. Vmware")
    print ("0. exit")
    choice = input(" >> ")
    exec_menu(choice)
    return

def git_name():
    print ("Enter Region")
    region= input(" >>  ")
    print ("Enter Enviornment")
    env = input(" >>  ")
    print ("Enter hostname")
    host= input(" >>  ")
    git_name= str(date) + "_" + str.upper(region[0:2]) + "_" + str.lower(env[0:4]) + "_" +  str.lower(host) + "_" + str.upper(state)
    print (git_name)
    print ("++++++++++++++++++++++++++++++++++++++++++++")
    print ("         CHECK IF IC-SCRIPT EXISTS          ")
    print ("++++++++++++++++++++++++++++++++++++++++++++")
    if os.path.isdir(IC_repo_dir+"/"+ git_name):
        print (str(IC_repo_dir) + str(git_name) + ("exists"))
    else:
        print ("IC-SCRIPTS doesnt exists")
        print ("would you like me to continue with git pull ?")
        res = input(" >> ")
        if res.lower()[0] == 'y':
            print (git_name)
            print(state)
            if state == "Build":
                os.makedirs("~/ic-scripts/deployments/" + git_name)
                print(sdr_build)
            elif state == "Decommission":
                print(sdr_decomm)
            elif state == "cutover":
                print(sdr_cutover)
            else:
                print("NOT A VALID STATE")
                exit()
        else:
            exit()
    return

def back():
    menu_actions['main_menu']()

def exit():
    sys.exit()
menu_actions = {
    'main_menu': main_menu,
    '1': Build,
    '2': Decommission,
    '3': Cutover,
    '8': Physical,
    '9': Vmware,
    '0': exit,
}


if __name__ == "__main__":
    main_menu()
