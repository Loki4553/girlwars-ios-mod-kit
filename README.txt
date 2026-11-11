GIRL WARS iOS MOD KIT
=====================
Put Android Girl Wars skin mods on an iPhone. No jailbreak needed. Windows PC only.
Tested with game version 1.0.17 (iOS). Use at your own risk: modding breaks the game's
terms of service, and a re-signed app is not the official App Store app.
This is a fan-made tool, not affiliated with or endorsed by Y2S Games. The kit
contains no game files and no mods: you bring your own IPA and mod files.

QUICK OVERVIEW
  0. Put your Android mod files in "Put mods here".
  1. Drag your decrypted IPA onto "Make Modded IPA.bat"  -> install it with Sideloadly.
  2. Double-click "Convert Mods for iPhone.bat"          -> copy the files to the phone.
  Always use "Make Modded IPA" first. "Convert Mods for iPhone" won't run until
  "Make Modded IPA" has run.


WHAT YOU NEED (one time)
------------------------
1. Python for Windows: https://www.python.org/downloads/
   During install, tick "Add python.exe to PATH".

2. Sideloadly (free): https://sideloadly.io  - installs the modded game on your iPhone.

3. An Apple ID for Sideloadly:
   - PAID Apple Developer account (recommended): the game installs over the real
     one, you keep your account, and it lasts 1 year. "Sign in with Apple" does
     NOT work in the modded game: log in with EMAIL (see "BEFORE YOU START").
   - FREE Apple ID: the game installs as a SECOND app next to the real one, and you
     CANNOT log in to an existing game account (the game crashes, then says
     "Please wipe Cache to try again!"). Only a NEW guest account works, and its
     progress lives only in that app. The app stops opening after 7 days:
     re-install it with Sideloadly (same Apple ID, don't delete it first) to keep
     your progress. See "FREE APPLE ID" below.

4. A DECRYPTED Girl Wars IPA. The App Store version is encrypted and cannot be
   modded. The kit does not decrypt apps and does not include an IPA.

5. A way to copy files into the game's folder on the iPhone:
   - iMazing (easiest, shows the game's folders), or
   - free: the iPhone Files app (see "FREE COPY METHOD" below).

6. The Android mod files you want (.assetbundle).


BEFORE YOU START - PROTECT YOUR ACCOUNT
---------------------------------------
In the real game, link an EMAIL login to your game account first (game settings).
"Sign in with Apple" does not work in the modded game, so without an email login
you can't get back into your account.
Paid account: you will delete the App Store version, and a guest account without
a linked email would be lost.


STEP 0 - PUT YOUR MODS IN THE KIT
---------------------------------
Copy your Android .assetbundle files into the "Put mods here" folder.
- Just drop them straight in. The kit reads each mod file to find its game folder.
- If the kit can't tell, it shows "??" and the possible folders. Then make the folder
  from the mod's target path. Example: the target path ends in
     ...\files\download\roleprefabsandres\battleprefabandres
  so put the file in
     Put mods here\roleprefabsandres\battleprefabandres\1047.assetbundle
- Only ONE mod per game file. For a different skin of the same file, remove the
  old mod file first.


STEP 1 - MAKE AND INSTALL THE MODDED GAME
-----------------------------------------
1. Drag your decrypted Girl Wars .ipa file onto "Make Modded IPA.bat".
   (The first run sets itself up for about a minute, then reads your IPA for about
   another minute.) Wait for "DONE".
   You get "<name> - MODDED.ipa" next to the original IPA. This step:
   - turns on File Sharing, so you can see and change the game's files;
   - reads the iPhone data the kit needs from YOUR IPA and saves it in "tools":
     which files are BUILT INTO the app, and the iPhone versions of the game's
     shaders. The kit itself contains no game files. This is also how it stays
     correct when a game update adds or removes files;
   - puts in the mods for built-in files (for example some Dates, like Chacha's).
   With no mods in "Put mods here", it only turns on File Sharing and saves that data.

   !! The new IPA only has the built-in mods that are in "Put mods here" RIGHT NOW.
      Keep all your built-in mods in there.

2. Paid account only: delete Girl Wars from your iPhone (only the first time).
   Free Apple ID: keep the real game. The modded one installs as a second app.

3. Plug in the iPhone with a USB cable and unlock it. Open Sideloadly, drag the
   MODDED.ipa in, enter your Apple ID, and click Start.

4. On the iPhone: Settings > General > VPN & Device Management > your Apple ID > Trust.
   If it asks, turn on Settings > Privacy & Security > Developer Mode.

5. Open the game, log in (free Apple ID: play as a NEW guest), and let it
   DOWNLOAD EVERYTHING. Then close the game.
   (Mods only replace files the game has already downloaded.)


STEP 2 - CONVERT AND COPY THE MODS
----------------------------------
1. Double-click "Convert Mods for iPhone.bat". The converted files appear in
   "iPhone Ready\download\<folder>\...".
   If it says "STOP: run 'Make Modded IPA.bat' first", do STEP 1 first.

2. Copy them to the iPhone, into the SAME folder under
   Girl Wars > Documents > download

   With iMazing: Apps > Girl Wars > Documents > download > open the same folder,
   drag in the FILES, and choose Replace.

   !! NEVER replace the whole "download" folder. That deletes the game's files.
      Copy the files inside each folder only.

   If it does NOT ask to Replace, the phone doesn't have that file yet, and the
   game would download the original over your mod later. Cancel. Open the game,
   look at that character or skin once so the game downloads it (you may need to
   unlock it first), close the game, and copy the mod again.

   Files marked "INSIDE THE IPA" (in blue) go into the app with STEP 1.
   Copy one to the phone only if the phone already has that file (it asks to
   Replace). If the phone doesn't have it, skip it.

3. Close the game completely and open it again.


FREE COPY METHOD (without iMazing)
----------------------------------
Apple Devices can only put files in the game's top folder, so you finish on the
iPhone with the Files app. Close the game first.

1. Open the "Apple Devices" app (Windows, from the Microsoft Store) > your iPhone >
   Files > Girl Wars. Drag the "iPhone Ready" folder (or single mod files) onto
   Girl Wars. They land next to "download". Nothing gets replaced yet.

2. On the iPhone, open Files > On My iPhone > Girl Wars > iPhone Ready > download.
   In each folder, select all the files and tap Move. Choose the same folder under
   Girl Wars > download, then choose Replace.
   No Replace question = the phone doesn't have that file yet (see STEP 2).

3. Delete the "iPhone Ready" folder on the phone afterwards.


FREE APPLE ID
-------------
Logging in to any existing account (Apple, or email made in another
install) crashes the modded game, and after that it only shows "Please wipe Cache
to try again!". If that happens: delete the modded app, untick "Use automatic
bundle ID" in Sideloadly's Advanced Options, type a NEW never-used ID (for example
com.yourname.girlwars2) and install again. Then play as a guest and don't log in.
You can link an email to that guest account and stay logged in, but logging in to
it again on another install crashes again.


LATER
-----
- New mod: put it in "Put mods here" and run "Convert Mods for iPhone".
  - Normal file: copy just that file to the phone.
  - Marked "INSIDE THE IPA" (in blue): run STEP 1 again and install the new MODDED.ipa with
    Sideloadly. It installs over the old one and keeps your game data.
- A different skin for the same file: replace the mod in "Put mods here", then do
  the same as for a new mod.
- Remove a mod from a built-in file: take it out of "Put mods here", run STEP 1
  again and re-install.
- Remove a mod from a normal file: the in-game "Repair" brings the originals back,
  but for ALL files. Afterwards, copy the mods you still want again.
- A skin went back to normal (the game downloaded a new version of that file):
  copy that file again.
- A new game version on the App Store: get the new decrypted IPA, repeat STEP 1
  (Sideloadly installs over the old one, so no need to delete it), and then STEP 2.
  STEP 1 updates the built-in file list for the new version automatically.
  If the kit shows errors on a new game version, it may need an update.
- Free Apple ID: re-install the MODDED.ipa with Sideloadly every 7 days, over the
  old one (don't delete it, or the guest progress is gone).
- Don't use the in-game "Repair" unless you want to remove ALL mods.
