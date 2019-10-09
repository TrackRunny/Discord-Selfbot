<!-- MAIN TITLE -->
# LinuxBoi • Discord bot

<!-- LINUX BOI PICTURE -->
  <img align="right" src="https://i.imgur.com/aiIXeCJ.png" width=30%>

<!-- BADGES -->
  ![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue?style=flat-square)
  ![Discord.py Version](https://img.shields.io/badge/discord.py-1.2.3-blue?style=flat-square)
  ![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square)
  ![Uptime - 7 Days](https://img.shields.io/uptimerobot/ratio/7/m783522026-b61cac99a2e1ba3a3d6f251c?style=flat-square)
  ![Uptime - Current Time](https://img.shields.io/uptimerobot/status/m783522026-b61cac99a2e1ba3a3d6f251c?style=flat-square)
  <a href="https://app.codacy.com/manual/TrackRunny/Discord-Selfbot/dashboard?bid=14423857&token=vnDn11JbhCP7nhu">![Code Quality](https://img.shields.io/codacy/grade/179a29ed15bb40b5b0eed2b695791f94?style=flat-square)</a>  

<!-- KEY INFORMATION HEADER -->
### →  Important Information

  * Official GitHub repo for LinuxBoi.
  * Multi-use Discord bot that is being actively developed.
  * Main purpose is to teach / help people about Linux on Discord.
  * 2 -3 Commits each week.
  * Uptime should be over 95% each 7 days as shown from the badge above.

<!-- MODULES HEADER -->
### → Modules

  * Events  
  * Fun
  * Information
  * Linuxinfo (coming soon)
  * Meme (being tested)
  * Moderation
  * Music ([Lavalink.py](https://github.com/Devoxin/Lavalink.py "Lavalink.py") for good sound quality)
  * Owner
  * Utility

<!-- INSTALLATION HEADER -->
### → Installation

  **Please note that I would rather you not run another instance of the bot and just invite it to your server. If you really want to run it with your own token for testing or another reason, please follow the directions below to run it.**

  Also note that **MAC OS X CANNOT\*** run [**Lavalink Server**](https://github.com/Devoxin/Lavalink.py "Lavalink.py") due to a missing library that is required to run it. You can attempt to run [**Lavalink Server**](https://github.com/Devoxin/Lavalink.py "Lavalink.py") on it, but when you try to play sound nothing will come out. You should get an error like this: `java.lang.UnsatisfiedLinkError: Required library at /natives/darwin/libudpqueue.dylib was not found`. Currently [**Lavalink Server**](https://github.com/Devoxin/Lavalink.py "Lavalink.py") supports Windows and Linux.
  [**Lavalink.py**](https://github.com/Devoxin/Lavalink.) does support Mac OS X, however this is a wrapper for Lavalink server. Lavalink server allows you to play sound with the bot.

  \* Its not impossible to try and compile Lavalink.jar with Mac natives up and running, though it has been done before but I personally have never tried it.

---

  There is a requirements.txt file that anyone on **Any Operating That Supports Python 3.6+** can use to install **All\*** of the dependences needed for LinuxBoi to run. If your computer / server has two versions of **python and / or you have python 2 and python 3 installed make sure to use python 3.6+**. Installation instructions are below as follows:

  * \*First install this **dependency** and built from source. This is a bitly api dependency for a shortenlink command.

  ```markdown
  git clone https://github.com/bitly/bitly-api-python.git

  cd bitly-api-python/

  python setup.py install
  <!-- Remember: Only Use this if you only have python 3 installed. -->

  or

  python3 setup.py install
  <!-- Remember: Use this if you have two versions of python and / or you have python 2 and python 3. -->

  ```

  * Next clone this repo and install the dependencies from the txt file.

  ```markdown
  git clone https://github.com/TrackRunny/LinuxBoi.git

  cd LinuxBoi

  pip install --user --requirement requirements.txt
  <!-- Remember: Only use this if you only have python 3 installed. -->

  or

  pip3 install --user --requirement requirements.txt
  <!-- Remember: Use this if you have two versions of python and / or you have python 2 and python 3. -->  
  ```

  * If your using windows, please read this portion below.

  <details>
    <summary><b>Click here</b></summary>
    <h3>• Error: Microsoft Visual C++ 14.0 is required.</h3>
    <p>Note, some users may recieve this error above when trying to install the dependences from the requirements.txt file. This happens when you are trying to build and install the <b>Pycosat</b> pip module. If this happens to you, please follow the instructions below.</p>
  
  1. Download the compiled **Pycosat** file for your Python version and windows architecture.
      * [**Pycosat | Python 3.6 | Win32**](https://download.lfd.uci.edu/pythonlibs/g5apjq5m/pycosat-0.6.3-cp36-cp36m-win32.whl)
      * [**Pycosat | Python 3.6 | Win64**](https://download.lfd.uci.edu/pythonlibs/g5apjq5m/pycosat-0.6.3-cp36-cp36m-win_amd64.whl)
      * [**Pycosat | Python 3.7 | Win32**](https://download.lfd.uci.edu/pythonlibs/g5apjq5m/pycosat-0.6.3-cp37-cp37m-win32.whl)
      * [**Pycosat | Python 3.7 | Win64**](https://download.lfd.uci.edu/pythonlibs/g5apjq5m/pycosat-0.6.3-cp37-cp37m-win_amd64.whl)
  2. Change directories into the downloaded file.
  3. Install the compiled pip module.

  ```markdown
    pip install pycosat-0.6.3-cp36-cp36m-win32.whl
    <!-- Win32 | Python 3.6 -->

    pip install pycosat-0.6.3-cp36-cp36m-win_amd64.whl
    <!-- Win64 | Python 3.6 -->

    ---

    pip install pycosat-0.6.3-cp37-cp37m-win32.whl
    <!-- Win32 | Python 3.7 -->

    pip install pycosat-0.6.3-cp37-cp37m-win_amd64.whl
    <!-- Win64 | Python 3.7 -->

    or

    pip3 install pycosat-0.6.3-cp36-cp36m-win32.whl
    <!-- Win32 | Python 3.6 | pip3 -->

    pip3 install pycosat-0.6.3-cp36-cp36m-win_amd64.whl
    <!-- Win64 | Python 3.6 | pip3 -->

    ---

    pip3 install pycosat-0.6.3-cp37-cp37m-win32.whl
    <!-- Win32 | Python 3.7 | pip3 -->

    pip3 install pycosat-0.6.3-cp37-cp37m-win_amd64.whl
    <!-- Win64 | Python 3.7 | pip3 -->
  ```

  </details>

### → Enviroment Variables (Continuing Installation)

  There are some enviroment variables you need to have on the computer / server that is running the Discord bot. **If you don't have these the bot will not work correctly!**

  I have created a copy and paste area for all the enviroment variables that you need for the bot. The instructions are below depending on which operating system you use.

  <details>
    <summary><b>Linux</b> (Click the arrow)</summary>
    <h3>• Enviroment Variables On Linux</h3>
    <p>Linux: Put the variables at the end of your <b>.bashrc</b> file. The <b>.bashrc</b> file is located in your home directory. You can copy and paste these and put in the values. These are located under the Windows instructions inside the code block.</p>
    <p>Here is an example of what it should look like.</p>
    <img src="https://i.imgur.com/RC1yyTf.jpg">
  </details>

  <details>
    <summary><b>Mac OS X</b> (Click the arrow)</summary>
    <h3>• Enviroment Variables On Mac</h3>
    <p>Mac OS X: Put the variables at the end of your <b>.bash_profile</b> file. The <b>.bash_profile</b> is located in your home directory. You can copy and paste these and put in the values. These are located under the Windows instructions inside the code block.</p>
    <p>Here is an example of what it should look like.</p>
    <img src="https://i.imgur.com/RC1yyTf.jpg">
  </details>

  <details>
    <summary><b>Windows</b> (Click the arrow)</summary>
    <h3>• Enviroment Variables On Windows</h3>
    <p>Windows: The process is a little more difficult on Windows. Please watch <a href="https://www.youtube.com/watch?v=IolxqkL7cD8">this</a> video so you can export these values on your Windows Operating System. Skip to <b>1:19</b> if you want to see how he does it. Make sure to keep the enviroment variables with the same name or they won't work. The variable names are inside the code block just under this piece of text.</p>
  </details>
  
  ```markdown
  export ip_info=""
  export email=""
  export email_password=""
  export bitly_user=""
  export bitly_key=""
  export linuxboi_token=""
  export linuxboi_testing_token=""
  ```

  Congrats, everything should be set up correctly so far. If you want to start the bot you can do `./LinuxBoi.py` as it should already be executiable.

---

<!-- LICENSE INFO -->
## → License

  This project is licensed under the GPLv3.

<!-- END OF README -->
## → Questions / Contact me

  * Discord Account: `TrackRunny#3900`
  * Email: `trackrunny@protonmail.com`
