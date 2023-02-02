import requests

class servicePostVideo:
    """Classe que executas validacoes, acessos ao banco e outros."""

    def __init__(self) -> None:
        pass

    def validate_get_video(self, get_video: str) -> bool:
        url = f"http://localhost:8000/posts/{get_video}"
        response = requests.get(url)
        #get the route and download the video in past files
        if response.status_code == 200:
            with open("files/video.3gp", "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
        return False

    def list_videos(self) -> dict[str, str]:
        """
        Retorna as videos disponiveis.
        """
        video_1 = {"name": "video_1",
                   "description": "video_1",
                   "local": "files/video.3gp"}
        return video_1
