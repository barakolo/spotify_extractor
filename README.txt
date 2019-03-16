# spotify_extractor
in order to work with this script do the following:
1. install python
2. register to spotify developers & create new app in spotify developers console - https://developer.spotify.com/
  2.a. to create a new app enter here and click "create new app" - https://developer.spotify.com/dashboard/applications
  2.b. when finished you will have a client_id & client_secret shown in the app itself!
  2.c. take these values and embed it in the script itself.
  2.d Important: add a redirect url to your new app - e.g: "https://127.0.0.1:5454" 
      ( it is in the app -> edit settings... -> Redirect URIs)
3. Now - almost finished! generate first time token!
  3.a. run the script and get the url to enter in chrome (what comes before "Go and enter with your account into this link and agree that in order to activate it hmmm...")
  3.b. enter in chrome to this url -> AGREE TO USAGE OF YOUR APP -> then get the access token from your url bar.
    The token can be get from the url with this: "https://127.0.0.1:5454/?code=<!!!YOUR_TOKEN_IS_HERE!!!>&state=123"
  3.c. extract this token - and place it in the script - under "cur_token = '<your-token-after-accessing-to-the-url-said!>'"
4. now run the script again - and run test() function - this will write the songs names and artists into "c:\temp\my_saved_songs.txt"

*You can change the path of the saved songs - you can change output_file_name to your own another filename :)
