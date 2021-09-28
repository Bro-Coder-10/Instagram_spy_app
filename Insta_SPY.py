import instaloader
while True:
    print("Welcome to Insta_SPY app."
          "\n\t Here you can view the Name, DP, Bio, following and followers of any account present in IG database.")
    print("App Instructions :"
          "\n \t 1. If prompted for a username provide the exact name including underscores(_) and periods(.)"
          "\n \t 2. Type 'quit()' in username if you wish to exit the Application."
          "\n \t 3. Copy the profile picture URL and paste it in your browser to get the profile picture."
          "\n \t 4. You can choose to download it by right clicking on it to save it!."
          "\n \t 5. Press any key after you view a profile to continue SPY-ing!!"
          "\n \t Have fun!!!"
          "\n\t Note: This app was developed for entertainment purposes only!")
    print(end='='*pow(5, 2))
    print()
    username = input("User name : ")
    if 'quit()' in username:
        break
    else:
        insta = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(insta.context, username)
        print('Full Name : ', profile.full_name)
        print('DP url : ', profile.profile_pic_url)
        print("Bio:\n", profile.biography)
        print('Following : ', profile.followees)
        print('Followers : ', profile.followers)
        input()
