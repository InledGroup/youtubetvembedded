import sys
import os
import subprocess
import time
import xbmc
import xbmcaddon
import xbmcgui

# Try importing pynput, notify if missing
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# Addon Info
ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')

def log(msg, level=xbmc.LOGINFO):
    xbmc.log(f"[{ADDON_ID}] {msg}", level)

def launch_browser():
    browser_path = ADDON.getSetting('browser_path')
    user_agent = ADDON.getSetting('user_agent')
    url = ADDON.getSetting('custom_url')

    if not os.path.exists(browser_path):
        xbmcgui.Dialog().ok("Error", f"Browser executable not found at:\n{browser_path}\nPlease check addon settings.")
        return

    if not PYNPUT_AVAILABLE:
        xbmcgui.Dialog().ok("System Dependency Missing", "The 'pynput' library is required to handle the Exit key.\nPlease install it on your OS (in Debian/Ubuntu and based distros 'apt install python3-pynput') to avoid getting stuck in the browser.")
        return
    
    # Construct command
    # --kiosk: Fullscreen, no borders
    # --no-first-run, --no-default-browser-check: suppress warnings
    # --user-data-dir: explicit profile (optional, maybe uses default if omitted, strictly safer to use a custom temp one or let it use default but user might be logged in default)
    # User might want to be logged in to YouTube, so using default profile (omitting user-data-dir) is better for UX, 
    # but might conflict if browser is already open.
    # Let's try standard launch first.
    
    cmd = [
        browser_path,
        "--kiosk",
        f"--user-agent={user_agent}",
        "--no-first-run",
        "--no-default-browser-check",
        # "--start-maximized", 
        url
    ]

    log(f"Launching command: {' '.join(cmd)}")

    try:
        # Start the browser process
        proc = subprocess.Popen(cmd)
        
        # Listener logic
        listener = None
        exit_timer = None
        cec_monitor = None

        if PYNPUT_AVAILABLE:
            from threading import Timer
            keyboard_controller = keyboard.Controller()

            def kill_browser():
                log("Long press detected. Force terminating browser...")
                proc.terminate()

            def on_press(key):
                nonlocal exit_timer
                try:
                    # Check for ESC or Media Stop
                    if key == keyboard.Key.esc or key == keyboard.Key.media_stop:
                        log("Exit/Stop key detected. Terminating browser...")
                        proc.terminate()
                        return False # Stop listener

                    # Check for Backspace (Back)
                    if key == keyboard.Key.backspace:
                        # Only start timer if not already running (debounce autorepeat)
                        if ADDON.getSetting('enable_long_press') == 'true' and exit_timer is None:
                            exit_timer = Timer(3.0, kill_browser)
                            exit_timer.start()
                            
                except AttributeError:
                    pass

            def on_release(key):
                nonlocal exit_timer
                if key == keyboard.Key.backspace:
                    if exit_timer:
                        exit_timer.cancel()
                        exit_timer = None

            listener = keyboard.Listener(on_press=on_press, on_release=on_release)
            listener.start()

            # CEC Monitor Implementation
            if ADDON.getSetting('enable_cec') == 'true':
                class CECMonitor(xbmc.Monitor):
                    def onAction(self, action):
                        try:
                            action_id = action.getId()
                            # log(f"CEC Action Received: {action_id}")
                            
                            # Map Actions to Keys
                            # 1=Left, 2=Right, 3=Up, 4=Down
                            # 7=Select/Enter, 10=Back
                            # 13=Stop
                            
                            key_to_press = None
                            
                            if action_id == 1: key_to_press = keyboard.Key.left
                            elif action_id == 2: key_to_press = keyboard.Key.right
                            elif action_id == 3: key_to_press = keyboard.Key.up
                            elif action_id == 4: key_to_press = keyboard.Key.down
                            elif action_id == 7: key_to_press = keyboard.Key.enter
                            elif action_id == 10: key_to_press = keyboard.Key.backspace
                            elif action_id == 13: 
                                # Stop handled via simulation or directly terminating?
                                # Let's simulate the key so the Listener picks it up and handles logic consistently
                                key_to_press = keyboard.Key.media_stop 
                            
                            if key_to_press:
                                keyboard_controller.press(key_to_press)
                                keyboard_controller.release(key_to_press)
                                
                        except Exception as e:
                            log(f"CEC Bridge Error: {e}", xbmc.LOGERROR)

                cec_monitor = CECMonitor()

        # Wait for browser to close (either by user or by our terminate)
        proc.wait()
        
        if listener:
            listener.stop()
        
        # Cleanup
        if exit_timer:
            exit_timer.cancel()
        
        if cec_monitor:
            del cec_monitor # Deregister monitor

    except Exception as e:
        log(f"Error launching browser: {e}", xbmc.LOGERROR)
        xbmcgui.Dialog().ok("Error", f"Failed to launch browser:\n{e}")

if __name__ == '__main__':
    launch_browser()
