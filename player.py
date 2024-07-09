import cv2, os, yt_dlp, inquirer
from blessed import Terminal
from text_displayer import TextDisplayer
from choice_selector import ChoiceSelector
from animation import Animation
import signal

def signal_handler(sig, frame):
    print("\nプログラムが中断されました。リソースを解放しています...")
    raise SystemExit

signal.signal(signal.SIGINT, signal_handler)
displayer = TextDisplayer()
animation = Animation()

logo = """
 _                           _                _                _      _                             _
| |_   ___  _ __  _ __ ___  (_) _ __    __ _ | |       __   __(_)  __| |  ___   ___          _ __  | |  __ _  _   _   ___  _ __ 
| __| / _ \| '__|| '_ ` _ \ | || '_ \  / _` || | _____ \ \ / /| | / _` | / _ \ / _ \  _____ | '_ \ | | / _` || | | | / _ \| '__|
| |_ |  __/| |   | | | | | || || | | || (_| || ||_____| \ V / | || (_| ||  __/| (_) ||_____|| |_) || || (_| || |_| ||  __/| |   
 \__| \___||_|   |_| |_| |_||_||_| |_| \__,_||_|         \_/  |_| \__,_| \___| \___/        | .__/ |_| \__,_| \__, | \___||_|   
                                                                                            |_|               |___/
"""

def clear_screen():
    print("\33[2J")

def cursor_move(x, y):
    print(f"\033[{y};{x}H")

def bgr_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m█"

def frame_to_colored_ascii(frame, width=160):
    height, original_width, _ = frame.shape
    aspect_ratio = original_width / float(height)
    new_height = int(width / aspect_ratio * 0.55)
    resized_frame = cv2.resize(frame, (width, new_height))

    ascii_image = ""
    for y in range(new_height):
        for x in range(width):
            b, g, r = resized_frame[y, x]
            ascii_image += bgr_to_ansi(r, g, b)
        ascii_image += "\033[0m\n"
    return ascii_image

def play_video(video_path):
    term = Terminal()
    cap = cv2.VideoCapture(video_path)

    try:
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            print(term.clear())
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                ascii_image = frame_to_colored_ascii(frame)
                print(term.home + ascii_image)
                cv2.waitKey(30)
    except Exception as e:
        print(f"再生中にエラーが発生しました: {e}")
    finally:
        cap.release()
        print(term.normal)

if __name__ == "__main__":
    clear_screen()
    cursor_move(0, 0)
    displayer.printIL(logo, 0.3)
    for filename in os.listdir("outputs"):
        file_path = os.path.join("outputs", filename)
        if filename != '.keep' and os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    cursor_move(0, 9)
    displayer.printI("再生方法を選択してください: ", 0.05)
    options = ["URL", "File"]
    selector = ChoiceSelector(options, 11)
    selected_option = selector.run()
    if selected_option == "File":
        video_path = displayer.inputI("再生したい動画のパスを入力してください: ", 0.05)
        while not (os.path.isfile(video_path)):
           video_path = displayer.inputI("正しいパスを入力してください: ", 0.05)
    if selected_option == "URL":
        url = displayer.inputI("URLを入力してください: ", 0.05)
        ytdlp_options = {
        'outtmpl': 'outputs/%(id)s.%(ext)s',
        'noprogress': True,
        'quiet': True,
        'no_warnings': True,
        }
        with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info_dict)

    animation.loading_animation(2.0)
    clear_screen()
    play_video(video_path)
    
    