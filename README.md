# Girl Wars iOS Mod Kit

Convert Android Girl Wars skin mods (`.assetbundle`) so they work on an iPhone.
No jailbreak needed. Runs on Windows.

> **Disclaimer:** fan-made tool, not affiliated with or endorsed by Y2S Games.
> Modding breaks the game's terms of service; use at your own risk.
> This repository contains **no game files, no IPA and no mods**. You bring your own.

Tested with game version **1.0.17** (iOS).

## What it does

- **Make Modded IPA:** takes your decrypted Girl Wars IPA, turns on File Sharing (so you can
  reach the game's files), puts in mods for files that are built into the app, and reads the
  iPhone data the converter needs from *your* IPA.
- **Convert Mods for iPhone:** converts Android mod files to the iOS format (platform,
  shaders), finds the right game folder by itself, and puts the results in `iPhone Ready`.

You then install the modded IPA with Sideloadly and copy the converted files to the game's
`Documents/download` folder (iMazing, or Apple Devices + the Files app).

## What you need

- Windows with [Python](https://www.python.org/downloads/) (tick *Add python.exe to PATH*)
- [Sideloadly](https://sideloadly.io)
- An Apple ID for Sideloadly (paid developer account recommended, see below)
- A **decrypted** Girl Wars IPA (the kit does not decrypt apps)
- Android mod files (`.assetbundle`)
- iMazing, or the free Apple Devices app + iPhone Files app

## Quick start

1. Download this repository (**Code → Download ZIP**) and extract it.
2. Put your mod files in `Put mods here`.
3. Drag your decrypted IPA onto **`Make Modded IPA.bat`**. Install the `- MODDED.ipa` it makes
   with Sideloadly.
4. Double-click **`Convert Mods for iPhone.bat`** and copy the files from `iPhone Ready\download`
   into the same folders under *Girl Wars › Documents › download* on the phone (choose *Replace*).

The first run installs what it needs (about a minute, needs internet).
**Full step-by-step guide: [README.txt](README.txt).**

## Account notes

| | Paid developer account | Free Apple ID |
|---|---|---|
| Install | Replaces the real game | Installs as a second app |
| Your existing account | Works, with **email** login | Doesn't work (game crashes) |
| Sign in with Apple | Doesn't work | Doesn't work |
| Re-install needed | Every year | Every 7 days |

Link an **email** login to your game account before switching to the modded game.

## License

[MIT](LICENSE)
