from api_v1.media.img_view import ImgProcess

media_urls = [
    (ImgProcess, '/image/<string:img_type>/<string:img_date>/<string:filename>')
]