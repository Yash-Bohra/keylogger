prerequisites :-
pip install pynput

what does this code DO ?

1. In the on_press function, we open the log file in append mode ("a"). We then check the pressed key and write the corresponding character or special key notation to the file.
2. If the key is a space, we write a space to the file.
3. If the key is an enter, we write a newline character to the file.
4. If the key is a backspace, we write [BACKSPACE] to the file.
5. If the key is a tab, we write [TAB] to the file.
6. If the key is a shift, we write [SHIFT] to the file.
7. If the key is a control key, we write [CTRL] to the file.
8. If the key is an alt key, we write [ALT] to the file.
9. Otherwise, we write the character associated with the key to the file.
10. In the on_release function, we check if the released key is the Escape key (Key.esc). If it is, we stop the listener.

Q) what is a keylogger?
A)is the action of recording the keys struck on a keyboard, typically covertly, so that a person using the keyboard is unaware that their actions are being monitored.

NOTICE->Keyloggers can be considered malicious software, and using them without the user's consent is illegal in many jurisdictions. Make sure you have the necessary permissions and follow all applicable laws and regulations.
 ---------------------------------------------------------------------------------------------**IMPORTANT NOTICE**-----------------------------------------------------------------------------------------------
    
**This code will log all keystrokes, including passwords and sensitive information. Use with caution and only for legitimate purposes.**
