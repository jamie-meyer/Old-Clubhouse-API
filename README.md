# Old Clubhouse API

01/25/2021

Python version 3.6+

What Is This?
-------------
It's the Clubhouse API! Probably outdated!

How To Use This
---------------
1. Install the necessary requirements with `pip install -r requirements`
2. Open clubhouse_api.py and enter various tokens and things


[OUTDATED] How to find everything (including tokens)
---------------
1. First, you need to jailbreak your device. Download the program here: [https://checkra.in/#release](https://checkra.in/#release). Use a USB-A to lightning cable (for some reason USB-C doesn't work) and connect your device to your mac. Follow the instructions on the jailbreak program and you'll end up with a jailbreak. Once you have jailbroken your device, install Cydia via the checka1n app (you may need to go into airplane mode).
    
    
    <img width="895" alt="hi" src="https://user-images.githubusercontent.com/31294355/150178772-567f3d21-1af8-4252-b0fb-fe9f235396a3.png">

    
2. Next, you need to download some software on your mac. I'm not going to go in to python virtual environments, but I recommend you look into them and set one up before proceeding (using Python 3 — I used 3.7). I assume for the next part you have done so (but for everything to work you don't actually need to — just highly recommended).
    
    ```
    pip3 install frida-tools objection
    brew install mitmproxy
    ```
    
3. Complete the following tutorial to get the frida server running on your device: 
    
    [iOS](https://frida.re/docs/ios/)
    
4. We'll set up mitmproxy. On your mac, type:
    
    ```
    mitmproxy
    ```
    
5. Find your local IP address for your mac (will likely be something like 192.168.X.X) in System Preferences→Network or ifconfig on the command line. On your iDevice, go to Settings→WiFi and click on the information button for the WiFi you're on. Click Configure Proxy→Manual and enter the IP address you found from your mac and the port 8080. Go to [http://mitm.it](http://mitm.it) on your device and follow the iOS instructions (remember to toggle mitmproxy to On in General→About→Certificate Trust Settings). Traffic should now be proxied. To turn it off, change your proxy settings back to Off.
6. Open the app you want to proxy and use the following command to see the processes running and apps you have (for future reference):
    
    ```
    frida-ps -Uai
    ```
    
7. Use the identifier for your app (in this case we'll use Clubhouse, so the identifier will look something like this: co.alphaexploration.clubhouse) in this command:
    
    ```
    objection -g co.alphaexploration.clubhouse explore
    ```
    
8. The first thing we need to do is disable SSL pinning (most apps won't need this step). You need this because Clubhouse is hardcoding SSL certificates into its code and this step will dynamically replace them with the mitmproxy certificate enabled on your device to allow proxying.
    
    ```
    ios sslpinning disable --quiet
    ```
    
    <img width="700" alt="hi1" src="https://user-images.githubusercontent.com/31294355/150178817-4b154a2f-53f6-4557-b57f-e7b8001ab7f4.png">

    
9. You should now see something that looks like this when you're looking at your mitmproxy terminal window.
    
    <img width="1582" alt="t" src="https://user-images.githubusercontent.com/31294355/150178838-f83d478c-200b-4264-985c-799c580618d1.png">

    
10. You should be able to click on each of the requests and see the request and response headers and data. You can also navigate through arrows. 
11. Go through all the expected and unexpected things you'd do on the app and then go through the request logs and see if there's anything interesting. Make an API wrapper if you want. Once you find some endpoints, feel free to enter unexpected values (don't do anything overtly malicious — that'll get you in trouble and they literally have all your information tied to your device). If objection's SLL pinning bypass didn't work, try: [https://github.com/kov4l3nko/MEDUZA](https://github.com/kov4l3nko/MEDUZA)
12. You can go further and use objection to dump memory, find secrets, etc. You may be able to even find endpoints you wouldn't be able to find with the above approach. Decrypt and pull IPA (then unzip and explore) with: [https://github.com/AloneMonkey/frida-ios-dump](https://github.com/AloneMonkey/frida-ios-dump). You can usually find all the API endpoints (without knowing their parameters) by dumping the IPA, finding the executable, opening it with a hex editor, and searching for known endpoints — this will lead you to the others.
