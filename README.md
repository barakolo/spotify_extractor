# spotify_extractor
in order to work with this script do the following:
1. install python
2. register to spotify developers & create new app in spotify developers console - https://developer.spotify.com/
  2.a. to create a new app enter here and click "create new app" - https://developer.spotify.com/dashboard/applications
  2.b. when finished you will have a client_id & client_secret shown in the app itself!
  2.c. take these values and embed it in the script itself.
  2.d Important: add a redirect url to your new app - e.g: "https://127.0.0.1:5454"  - 
      ( it is in the app -> edit settings... -> Redirect URIs)
3. Now - almost finished! generate first time token!
  3.a. run the script and call the function "first_time_usage()" get the url where written: 
  3.b. enter in chrome to this url.
  3.c. extract the token - and place it in the script - under "token = ..."
