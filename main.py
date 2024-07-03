import cv2, os, yt_dlp
from blessed import Terminal

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
        ascii_image += "\033[0m\n"  # 色のリセットと次の行への移動
    return ascii_image

def play_video(video_path):
    term = Terminal()
    cap = cv2.VideoCapture(video_path)

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.clear())
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            ascii_image = frame_to_colored_ascii(frame)
            print(term.home + ascii_image)
            cv2.waitKey(30)

    cap.release()

if __name__ == "__main__":
    # video_path = input("再生したい動画のパスを入力してください: ")
    # while not (os.path.isfile(video_path)):
    #     video_path = input("正しいパスを入力してください: ")
    #
    url = input("URLを入力してください: ")
    ytdlp_options = {
        'outtmpl': 'outputs/%(id)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info_dict)
        play_video(video_path)